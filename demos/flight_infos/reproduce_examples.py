#   Process the {train|test}.json files
#   to "realize" the original questions
#   either with
#     - a simplistic realizer using only Python string functions
#     - a realizer that uses pyrealb
#   It computes the BLEU score of each realizer

import json,re,copy,os,sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'RASA_bot','response')))
from calculatebleu import BLEU
from RASA_bot.response.Entities_module import Entities
from show_example import show_example
from RASA_bot.response.realize_example import realize_example

from pyrealb import Constituent
from typing import Callable

Realizer = Callable[[str,Entities,bool], str]

## testing of a single example
def process_example(exampleStr:str,realizer:Realizer) -> None:
    example=json.loads(exampleStr)
    entities = Entities(example['entities'])
    print(realizer(example["intent"],entities,True))
    if len(entities) > 0:
        print("***:", example["intent"], entities)


def gen_example(intent:str,entities:Entities,realizer:Realizer,rname:str,hyps:list[str]) -> None:
    hyp = realizer(intent,entities)
    if len(entities) > 0:
        print("***:", intent, entities)
        # print("TXT",ref)
    print(rname, hyp)
    # retokenize hyp for computing BLEU
    hyps.append(" ".join(w for w in re.split("\W", hyp) if len(w.strip()) > 0))


def process_file(inputF:str) -> None:
    print("Processing:",inputF)
    data = json.load(open(inputF, "r", encoding="utf-8"))
    refs=[] # original sentences
    strs=[] # sentences created with Python string methods
    pyrs=[] # sentences created with pyrealb
    for example in data["rasa_nlu_data"]["common_examples"]:
        intent = example["intent"]
        # if intent=="flight":continue  ## uncomment to filter intents
        entities = Entities(copy.deepcopy(example["entities"]))
        print("---",intent)
        print(entities)
        ref = example["text"]
        print("TXT", ref)
        refs.append(ref)
        gen_example(intent,copy.deepcopy(entities),show_example,"STR",strs)
        entities = Entities(example["entities"])
        gen_example(intent,entities,realize_example,"PYR",pyrs)
    print('---\nBLEU-STR: {:.1%}\nBLEU-PYR: {:.1%}'.format(BLEU(strs,[refs]),BLEU(pyrs,[refs])))

if __name__ == "__main__":
    pwd = os.path.dirname(__file__)
    process_file(os.path.join(pwd,"Examples","train.json"))
    print("="*50)
    process_file(os.path.join(pwd,"Examples","test.json"))
