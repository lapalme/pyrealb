#  convert The ATIS (Airline Travel Information System) Dataset
#  at https://github.com/howl-anderson/ATIS_dataset/blob/master/README.en-US.md
#  into a very similar format except for entities with name containing "."
#  which are split.  The part before the dot is inserted with a new field role.
#  We also patch the position when the first entity is at the start of the sentence
#  The airport, airlines and cities are also changed so that the

import json, os, re
from parse_examples import parse_example

value_ent_role_re = re.compile(r'\[(?P<val>.*?)](\((?P<ent0>.*?)\)|{"entity":"(?P<ent>.*?)","role":"(?P<role>.*?)"})')

def process_entities(entities):
    if len(entities)==0 : return
    if entities[0]["start"] == 1:  # shift entities at the start of the line (should be 0 and not 1)
        entities[0]["start"] -= 1
        entities[0]["end"] -= 1
    for e in entities:
        entity = e["entity"]
        if "." in entity:
            (e["role"],e["entity"])=entity.split(".")

def process_example(example):
    process_entities(example["entities"])
    # ensure that important infos are in the flight DB
    parse_example(example,True)
    # recreate the text from the modified entities
    example["text"] = value_ent_role_re.sub(r"\g<val>", example["text"])

def process_file(fileN):
    print("Processing",fileN)
    data = json.load(open(fileN+".json","r",encoding="utf-8"))
    nb=0
    for example in data["rasa_nlu_data"]["common_examples"]:
        process_example(example)
        nb += 1
    json.dump(data,open(fileN[:-5]+".json","w",encoding="utf-8"),indent=2)
    print("%d examples written on file %s.json"%(nb,fileN[:-5]))

if __name__ == '__main__':
    pwd = os.path.dirname(__file__)
    process_file(os.path.join(pwd, "Examples", "test-orig"))
    process_file(os.path.join(pwd,"Examples","train-orig"))

#  sortie
# Processing /Users/lapalme/Dropbox/pyrealb/demos/flight_infos/Examples/test-orig
# 893 examples written on file /Users/lapalme/Dropbox/pyrealb/demos/flight_infos/Examples/test.json
# Processing /Users/lapalme/Dropbox/pyrealb/demos/flight_infos/Examples/train-orig
# 4978 examples written on file /Users/lapalme/Dropbox/pyrealb/demos/flight_infos/Examples/train.json
