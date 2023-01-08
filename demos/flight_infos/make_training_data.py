import json, os
from collections import Counter
from parse_examples import parse_example


def create_intents(allIntents, allEntities, rasa_dir):
    q = "'"
    qq = "''"
    for intent in allIntents:
        if len(allIntents[intent]) > 1:  # RASA needs at least 2 examples of each intent...
            nlu_yaml = open(os.path.join(rasa_dir, "data", f"intent-{intent}.yml"), "w", encoding="utf-8")
            print('version: "3.1"\nnlu:', file=nlu_yaml)
            print(f"- intent: {intent}", file=nlu_yaml)
            print("  examples: |", file=nlu_yaml)
            for text, entitySet in allIntents[intent]:
                keep = True
                for e in entitySet:
                    if allEntities[e][0] < 2:  # RASA needs at least 2 examples of each entity...
                        print('Hapax %s:%s' % (e, text))
                        keep = False
                if keep:
                    print(f"    - '{text.replace(q, qq)}'", file=nlu_yaml)
            print("Wrote", nlu_yaml.name)


def create_domain(allIntents, allEntities, rasadir):
    domain_yaml = open(os.path.join(rasadir, "domain.yml"), "w", encoding="utf-8")
    print("""version: "3.1"

session_config:
  session_expiration_time: 60
  carry_over_slots_to_new_session: true

intents:""", file=domain_yaml)
    for intent in ["greet", "goodbye", "bot_challenge"]:
        print("  - %s" % intent, file=domain_yaml)
    for intent in allIntents:
        if len(allIntents[intent]) > 1:
            print("  -", intent, file=domain_yaml)
    print("\nentities:", file=domain_yaml)
    for entity in allEntities:
        [_n, roleSet] = allEntities[entity]
        if len(roleSet) == 0:
            print("  -", entity, file=domain_yaml)
        else:
            print("  - %s:" % entity, file=domain_yaml)
            print("      roles:", file=domain_yaml)
            for role in roleSet:
                print("      - %s" % role, file=domain_yaml)
    print("Wrote", domain_yaml.name)


def create_simple_intents(rasadir):
    simple_intents_yaml = open(os.path.join(rasadir, "data", "simple_intents.yml"), "w", encoding="utf-8")
    print("""version: "3.1"
nlu:
- intent: greet
  examples: |
    - good morning
    - good evening
    - good afternoon

- intent: goodbye
  examples: |
    - bye
    - goodbye
    - have a nice day
    - see you later

- intent: bot_challenge
  examples: |
    - are you a bot?
    - are you a human?
    - am I talking to a bot?
    - am I talking to a human?
""", file=simple_intents_yaml)
    print("Wrote", simple_intents_yaml.name)


if __name__ == '__main__':
    pwd = os.path.dirname(__file__)
    inputFN = os.path.join(pwd, "Examples", "train.json")
    rasa_dir = os.path.join(pwd, "RASA_bot")
    inputF = open(inputFN, "r", encoding="utf-8")
    data = json.load(inputF)
    allIntents = {}
    allEntities = Counter()
    allValues = Counter()
    allRoles = Counter()
    examples = data["rasa_nlu_data"]["common_examples"]
    for example in examples:
        parse_example(example, False, allIntents, allEntities, allRoles, allValues)
    create_intents(allIntents, allEntities, rasa_dir)
    create_simple_intents(rasa_dir)
    create_domain(allIntents, allEntities, rasa_dir)
