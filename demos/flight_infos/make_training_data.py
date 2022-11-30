import json, os
from collections import Counter
from RASA_bot.response.parse_examples import parse_example

q="'"
qq="''"

def create_nlu(allIntents,allEntities,rasadir):
    for intent in allIntents:
        if len(allIntents[intent])>1:  # RASA needs at least 2 examples of each intent...
            nlu_yaml=open(f"{rasadir}/data/intent-{intent}.yml", "w", encoding="utf-8")
            print('version: "3.1"\nnlu:', file=nlu_yaml)
            print(f"- intent: {intent}", file=nlu_yaml)
            print( "  examples: |", file=nlu_yaml)
            for text,entitySet in allIntents[intent]:
                keep=True
                for e in entitySet:
                    if allEntities[e][0]<2:# RASA needs at least 2 examples of each entity...
                        print('Hapax %s:%s'%(e,text))
                        keep=False
                if keep:
                    print(f"    - '{text.replace(q,qq)}'", file=nlu_yaml)
            print("Wrote", nlu_yaml.name)

def create_domain(allIntents,allEntities,rasadir):
    domain_yaml=open(f"{rasadir}/domain.yml", "w", encoding="utf-8")
    print("""version: "3.1"

session_config:
  session_expiration_time: 60
  carry_over_slots_to_new_session: true

intents:""",file=domain_yaml)
    print("  - greet",file=domain_yaml)
    for intent in allIntents:
        if len(allIntents[intent]) > 1:
            print("  -",intent,file=domain_yaml)
    print("\nentities:",file=domain_yaml)
    for entity in allEntities:
        [_n,roleSet]=allEntities[entity]
        if len(roleSet)==0:
            print("  -",entity,file=domain_yaml)
        else:
            print("  - %s:"%entity,file=domain_yaml)
            print("      roles:",file=domain_yaml)
            for role in roleSet:
                print("      - %s"%role,file=domain_yaml)
    print("""
actions:
  - give_flight_info""",file=domain_yaml)
    print("Wrote", domain_yaml.name)

def create_responses(rasadir):
    responses_yaml = open(f"{rasadir}/data/responses.yml", "w", encoding="utf-8")
    print("""version: "3.1"
responses:
  utter_greet:
  - text: |
      Hello! what information about flights do you want ?
  - text: |
      Hi! Any flight info ?
""",file=responses_yaml)
    print("Wrote", responses_yaml.name)

def create_stories(rasadir):
    stories_yaml = open(f"{rasadir}/data/stories.yml", "w", encoding="utf-8")
    print("""version: "3.1"    
stories:
  - story: greet and show intent
    steps:
    - intent: greet
    - action: utter_greet
    - intent: flight
    - action: give_flight_info
""",file=stories_yaml)
    print("Wrote",stories_yaml.name)


if __name__ == '__main__':
    pwd = os.path.dirname(__file__)
    inputFN = os.path.join(pwd,"Examples","train.json")
    rasadir = os.path.join(pwd,"RASA_training")
    inputF = open(inputFN, "r", encoding="utf-8")
    data = json.load(inputF)
    allIntents = {}
    allEntities = Counter()
    allValues = Counter()
    allRoles = Counter()
    examples=data["rasa_nlu_data"]["common_examples"]
    for example in examples:
        parse_example(example,False,allIntents,allEntities,allRoles,allValues)
    create_nlu(allIntents,allEntities,rasadir)
    create_domain(allIntents,allEntities,rasadir)
    create_responses(rasadir)
    create_stories(rasadir)
