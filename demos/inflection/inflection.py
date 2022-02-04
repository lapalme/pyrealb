from context import pyrealb
from pyrealb.all import *
    
## conjugation and declension

## print a table of values so that the lines are aligned
## it takes for granted that all lines are of the same length
## if transforms all values using str()

def width(val):
    if isinstance(val,str):
        return len(val)
    return len(str(val))

# the first nbHeadLines are centered and followed by a line
def printTable(table,nbHeadlines=0,nbColhead=0):
    if not len(table):return
    widths=[width(table[0][j]) for j in range(0,len(table[0])) ]
    for i in range(0,len(table)):
        for j in range(0,len(table[i])):
            w=width(table[i][j])
            if w>widths[j]:widths[j]=w
    if nbHeadlines>0:
        hdfmt=" | ".join(f"{{:^{w}s}}" for w in widths)
        for i in range(0,nbHeadlines):
            print(hdfmt.format(*map(str,table[i])))
        print("-"*(sum(widths)+3*(len(widths)-1)))
    ## create format string
    fmt=" | ".join(f"{{:{w}s}}" for w in widths)
    ## print the table
    for i in range(nbHeadlines,len(table)):
        print(fmt.format(*map(str,table[i]))) 
    print()   
 
def declinerNom(mot,lang):
    table=[]
    if lang=="fr":
        table.append(["","Singulier","Pluriel"])
        g=getLemma(mot)["N"]["g"]
        if g in "mx":
            table.append(["Masculin",
                          N(mot).g("m").n("s").realize(),
                          N(mot).g("m").n("p").realize()])
        if g in "fx":
            table.append(["Féminin",
                          N(mot).g("f").n("s").realize(),
                          N(mot).g("f").n("p").realize()])
    else:
        table.append(["Singular","Plural"])
        table.append([N(mot).n("s").realize(),N(mot).n("p").realize()])
    return table

def declinerAdjectif(mot,lang):
    table=[]
    if lang=="fr":
        table.append(["","Singulier","Pluriel"])
        table.append(["Masculin",
                      A(mot).g("m").n("s").realize(),
                      A(mot).g("m").n("p").realize()])
        table.append(["Féminin",
                      A(mot).g("f").n("s").realize(),
                      A(mot).g("f").n("p").realize()])
    else:
        table.append(["Comparative","Superlative"])
        table.append([A(mot).f("co").realize(),A(mot).f("su").realize()])
    return table
        
def decliner(mot,lang):
    if lang=="fr":loadFr(); 
    else: loadEn()
    entry=getLemma(mot)
    if entry==None:
        if lang=="fr":
            print("%s : absent du lexique français"%mot)
        else:
            print("%s : not found in English lexicon"%mot)
        return
    if "N" in entry:
        print("***",mot, "comme nom" if lang=="fr" else "as noun")
        printTable(declinerNom(mot,lang))
    if "A" in entry:
        print("***",mot, "comme adjectif" if lang=="fr" else "as adjective")
        printTable(declinerAdjectif(mot,lang))
        

def conjuguer(verbe,lang,typs):
    
    def realize(t,pe,n):
        if t=="ip":
            if (n=="s" and pe in [1,3]) or (n=="p" and pe==3):
                return ""
            else:
                return VP(V(verbe).t(t).pe(pe).n(n)).typ(typs).realize()
        else:
            sp=SP(Pro("je" if lang=="fr" else "I").pe(pe).n(n),VP(V(verbe).t(t))).typ(typs)
            if t.startswith("s"): # subjonctif
                sp=SP(Q("que"),sp)
            return sp.realize()
    
    if lang=="fr":
        loadFr()
        temps= [
            [["Présent","p"],["Imparfait","i"],["Futur simple","f"],["Passé simple","ps"]],
            [["Passé composé","pc"],["Plus-que-parfait","pq"],["Futur antérieur","fa"]],
            [["Subjonctif présent","s"],["Subjonctif imparfait","si"],["Subjonctif passé","spa"],
             ["Subjonctif plus-que-parfait","spq"]],
            [["Conditionnel présent","c"],["Conditionnel passé","cp"],["Impératif","ip"]],
            [["Participe présent","pr"],["Participe passé","pp"],["Infinitif","b"]]
        ]
    else:
        loadEn()
        temps= [
            [["Present","p"]],
            [["Simple past","ps"]],
            [["Future","f"]],
        ]
    
    print("***",verbe,"comme verbe" if lang=="fr" else "as verb",str(typs))
    print()   
    for tmp in temps:
        table=[[t[0] for t in tmp]]
        if tmp[0][0].startswith("Participe"):
            table.append([VP(V(verbe).t(t[1])).typ(typs).realize() for t in tmp])
        else:
            for n in "sp":
                for pe in range(1,4):
                    table.append([realize(t[1],pe,n) for t in tmp])
        printTable(table,1)
    print("===")
        

if __name__ == '__main__':
    conjuguer("aimer","fr",{"neg":False,"prog":True,"pas":True,"refl":True})
    conjuguer("say","en",{"neg":True,"prog":True,"pas":False,"perf":True,"refl":True})
    decliner("chat","fr")
    decliner("beau","fr")
    decliner("love","en")
    decliner("good","en")