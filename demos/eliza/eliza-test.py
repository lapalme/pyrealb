from keywordsFr import elizaInitials, elizaFinals, elizaQuits
from eliza import choose, getTerminals, getKeyword, select, enKeys, getQuestion,showTerminalLists, matchDecomp
from tokenize import tokenizeFr

user_gender = "m"
eliza_gender = "f"
use_majestic = True
trace = False

def ask(fn,groups,infos):
    expr = fn(groups,user_gender).typ({"maje":use_majestic})
    if trace: print(expr.toSource())
    res = "Eliza  : "+expr.realize()
    if trace: res += infos
    print(res)

def runScript(inputs):
    print("Discussion avec Eliza")
    print(f"   genre du patient:{user_gender}, genre d'Eliza:{eliza_gender}, vouvoiement:{use_majestic}")
    ask(choose(elizaInitials),[],": initials")
    for inpt in inputs:
        print("Patient: "+inpt)
        if inpt.lower() in elizaQuits:
            ask(choose(elizaFinals),[],": finals")
            break
        else:
            terminals = [getTerminals(tok) for tok in tokenizeFr(inpt)]
            keyword = getKeyword(terminals)
            if keyword is None:
                ask(select(enKeys["xnone"]["pats"][0]),[],
                    ": xnone:"+enKeys["xnone"]["pats"][0]["idx_reasmb"])
            else:
                (questionFn,groups) = getQuestion(terminals,keyword,use_majestic,trace)
                if questionFn is not None:
                    ask(questionFn,groups,"")
                else:
                    print("****: pas de question trouvée:"+keyword)
    print(""*10)

userInputs = [
    "Je me rappelle le bon vieux temps",
    "Mais j'oublie toujours votre nom",
    "Je rêve de devenir célèbre",
    "J'ai peur des machines",
    "Je suis souvent fatigué",
    "J'estime que vous ne m'aidez pas beaucoup",
    "J'aimerais vous présenter de mon épouse",
    "Pourquoi ne pouvez-vous pas m'aider à progresser",
    "Pourquoi ne pouvez-vous pas m'aider à progresser",
    "Je vous demande pardon",
    "Tous sont semblables",
    "Can we continue in English",
    "But I want to speak in English",
    "Fin"
]

# tests unitaires de toutes les phrases
def testAll(key_en, userText):
    print(f'testAll("{key_en}","{userText}")')
    keyword = enKeys[key_en]
    if keyword is not None:
        key = keyword["key"]
        terminals = [getTerminals(tok) for tok in tokenizeFr(userText)]
        if trace:
            print(f"** key_en: {keyword['key_en']}, lemma:{key[0].lemma if type(key)==list else key.lemma} : {userText}")
            showTerminalLists(terminals)
        for pat in keyword["pats"]:
            groups = matchDecomp(pat["decomp"],terminals,use_majestic)
            if groups is not None:
                if trace: print(print(f"groups:/"+"/".join(t.realize() for g in groups[1:] for t in g)+"/"))
                for fn in pat["reasmb"]:
                    if callable(fn):
                        print(fn(groups,user_gender).typ({"maje": use_majestic}).realize())
                    else:
                        print("===> "+fn)
        print("="*10)
    else:
        print(f"keyword:{key_en} absent")
    print("-"*10)

def run_testAll():
     testAll("xnone","")
     testAll("sorry","excusez-moi")
     testAll("sorry","je vous demande pardon")
     testAll("remember","je me rappelle des choses")
     testAll("remember","vous vous rappelez de vos voyages")
     testAll("remember","ceci vous rappelle des bons souvenirs")
     testAll("forget","J'oublie les anniversaires")
     testAll("forget","Quand avez-vous oublié de venir")
     testAll("if","Ah si j'avais su")
     testAll("dreamed","Je rêve d'être informaticien")
     testAll("dream","J'ai fait un rêve avec des éléphants roses")
     testAll("perhaps","J'irai peut-être au ciel")
     testAll("name","je ne connais pas votre nom")
     testAll("deutsch","Sprechen bitte auf Deutsch")
     testAll("francais","In English please")
     testAll("italiano","In italiano")
     testAll("espanol","Habla espanol")
     testAll("xforeign","Anything")
     testAll("hello","Bonjour")
     testAll("computer","J'ai peur des ordinateurs")
     testAll("am","Pourquoi suis-je perdu ?")
     testAll("am","Pourquoi êtes-vous perdu ?")
     testAll("am","Pourquoi es-tu perdu ?")
     testAll("am","Ils sont jaloux")
     testAll("your","J'aime bien votre attitude")
     testAll("i","Étais-je capable d'y arriver ?")
     testAll("i","Étais-tu capable d'y arriver ?")
     testAll("i","Étiez-vous capable d'y arriver ?")
     testAll("i","Je désire du chocolat")
     testAll("i","Je suis malheureux en affaire")
     testAll("i","Je suis heureux en affaire")
     testAll("i","Je pense que je vais bien")
     testAll("i","je suis à l'affut")
     testAll("i","Je ne peux pas aller à la plage")
     testAll("i","Je ne veux pas manger de la soupe")
     testAll('i',"Je sens des mauvaises vibrations")
     testAll("you","Vous me rappelez de revenir")
     testAll("you","Vous êtes très fort")
     testAll("yes","Très bien")
     testAll("no_one","Personne ne veut venir")
     testAll("no","non")
     testAll("my","j'aime bien mon épouse")
     testAll("can","Pouvez-vous m'aider ?")
     testAll("can","puis-je vous demander des choses")
     testAll("what","Je ne sais plus quoi faire")
     testAll("because","Je vous parle parce que j'ai peur")
     testAll("everyone","J'imagine que tout le monde veut aller au ciel")
     testAll("why","Je ne vois pas pourquoi ne pouvez-vous pas arriver demain")
     testAll("why","Pourquoi ne puis-je pas arriver en retard")
     testAll("always","J'aime toujours cela")
     testAll("alike","Le chien est semblable au chat")
     testAll("like","C'est pareil")
     testAll("different","nous sommes tous différents")

    # test all initial and final sentences
     for fn in elizaInitials+elizaFinals:
        print(fn([],"f").typ({"maje":True}).realize())


if __name__ == "__main__":
    # runScript(userInputs)
    run_testAll()
