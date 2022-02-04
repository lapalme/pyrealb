from context import pyrealb
from pyrealb.all import *

# Adaptation en python de l'adaptation en JavaScript
#     http://rali.iro.umontreal.ca/JSrealB/current/demos/Evenements/index.html
# de l'exemple présenté par Nicolas Daoust dans son mémoire de maîtrise
#      http:#daou.st/JSreal/#/Demonstration
#  les données sont maintenant en "vrai" JSON avec des identificateurs plus évocateurs
#  Elles ne sont plus triées pour faire ressortir l'aspect Data2Text

#  On utilise "markup.py" pour créer le HTML

import datetime
import markup
from markup import oneliner as e

from collections import Counter

page = markup.page( )
page.init( title="Événements en pyRealB")
page.h1(e.em("Data to Text")+": Description d'événements")
page.p(e.em("Adaptation du "+
            e.a("programme de démonstration de jsReal",href="http://daou.st/JSreal/#/Demonstration",target="_new")+
            " créé par Nicolas Daoust pour "+
            e.a("son mémoire de maîtrise",href="http://rali.iro.umontreal.ca/rali/?q=fr/node/1341", 
                                          title="JSreal: un réalisateur de texte pour la programmation web | RALI")))
page.p("Les événements (en format JSON) sont d'abord triés en ordre chronologique et regroupés par ville avant d'être décrits.")

loadFr();

## ajouts au lexique
addToLexicon({"Alice":{ "N": { "g": "f", "pe": 3, "tab": "nI" } }});
addToLexicon({"Robert":{ "N": { "g": "m", "pe": 3, "tab": "nI" } }});
addToLexicon({"Nicolas":{ "N": { "g": "m", "pe": 3, "tab": "nI" } }});

## Définit les informations comme des chaines pour pouvoir les afficher dans la page avant l'évaluation
# événements à présenter
evListS = """[{ "date":"2013-09-25","time":"19:00:00", "ville":"Laval",
   "cat":"atelier", "attr":"nouveau", "tit":"Exercices de réalisation", "part":"al", "res":"al" } ,
 { "date":"2013-10-02","time":"19:00:00", "ville":"Longueuil",
   "cat":"conf", "attr":"nouveau", "tit":"Pourquoi la réalisation?", "part":"nico", "res":"nico" } ,
 { "date":"2013-09-30","time":"13:00:00", "ville":"Granby",
   "cat":"atelier", "attr":"classique", "tit":"Principes de réalisation", "part":"al" } ,
 { "date":"2013-09-27", "ville":"Montréal",
   "cat":"consult", "attr":"d'une demi-heure", "part":"bob", "res":"bob" } ,
 { "date":"2013-09-30", "ville":"Granby", "adr":"au 901 rue Principale",
   "cat":"consult", "attr":"privé", "part":"bob", "res":"bob" } ,
 { "date":"2013-10-02","time":"13:00:00", "ville":"Granby",
   "cat":"atelier", "attr":"nouveau", "tit":"Exercices de réalisation", "part":"bob" } ,
 { "date":"2013-10-03","time":"13:00:00", "ville":"Longueuil",
   "cat":"atelier", "tit":"Planification et réalisation", "part":"nico" }]"""
evList=eval(evListS)

# catégories d'événements
catWordString="""{"consult": N("consultation"),
 "atelier": N("atelier"),
 "conf":    N("conférence"),
 "sejour":  N("séjour")}""";
catWord = eval(catWordString); 

# participants
partInfoString="""{"al":   {"name": N("Alice"),   "tel": 5552543, "email": False },
 "bob":  {"name": N("Robert"),  "tel": False,   "email": "rob@JSreal.js" },
 "nico": {"name": N("Nicolas"), "tel": 5556426, "email": "nic@JSreal.js" }}""";
partInfo = eval(partInfoString); 

# créer une date pour un événement
#  d'abord le "datetime"
def make_datetime(e):
    d=e["date"]
    if "time" in e:
        t=e["time"]
        return datetime.datetime(int(d[0:4]),int(d[5:7]),int(d[8:10]),
                        hour=int(t[0:2]),minute=int(t[3:5]),second=int(t[6:8]))
    return datetime.datetime(int(d[0:4]),int(d[5:7]),int(d[8:10]))

#  la version pyRealB
def makeDT(e,showTime=True):
    dateTime=make_datetime(e)
    dt=DT(dateTime)
    if "time" not in e or not showTime:
        dt.dOpt({"hour":False,"minute":False,"second":False})
    else:
        if dateTime.second==0:dt.dOpt({"second":False})
        if dateTime.minute==0:dt.dOpt({"minute":False})
    return dt

# formater un numéro de téléphone (sans réalisation...)
def fmtTel(n):
    s=str(n)
    if len(s)==10 : 
        return f"({s[0:3]}) {s[3:6]-s[6:10]}"
    elif len(s)==7: 
        return f"(514) {s[0:3]}-{s[3:7]}"
    else: 
        return s

def fmtEmail(s):
    return S(s).tag("a",{"href":"mailto:"+s})

def showMotif(ev):
    np=NP(D("un"),catWord[ev["cat"]])
    if "attr" in ev:
        attr=ev["attr"]
        lemma=getLemma(attr)
        if lemma!=None and "A" in lemma:
            np.add(A(attr))
        else:
            np.add(Q(attr))          
    return np

# afficher les informations de contact
def showContact(ev,pronominalize):
    part=partInfo[ev["part"]]
    nomParticipant=NP(part["name"])
    contactez=V("contacter").t("ip").pe(2).n("p")
    if pronominalize:
        nomParticipant.pro()
        contactez.lier()
    return S(PP(P("pour"),V("réserver").t("b")).a(","),
             S(VP(contactez,nomParticipant)).a(":"),part["contact"])

# créer une liste de listes d'événements regroupant tous les événements d'une même ville
def evenementsParVille(inL,outL):
    if len(inL)==0:return outL
    if inL[0]["ville"]==outL[-1][0]["ville"]:
        outL[-1].append(inL[0])
    else:
        outL.append([inL[0]])
    return evenementsParVille(inL[1:], outL)

def showGroupe(evs):
    if len(evs)==1: # un seul événement, verbaliseer directement
        ev=evs[0]
        page.h4(str(S(catWord[ev["cat"]],P("à"),ev["ville"])))
        quand=makeDT(ev).a(",")
        participant=partInfo[ev["part"]]["name"]
        place=S(P("à"),ev["ville"])
        if "adr" in ev:place.add(ev["adr"],0)
        s=S(quand,participant,
            V("être").t("f"),place,
            PP(P("pour"),showMotif(ev)))
        if "tit" in ev:
            s.add(S(ev["tit"]).tag("i"))
        page.p(str(s)+e.br()+str(showContact(ev,True)))
    else: # plusieurs événements dans la même ville
        ev=evs[0]
        page.h4(str(S(N("séjour"),P("à"),ev["ville"])))
        quand=PP(P("de"),makeDT(evs[0],False),
                 P("à"),makeDT(evs[-1],False)).a(",")
        ps=set([partInfo[ev["part"]]["name"] for ev in evs]) # récupérer les noms des participants
        cats=Counter()                     # récupérer les catégories
        for ev in evs:cats[ev["cat"]]+=1
        # réaliser les participants
        participants=CP(C("et"),*ps)
        place=S(P("à"),ev["ville"])
        if "adr" in ev:place.add(ev["adr"],0)
        # réaliser les catégories d'activités
        cs=CP(C("et"),*[NP(NO(nb).nat(True),catWord[c]) for c,nb in cats.items()])
        s=S(quand,participants,VP(V("être").t("f"),place,PP(P("pour"),cs)))
        page.p(str(s))
        # formatter les événements dans une liste à puce
        page.ul.open()
        for ev in evs:
            s=S(makeDT(ev).dOpt({"det":False,"day":False,"year":False}).a(":"),
                showMotif(ev))
            if "tit" in ev:
                s.add(S(ev["tit"]).tag("i"))
            if len(ps)>1: #préciser le participant s'il y en a plus d'un dans la période
                s.add(PP(P("avec"),partInfo[ev["part"]]["name"]))    
            page.li(str(s))
        page.ul.close()
        page.p(str(showContact(evs[0],len(ps)==1)))
        
page.h2("Données d'entrée")        
page.h3("Événements")
page.pre(evListS)
page.h3("Catégories d'événements")
page.pre(catWordString)
page.h3("Participants")
page.pre(partInfoString)

page.h2("Texte réalisé")
# trier les événements selon les dates
evList.sort(key=make_datetime)

# ajouter l'information de contact pour chaque participant
for p,info in partInfo.items():
    contact=CP(C("ou"))
    if "tel" in info and info["tel"]:
        contact.add(S(fmtTel(info["tel"])))
    if "email" in info and info["email"]:
        contact.add(S(fmtEmail(info["email"])))
    info["contact"]=contact

# générer le texte correspondant à chaque événement
for groupe in evenementsParVille(evList[1:], [[evList[0]]]):
    showGroupe(groupe)
# afficher la page    
print(page)


if __name__ == '__main__':
    pass