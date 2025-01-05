from pyrealb import *
    
## conjugation and declension

## print a table of values so that the lines are aligned
## it takes for granted that all lines are of the same length
## it transforms all values using str()

def width(val):
    if isinstance(val,str):
        return len(val)
    return len(str(val))

# the first nbHeadLines are centered and followed by a line
def printTable(table,nbHeadlines=0):
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

def realize(exp):
    try:
        return exp().realize()
    except Exception as error:
        return "--"

def declinerNom(mot,lang):
    table=[]
    if lang=="fr":
        table.append(["","Singulier","Pluriel"])
        g=getLemma(mot)["N"]["g"]
        if g in "mx":
            table.append(["Masculin",
                          realize(lambda:N(mot).g("m").n("s")),
                          realize(lambda:N(mot).g("m").n("p"))])
        if g in "fx":
            table.append(["Féminin",
                          realize(lambda:N(mot).g("f").n("s")),
                          realize(lambda:N(mot).g("f").n("p"))])
    else:
        table.append(["Singular","Plural"])
        table.append([realize(lambda:N(mot).n("s")),realize(lambda:N(mot).n("p"))])
    return table

def declinerAdjectif(mot,lang):
    table=[]
    if lang=="fr":
        table.append(["","Singulier","Pluriel"])
        table.append(["Masculin",
                      realize(lambda:A(mot).g("m").n("s")),
                      realize(lambda:A(mot).g("m").n("p"))])
        table.append(["Féminin",
                      realize(lambda:A(mot).g("f").n("s")),
                      realize(lambda:A(mot).g("f").n("p"))])
    else:
        table.append(["Comparative","Superlative"])
        table.append([realize(lambda:A(mot).f("co")),realize(lambda:A(mot).f("su"))])
    return table
        
def decliner(mot,lang):
    if lang=="fr":loadFr()
    else: loadEn()
    entry=getLemma(mot)
    if entry is None:
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
    
    def realize(t,pe,n,g=None):
        try:
            if g is not None : # French past participle
                return VP(V(verbe)).t("pp").n(n).g(g).typ(typs).realize()
            if t=="ip":
                if (n=="s" and pe in [1,3]) or (n=="p" and pe==3):
                    return "--"
                else:
                    return VP(V(verbe).t(t).pe(pe).n(n)).typ(typs).realize()
            else:
                v = V(verbe).t(t)
                if pe is None: return VP(v).typ(typs).realize()
                sp=SP(Pro("moi" if lang=="fr" else "me").c("nom").pe(pe).n(n),VP(V(verbe).t(t))).typ(typs)
                if t.startswith("s") and lang=="fr": # subjonctif
                    sp=SP(Q("que"),sp)
                return sp.realize()
        except Exception as error:
            return "--"
    
    if lang=="fr":
        loadFr()
        temps= [
            [["Présent","p"],["Imparfait","i"],["Futur simple","f"],["Passé simple","ps"]],
            [["Passé composé","pc"],["Plus-que-parfait","pq"],["Passé antérieur","pa"],["Futur antérieur","fa"]],
            [["Subjonctif présent","s"],["Subjonctif imparfait","si"],["Subjonctif passé","spa"],
             ["Subjonctif plus-que-parfait","spq"]],
            [["Conditionnel présent","c"],["Conditionnel passé","cp"],["Impératif","ip"]],
            [["Participe présent","pr"],["Participe passé","pp"],["Infinitif","b"],["Infinitif passé","bp"]]
        ]
    else:
        loadEn()
        temps= [
            [["Present","p"]],
            [["Simple past","ps"]],
            [["Future","f"]],
            [["Subjonctive","s"]],
            [["Conditional","c"]],
            [["Imperative","ip"]],
        ]
    
    print("***",verbe,"comme verbe" if lang=="fr" else "as verb",str(typs))
    print()   
    for tmp in temps:
        table=[[t[0] for t in tmp]]
        if tmp[0][0].startswith("Participe"):
            table.append([realize(t[1],None,"s" if t[1]!="pp" else None,"m" if t[1]!="pp" else None)
                          for t in tmp])
            if lang == "fr":
                table.append(["",realize("pp",None,"s","f"),"",""])
                table.append(["",realize("pp",None,"p","m"),"",""])
                table.append(["",realize("pp",None,"p","f"),"",""])
        else:
            for n in "sp":
                for pe in range(1,4):
                    table.append([realize(t[1],pe,n) for t in tmp])
        printTable(table,1)
    print("===")
        

if __name__ == '__main__':
    Constituent.exceptionOnWarning = True
    conjuguer("être","fr",{"neg":False,"prog":False,"pas":False,"refl":False})
    conjuguer("aller","fr",{"neg":False,"prog":False,"pas":False,"refl":False})
    conjuguer("dissoudre","fr",{"neg":False,"prog":False,"pas":False,"refl":False})
    conjuguer("love","en",{"neg":False,"prog":True,"pas":True,"refl":False})
    conjuguer("say","en",{"neg":True,"prog":True,"pas":False,"perf":True,"refl":True})
    decliner("chat","fr")
    decliner("beau","fr")
    decliner("manager","en")
    decliner("good","en")
    decliner("economics","en")