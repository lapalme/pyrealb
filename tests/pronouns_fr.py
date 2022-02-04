from context import pyrealb
from pyrealb.all import *
from test import test


def pronouns_fr():
    # table of pronouns as given by François Lareau

    options=["","refl","nom","acc","dat","refl"]
    
    tonics = {
       "moi":  ["moi","moi-même","je","me","me","me"],
       "toi":  ["toi","toi-même","tu","te","te","te"],
       "lui":  ["lui","lui-même","il","le","lui","se"],
       "elle": ["elle","elle-même","elle","la","lui","se"],
       "on":   ["soi","soi-même","on","le","soi","se"],
       "nous": ["nous","nous-mêmes","nous","nous","nous","nous"],
       "vous": ["vous","vous-mêmes","vous","vous","vous","vous"],
       "eux":  ["eux","eux-mêmes","ils","les","leur","se"],
       "elles":["elles","elles-mêmes","elles","les","leur","se"],
    }
    
    possPros = {
       "mien":lambda:Pro("mien").pe(1),
       "miens":lambda:Pro("mien").n("p").pe(1),
       "mienne":lambda:Pro("mien").g("f").pe(1),
       "miennes":lambda:Pro("mien").n("p").g("f").pe(1),
       "tien":lambda:Pro("tien"),
       "tiens":lambda:Pro("tien").n("p"),
       "tienne":lambda:Pro("tien").g("f"),
       "tiennes":lambda:Pro("tien").n("p").g("f"),
       "sien":lambda:Pro("sien"),
       "siens":lambda:Pro("sien").n("p"),
       "sienne":lambda:Pro("sien").g("f"),
       "siennes":lambda:Pro("sien").n("p").g("f"),
       "nôtre":lambda:Pro("nôtre").pe(1),
       "nôtres":lambda:Pro("nôtre").n("p").pe(1),
       "nôtre":lambda:Pro("nôtre").g("f").pe(1),
       "nôtres":lambda:Pro("nôtre").n("p").g("f").pe(1),
       "vôtre":lambda:Pro("vôtre"),
       "vôtres":lambda:Pro("vôtre").n("p"),
       "vôtre":lambda:Pro("vôtre").g("f"),
       "vôtres":lambda:Pro("vôtre").n("p").g("f"),
       "leur":lambda:Pro("leur"),
       "leurs":lambda:Pro("leur").n("p"),
       "leur":lambda:Pro("leur").g("f"),
       "leurs":lambda:Pro("leur").n("p").g("f"),
    }
    
    possDets = {
        "mon":lambda:D("mon").pe(1),
        "mon":lambda:D("mon").pe(1).n("s").g("m"),
        "ma":lambda:D("mon").pe(1).n("s").g("f"),
        "mes":lambda:D("mon").pe(1).n("p").g("m"),
        "mes":lambda:D("mon").pe(1).n("p").g("f"),
        "ton":lambda:D("mon").pe(2),
        "ton":lambda:D("ton").n("s").g("m"),
        "ta":lambda:D("ton").n("s").g("f"),
        "tes":lambda:D("ton").n("p").g("m"),
        "tes":lambda:D("ton").n("p").g("f"),
        "son":lambda:D("mon").pe(3),
        "son":lambda:D("son").n("s").g("m"),
        "sa":lambda:D("son").n("s").g("f"),
        "ses":lambda:D("son").n("p").g("m"),
        "ses":lambda:D("son").n("p").g("f"),
        "notre":lambda:D("notre").pe(1),
        "notre":lambda:D("notre").pe(1).n("s").g("m"),
        "notre":lambda:D("notre").pe(1).n("s").g("f"),
        "nos":lambda:D("notre").pe(1).n("p").g("m"),
        "nos":lambda:D("notre").pe(1).n("p").g("f"),
        "votre":lambda:D("notre").pe(2),
        "votre":lambda:D("votre").n("s").g("m"),
        "votre":lambda:D("votre").n("s").g("f"),
        "vos":lambda:D("votre").n("p").g("m"),
        "vos":lambda:D("votre").n("p").g("f"),
        "leur":lambda:D("notre").pe(3),
        "leur":lambda:D("leur").n("s").g("m"),
        "leur":lambda:D("leur").n("s").g("f"),
        "leurs":lambda:D("leur").n("p").g("m"),
        "leurs":lambda:D("leur").n("p").g("f"),
    }

    ## build list of tests
    tests=[]
    loadFr()
    for pro,results in tonics.items():
        for i,param in enumerate(options):
            exp=Pro(pro)
            if i<2:exp.tn(param)
            else: exp.c(param)
            if pro=="me":exp.pe(1)
            tests.append({
                "expression":exp,
                "expected":results[i],
                "message":f"{exp.toSource()}=>{pro}"
                })
    
    for poss,exp in list(possDets.items())+list(possPros.items()):
        tests.append({
            "expression":exp(),
            "expected":poss,
            "message":f"{exp().toSource()}=>{poss}"
        })
    return tests

if __name__ == '__main__':
    test("Pronoms français","fr",pronouns_fr)