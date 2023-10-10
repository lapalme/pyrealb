import re, random
from datasets import load_dataset
from English import English
from Francais import Francais

## https://gem-benchmark.com/data_cards/e2e_nlg
split_names = ["train", "validation", "test",
               "challenge_train_sample","challenge_validation_sample","challenge_test_scramble"]

def mr_to_json(mr):
    return {mo.group("key"):mo.group("value") for mo in
            re.finditer(r"(?P<key>\w+?)\[(?P<value>.*?)\](, )?",mr)}

def realize_all(d):
    print("id: ",d["gem_id"])
    print("mr: ", d["meaning_representation"])
    phrase_type = random.choice([1, 2, 3])
    print("en :", english.realize(mr_to_json(d["meaning_representation"]), phrase_type))
    print("fr :", francais.realize(mr_to_json(d["meaning_representation"]), phrase_type))
    print("tgt:", d["target"])

if __name__ == "__main__":
    split= split_names[-1]
    print("Dataset:",split)
    dataset = load_dataset("GEM/e2e_nlg",split=split)
    english = English()
    francais = Francais()
    for i in range(1,dataset.num_rows,7):
        realize_all(dataset[i])
        print("---")

