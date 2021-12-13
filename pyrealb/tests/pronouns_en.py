from context import pyrealb
from pyrealb import *
from tests.test import test


def pronouns_en():
    # table of pronouns as given by François Lareau

    options=["","refl","nom","acc","dat","gen"]
    
    tonics = {
      "me":  ["me","myself","I","me","me","mine"],
      "you": ["you","yourself","you","you","you","yours"],
      "him": ["him","himself","he","him","him","his"],
      "her": ["her","herself","she","her","her","hers"],
      "it":  ["it","itself","it","it","it","its"],
      "us":  ["us","ourselves","we","us","us","ours"],
      "them":["them","themselves","they","them","them","theirs"],
    }
    
    possDets ={
        "my":lambda:D("my").pe(1).ow("s"),
        "your":lambda:D("my").pe(2).ow("s"),
        "his":lambda:D("my").pe(3).ow("s").g("m"),
        "her":lambda:D("my").pe(3).ow("s").g("m").g("f"),
        "its":lambda:D("my").pe(3).ow("s").g("m").g("f").g("n"),
        "our":lambda:D("my").pe(1).ow("p"),
        "your":lambda:D("my").pe(2).ow("p"),
        "their":lambda:D("my").pe(3).ow("p"),
    }
    
    ## build list of tests
    tests=[]
    loadEn()
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
    
    for poss,exp in possDets.items():
        tests.append({
            "expression":exp(),
            "expected":poss,
            "message":f"{exp().toSource()}=>{poss}"
        })
    return tests

if __name__ == '__main__':
    test("English pronouns","en",pronouns_en,badOnly=True)