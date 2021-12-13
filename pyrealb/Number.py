#Fonctions pour la sortie en lettres:
#Fonction EnToutesLettres par Guy Lapalme , légèrement modifiée par Francis pour accomoder le genre
import re,sys

def enToutesLettres(s,lang):
    en=lang=="en"
    trace=False; # utile pour la mise au point

    # expressions des unités pour les "grands" nombres >1000 
    # expressions donnent les formes [{singulier, pluriel}...]
    #  noms de unités selon l'échelle courte présentée dans le Guide Antidote
    # elle diffère de celle présentée dans http:#villemin.gerard.free.fr/TABLES/NbLettre.htm
    unitesM=[   {"sing":"mille"         ,"plur":"mille"}        # 10^3
               ,{"sing":"un million"    ,"plur":"millions"}     # 10^6
               ,{"sing":"un milliard"   ,"plur":"milliards"}    # 10^9
               ,{"sing":"un trillion"   ,"plur":"trillions"}    # 10^12
               ,{"sing":"un quatrillion","plur":"quatrillions"} # 10^15
               ,{"sing":"un quintillion","plur":"quintillions"} # 10^18
                ];
    unitsM =[   {"sing":"one thousand"      ,"plur":"thousand"}    # 10^3
               ,{"sing":"one million"       ,"plur":"million"}     # 10^6
               ,{"sing":"one billion"       ,"plur":"billion"}     # 10^9
               ,{"sing":"one trillion"      ,"plur":"trillion"}    # 10^12
               ,{"sing":"one quatrillion"   ,"plur":"quatrillion"} # 10^15
               ,{"sing":"one quintillion"   ,"plur":"quintillion"} # 10^18
                ];

    maxLong=21;  # longueur d'une chaîne de chiffres traitable (fixé par la liste unitesM)

    # séparer une chaine en groupes de trois et complétant le premier groupe avec des 0 au début
    def splitS(s):
        if len(s)>3:
            return splitS(s[:-3])+[s[-3:]]
        elif len(s)==1: s="00"+s
        elif len(s)==2: s="0"+s
        return [s]

    # est-ce que tous les triplets d'une liste correspondent à  0 ?
    def tousZero(ns):
        if len(ns)==0:return True;
        return ns[0]=="000" and tousZero(ns[1:])

    # création d'une liste de triplets de chiffres
    def grouper(ns): # ns est une liste de chaines de 3 chiffres
        l=len(ns)
        if trace: print("grouper:"+l+":"+ns)
        head=ns[0]
        if l==1:return centaines(head)
        tail=ns[1:]
        if head=="000": return grouper(tail)
        uM=unitsM if en else unitesM;
        return (uM[l-2]["sing"] if head=="001" else grouper([head])+" "+uM[l-2]["plur"])\
                +" "+("" if tousZero(tail) else grouper(tail));

    # traiter un nombre entre 0 et 999
    def centaines(ns): # ns est une chaine d'au plus trois chiffres
        if trace:print("centaines:"+ns)
        if len(ns)==1: return unites(ns)
        if len(ns)==2: return dizaines(ns)
        c=ns[0]       # centaines
        du=ns[1:] # dizaines+unités
        if c=="0": return dizaines(du)
        cent="hundred" if en else "cent"
        if du=="00":
            if c=="1":return ("one " if en else "")+cent
            return unites(c)+" "+cent+("" if en else "s")
        if c=="1": return ("one " if en else "")+cent+" "+dizaines(du)
        return unites(c)+" "+cent+(" and " if en else" ")+dizaines(du)

    # traiter un nombre entre 10 et 99
    def dizaines(ns):# ns est une chaine de deux chiffres
        if trace: print("dizaines:",ns);
        d=ns[0] # dizaines
        u=ns[1] # unités
        if d=="0": return unites(u)
        elif d=="1":
            if en: 
                return ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"][int(u)]
            else:
                return["dix","onze","douze","treize","quatorze","quinze","seize","dix-sept","dix-huit","dix-neuf"][int(u)];
        elif d in "23456":
            tens = (["twenty","thirty","forty","fifty","sixty"] if en else 
                    ["vingt","trente","quarante","cinquante","soixante"])[int(d)-2]
            if u=="0": return tens
            return tens + ( ("-one" if en else " et un") if u=="1" else ("-"+unites(u)))
        elif d=="7":
            if u=="0": return "seventy" if en else "soixante-dix"
            return ("seventy-"+unites(u))if en else ("soixante-"+dizaines("1"+u))
        elif d=="8":
            if u=="0": return "eighty" if en else "quatre-vingts"
            return ("eighty-" if en else "quatre-vingt-")+unites(u)
        elif d=="9":
            if u=="0": return "ninety" if en else "quatre-vingt-dix"
            return ("ninety-"+unites(u))if en else ("quatre-vingt-"+dizaines("1"+u))
        else:
            print("strange dizaine:",ns,file=sys.stderr)

    # traiter un chiffre entre 0 et 10
    def unites(u): # u est une chaine d'un chiffre
        if en: return ["zero","one","two","three","four","five","six","seven","eight","nine"][int(u)]
        return ["zéro","un","deux","trois","quatre","cinq","six","sept","huit","neuf"][int(u)]
    
#/ début de l'exécution de la fonction
    if isinstance(s,int):s=str(s) # convertir un nombre en chaîne
    if not re.match(r"^-?\d+$",s):
        print("nombreChaineEnLettres ne traite que des chiffres:"+s,file=sys.stderr)
    neg=False
    if s[0]=="-":
        neg=True
        s=s[1:]
    if len(s)>maxLong:
        print("nombreChaineEnLettres ne traite que les nombres d'au plus "+maxLong+" chiffres:"+s,sys.stderr)
    res=grouper(splitS(s))
    if neg: res=("minus " if en else "moins ")+res
    return res.strip()


# si l'orthographe française rectifiée est demandée, appliquer cette fonction à la sortie
# de enToutesLettres() pour mettre des tirets à la place des espaces partout dans le nombre...
# def rectifiee(s){
#     return s.replace(/ /g,"-");
# }

# écriture des nombres ordinaux   #GL

# rules taken from https:#www.ego4u.com/en/cram-up/vocabulary/numbers/ordinal
ordEnExceptions={"one":"first","two":"second","three":"third","five":"fifth",
                 "eight":"eighth","nine":"ninth","twelve":"twelfth"}
# règles tirées de https:#francais.lingolia.com/fr/vocabulaire/nombres-date-et-heure/les-nombres-ordinaux
ordFrExceptions={"un":"premier","une":"première","cinq":"cinquième","neuf":"neuvième"}

def ordinal(s,lang,gender):
    en = lang=="en"
    s=enToutesLettres(s,lang)
    if s=="zéro" or s=="zero": return s
    m=re.match(r"(.*?)(\w+)$",s)
    lastWord=m[2]
    if en: 
        if lastWord in ordEnExceptions: return m[1]+ordEnExceptions[lastWord]
        if s[-1]=="y": return s[:-1]+"ieth"; # added from the reference
        return s+"th"
    else:
        if s == "un":return "première" if gender=="f" else "premier"
        if s.endswith("et un"): return s+"ième"
        if lastWord in ordFrExceptions: return m[1]+ordFrExceptions[lastWord]
        if s[-1]=="e" or s.endswith("quatre-vingts"): return s[:-1]+"ième";
        return s+"ième"

if __name__ == '__main__':
    print(enToutesLettres("1234567","en"))
    print(enToutesLettres("1234567","fr"))
    print(enToutesLettres(-45, "en"))
    print(enToutesLettres(300, "fr"))
    print(ordinal(34,"en","f"))
    for n in range(7,100000, 397):
        print(enToutesLettres(n, "en"))
        print(enToutesLettres(n, "fr"))
        

