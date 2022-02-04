from context import pyrealb
from pyrealb.all import *

### generate sentence variations on sentences in examples.py
###   the list of options is defined by setting values in "checkboxes"

from examples import *
import copy

types={"en":["neg","contr","pas","prog","perf","int","mod"],
       "fr":["neg","pas","prog","int","mod"]};

pos={"int":["yon","wos","was","wod","wad","woi","wai","whe","why","whn","how","muc"],
     "mod":["poss","perm","nece","obli","will"]}

##  generate a list of objects that can be given as argument to .typ()
## checkbox simulation: " " (unchecked), "*" (checked), "-":indeterminate
def genererTyp(types,checked,obj,typ):
    if len(types)==0:
        typ.append(copy.copy(obj))
    else:
        type0=types[0]
        obj[type0]=False
        genererTyp(types[1:], checked, obj,typ)
        if checked[type0]!=" ":
            if type0 in pos:
                if checked[type0]=="-":
                    obj[type0]=pos[type0][0]
                    genererTyp(types[1:],checked,obj,typ)
                else:
                    for p in pos[type0]:
                        obj[type0]=p 
                        genererTyp(types[1:], checked, obj,typ)
            else:
                obj[type0]=True 
                genererTyp(types[1:], checked, obj,typ)

showFlags=True

def generate(examples,types,checkboxes):
    for ex in examples:
        typs=[]
        genererTyp(types,checkboxes,{},typs)
        for typ in typs:
            # we must "clone" the expression which eval(s.toSource()) before applying the modifications
            # otherwise modifications are applied to the original expression 
            exp=f'{ex["expr"].strip()}.typ({repr(typ)})'
            # print(exp)
            if showFlags:
                flags=",".join(key+":"+str(val) for key,val in typ.items() if val!=False)
                print("%-40s:: %s"%(flags,eval(exp).realize()))
            else:
                print(str(eval(exp)))
        if showFlags:print("=== %d ==="%len(typs))
            
loadFr()
generate(examplesFr,types["fr"],
         ## checkbox simulation: " " (unchecked), "*" (checked), "-":indeterminate
         {"neg":" ","pas":"*","prog":" ","int":"-","mod":"*"})

loadEn()
addToLexicon({"John":{"N":{"g":"m","tab":"n4"}}})
addToLexicon({"Jim": {"N":{"g":"m","tab":"n4"}}})
addToLexicon({"Bill":{"N":{"g":"m","tab":"n4"}}})
addToLexicon({"Mary":{"N":{"g":"f","tab":"n4"}}})

generate(examplesEn,types["en"],
         ## checkbox simulation: " " (unchecked), "*" (checked), "-":indeterminate
         {"neg":"*","contr":" ","pas":"*","prog":"*","perf":"*","int":"-","mod":"-"})
