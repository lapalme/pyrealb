from pyrealb import *
import random

from lemmatize import lemmataFr, tokenizeFr
from keywordsFr import keywordsFr, elizaFinals, elizaQuits, elizaInitials

Constituent.debug = True
# trier les mots-clés en ordre descendant de "rank"
keywordsFr.sort(key=lambda kw:kw["rank"],reverse=True)

#  Créer une table des mots-clés en anglais
#  utilisé dans testAll et "goto keyword")
enKeys = {}
for kw in keywordsFr:
    enKeys[kw["key_en"]] = kw
    for pat in kw["pats"]:
        # nouvel attribut pour garder trace de la dernière alternative générée
        pat["idx_reasmb"] = len(pat["reasmb"])-1

# Trouver les terminaux qui peuvent réaliser "word" et les trier par leur fréquence de POS (heuristique)
def getTerminals(word):
    terminalOrder = {"D": 0, "N": 1, "V": 2, "A": 3, "Pro": 4, "Adv": 5, "P": 6, "C": 7, "DT": 8, "NO": 9, "Q": 10}
    if word in lemmataFr:
        terms = lemmataFr[word]
        terms.sort(key=lambda t:t.constType)
        return terms
    return [Q(word)]

# afficher des listes de terminaux (pour la mise au point)
def showTerminalLists(terminalLists):
    for tl in terminalLists:
        print(tl[0].realize()+" : "+", ".join(e.toSource() for e in tl))
    print("---")

# vérifier si "term1" correspond à "term2" (i.e. même constType et même lemme))
# si props==true, on vérifie aussi les propriétés "pe","g","n","t"
# si la valeur de la propriété de term1 est "x", on accepte toutes les valeurs
# si term1 ou term2 sont des listes, il suffit qu'un des éléments de la liste match
def mememot(term1,term2,props):
    if type(term1) == list:
        for term in term1:
            if mememot(term,term2,props) is not None:
                return term2
        return None
    if type(term2) == list:
        for term in term2:
            if mememot(term1,term,props) is not None:
                return term
        return None
    if term1.constType == term2.constType and term1.lemma == term2.lemma:
        for prop in ["pe","g","n","t"]:
            p = term1.getProp(prop)
            if p is not None and p != "x":
                if p != term2.getProp(prop): return None
        return term2
    return None

# changer les premières personnes en deuxième (et vice-versa) dans une liste de terminaux
# S'il y a des changements alors on recrée de nouveaux terminaux avec "clone"
def changePerson(group,use_majestic):
    res = []
    for termList in group:
        term = termList[0]
        if term.isA("Pro","D","V"):
            pe = term.getProp("pe")
            if pe == 1:
                term = term.clone().pe(2)
            elif pe == 2:
                term = term.clone().pe(1).n("s")
            if term.lemma == "mon" and use_majestic:
                term = term.close().setLemma("notre").maje(False)
        res.append(term)
    return res

# simili regex pour matcher une expression de décomposition avec des * et une liste de terminaux
# Si use_majestic est true,  on change les personnes dans les terminaux des groupes
def matchDecomp(decomps,terminals,use_majestic):
    groups=[[Q("dummy")]] # inutilisé, mais permet d'indexer à partir de 1
    last = len(decomps)-1
    iTerm = 0
    for iDecomp in range(0,len(decomps)):
        if mememot(decomps[iDecomp],Q("*"),False) is not None: # deal with *
            if iDecomp == last:
                # faire un groupe avec le premier terminal de tout le reste
                groups.append(changePerson(terminals[iTerm:],use_majestic))
            else:
                group = []
                nextWord = decomps[iDecomp+1]
                while mememot(nextWord,terminals[iTerm],True) is None:
                    # sauter ce  terminal jsuqu'au prochain mot de décomp
                    group.append(terminals[iTerm])
                    iTerm+=1
                    if (iTerm >= len(terminals)): break
                groups.append(changePerson(group,use_majestic))
        elif iTerm >= len(terminals): # decomp trop long pour terminals
            return None
        elif mememot(decomps[iDecomp],terminals[iTerm],True) is not None:
            # mot de decomp correspond au terminal
            iTerm += 1
        else: # mot de decomp ne correspond pas au terminal
            return None
    return groups

# choisir un element au hasard dans une liste
def choose(liste):
    return random.choice(liste)

# etourner la prochaine alternative dans une liste de pattern
def select(pat):
    idx = (pat["idx_reasmb"]+1)%len(pat["reasmb"]) # trouver le prochain index
    pat["idx_reasmb"] = idx   # mettre à jour l'index
    return pat["reasmb"][idx]

# trouver le mot clé dont la clé match un des terminaux
def getKeyword(terminals):
    return next((keyword for keyword in keywordsFr
                if any(t for t in terminals if mememot(keyword["key"],t,False) is not None)),
                None)

# retourner la fonction question qui matche un pattern dans un mot-clé avec les groupes
# traite aussi le cas du "goto" en se rappelant récursivement
def getQuestion(terminals, keyword,use_majestic,trace):
    for pat in keyword["pats"]:
        groups = matchDecomp(pat["decomp"],terminals,use_majestic)
        if groups is not None:
            if trace: print(f"groups:/"+"/".join(t.realize() for g in groups[1:] for t in g)+"/")
            questionFN = select(pat)
            if not callable(questionFN): # traiter le goto
                if trace: print("=>",questionFN)
                return getQuestion(terminals,enKeys[questionFN[5:]],use_majestic, trace)
            return (questionFN,groups)
    return (None,None)


if __name__ == "__main__":
    enonce = "C'est mon ami qui m'a suggéré de venir vous voir"
    tokens = tokenizeFr(enonce)
    allTerms = [getTerminals(tok) for tok in tokens]
    showTerminalLists(allTerms)