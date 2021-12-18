## Python version of jsRealB
##   the organization parallels the one of JavaScript version (version 3.9)
##   in fact, the JavaScript version was sometimes revised in order to make it
##   similar
## Guy Lapalme, December 2021

from Constituent import Constituent
from Terminal import  Terminal,N,A,Pro,D,Adv,V,P,C,DT,NO,Q
from Phrase import Phrase, NP,AP,VP,AdvP,PP,CP,S,SP
from Lexicon import loadEn,loadFr,currentLanguage,addToLexicon,updateLexicon,getLemma,getLexicon,getRules

import random,sys,datetime

## select a random element in a list useful to have some variety in the generated text
#  if the first argument is a list, selection is done within the list
#  otherwise the selection is among the arguments 
#   (if the selected element is a function, evaluate it with no parameter)
def oneOf(*elems):
    if len(elems)==1:
        if isinstance(elems[0],list):
            e=random.choice(elems[0])
        else:
            e=elems[0]
    else:
        e=random.choice(elems)
    return e() if callable(e) else e

# Flag for quoting out of vocabulary tokens (not yet taken into account)
# quoteOOV=False;
# def setQuoteOOV(qOOV):
#     global quoteOOV
#     quoteOOV=qOOV

# create expression from a JSON structure
def fromJSON(json,lang=None):
    if isinstance(json,dict):
        if "lang" in json:
            if json["lang"]=="en": lang="en"
            elif json["lang"]=="fr":lang="fr";
            else: 
                print("FromJSON: lang should be 'en' or 'fr', not "+json["lang"]+" 'en' will be used",file=sys.stderr);
                lang="en";
        lang1 = lang if lang!=None else currentLanguage()
        if "phrase" in json:
            constType=json["phrase"];
            if constType in ['NP', 'AP', 'AdvP', 'VP', 'PP', 'CP', 'S', 'SP']:
                return Phrase.fromJSON(constType,json,lang1)
            else:
                print("fromJSON: unknown Phrase type:"+constType,file=sys.stderr)
        elif "terminal" in json:
            constType=json["terminal"];
            if constType in ['N', 'A', 'Pro', 'D', 'Adv', 'V', 'P', 'C', 'DT', 'NO', 'Q']:
                return Terminal.fromJSON(constType,json,lang1)
            else:
                print("fromJSON: unknown Terminal type:"+constType,file=sys.stderr)
    else:
        print("fromJSON: object expected, but found "+type(json).__name__+":"+repr(json),file=sys.stderr)

# useful variables for using expressions written originally for the javascript version
false = False
true  = True 
null  = None 

# version and date informations
pyRealB_version="1.0"
pyRealB_dateCreated=datetime.datetime.today()

if __name__ == '__main__':
    def english():
        # a few examples geneerates warnings shown here as comments
        loadEn()
        print(V("reserve").t("")) # V('reserve'):: : this bad value for option t is ignored.
        print(N()) # N(None):: the parameter should be string, not NoneType.
        print(DT())
        print(DT(datetime.datetime.today()).dOpt({'rtime':True}))
        print(DT(None).dOpt({"det":False}))
        s=lambda:S(Pro("I").pe(1),
                 VP(V("say").t("ps"),
                    NP(N("hello"),
                       PP(P("to"),NP(D("the"),N("world").n("p")))))).typ({"pas":False,"neg":True})
        print(S(NP(D("a"),N("cat").n("p"))))
        print(s())
        sJson=s().toJSON()
        import json
        json.dump(sJson,sys.stdout,indent=3)
        print()
        s1=fromJSON(s().toJSON())
        print(s1)

    def francais():
        loadFr()
        print(S(NP(D("le"),N("chat")).n("p"),VP(V("asseoir"))).typ({"refl":True}).realize())
        addToLexicon({"John":{"N":{"g":"m","tab":"n35"}}})
        addToLexicon({"Mary":{"N":{"g":"f","tab":"n36"}}})

        print(S(NP(D("le"),N("chat")),
                VP(V("manger"),
                   NP(D("le"),N("souris")))).typ({'int': 'yon', 'neg': true}).realize()
        )
        print(S(Pro("lui").c('nom').pe(3).g('m').n('s'),
                VP(V("donner").t('pc'), NP(D("un"), N("pomme")).pro(),
                   PP(P("à"), NP(D("le"), N("fille"))).pro())
                ).typ({'neg': False, 'pas': True}).realize())
        print(VP(V("aller").t("pc").pe(2).n("p")).typ(1))
        print(S(Pro("moi").c("nom").pe(3).n("p"), VP(Pro("eux").c('refl'), V("évanouir").t('pc'))).typ({"neg":True}))
        print(S(CP(C("et"), NP(N("John")), NP(N("Mary"))), VP(V("évanouir").t('pc'))).typ({"neg":True,"refl":True}))
        print(S(Pro("je").pe(1).n('p'),
                VP(V("agir").t('p'),
                   AdvP(Adv("conformément"),
                   PP(P("à"),NP(D("le"),N("loi"))))).typ({'neg': True})))
        print(S(Pro("lui").c("nom"),
                  VP(V("parler").t("pc"),
                     PP(P("à"),NP(D("mon"),N("ami"))).pro(),
                     PP(P("de"),NP(D("mon"),N("problème"))).pro())))
        print(S(NP(D("un"),N("garçon").g("f")),
                VP(V("travailler"),
                   PP(P("sur"),N("internet")))).typ({"neg":True}))
        # print(V("cliquer").t("pc").pe(1))
        print(V("repentir").t('p').pe(2).n('s').lier())
        print(V("repentir").t('ip').pe(2).n('s').lier())
        # print(PP(P("sur"),N("internet")))
        print(S(NP(D("un"),N("garçon").g("f")), #erreur de morphologie : genre différent de celui du lexique N('garçon') :{'g': 'f', 'lexique': 'm'}.
                VP(V("travailler"),
                   PP(P("sur"),N("internet")))))
        print(S(NP(D("le"),N("élève").g('f')),
                VP(Pro("moi").pe(1).c('dat'),V("dire"),
                   PP(P("de"),VP(V("interroger").t('b'),
                                 NP(D("le"),N("élève").g('f')).pro(None))
                                 .typ({'neg': True})))).realize())
        print(VP(V("aimer").t("ip").pe(2).n("s")).typ({"refl":True}).realize())
        print(S(Pro("je").pe(2),VP(V("enfuir"))).realize())
        print(S(Pro("je").pe(2).n("p"),VP(V("laver").t("pc"))).typ({"refl":True}).realize())
        print(S(Pro("je").pe(2),VP(V("savoir"))).typ({"pas":True}).realize())
        print(S(NP(D("le"),N("chat")),VP(V("manger"))).typ({"pas":True}))
        print(oneOf([lambda:N("amour"),lambda:N("amitié")]))
        print(oneOf([lambda:N("amour"),lambda:N("amitié")]))
        print(oneOf(lambda:N("amitié")))
        print(oneOf(lambda:N("amour"),lambda:N("amitié")))
        print(NO(4).nat())
        print(NO(4).dOpt({"nat":True}))
        print(D("un","B")) # D('un'):: langage devrait être  "en" ou  "fr" , ce sera fr.
        c=lambda:NP(D("un"),N("chat"))
        print(c())

        s=CP(C("et"),NP(NO("1").nat(True),N("consultation")),NP(NO("2").nat(True),N("atelier")))
        print(s.toSource())
        print(s)
        print(DT(None))
        print(DT("").dOpt({"det":False}))
        print(S(NP(D("le"),
             N("rat").n("p"),
             SP(Pro("que"),
                NP(D("le"),
                   N("chat").g("f").n('p')),
                VP(V("manger").t('pc')))),
          VP(V("être").t('p'),
             AP(A("gris")))))
    
    english()
    francais()