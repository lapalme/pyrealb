#!/usr/bin/env python3
'''
Created on 30 janv. 2018
   Calcul de la distance de Levenshtein entre deux listes de chaînes (mots)
   Création d'une chaîne qui fait ressortir les différences
   en barrant les mots détruits dans la première chaîne et 
   en soulignant les mots insérés
Si le terminal supporte les codes couleurs, les destructions s'affichent en rouge et
les insertions en bleu

On peut comparer deux fichiers alignés ligne à ligne
appel: levenshtein.py fichier1 fichier2 [char]
s'il y a un troisième paramètre la comparaison se fait par caractères sinon par "mots" 
   
@author: lapalme
'''
import re

## comparaison en ignorant la casse et les caractères non alphabétiques...
def wordEquals(s1,s2):
    return re.sub(r"\W","",s1.lower()) == re.sub(r"\W","",s2.lower())

def charEquals(c1,c2):
    return c1==c2

def printDistances(text1,text2,distance):
    m=len(text1)
    n=len(text2)
    print(12*" ",end="")
    for j in range(0,n+1):
        print("%5d "%j,end="")
    print()
    print(12*" ",end="")
    for j in range(0,n+1):
        print("%5.5s "%(text2[j-1] if j>0 else " "),end="")
    print()
    for i in range(0,m+1):
        print("%5d "%i,end="")
        print("%5.5s "%(text1[i-1] if i>0 else ""),end="")
        for j in range(0,n+1):
            print("%5d "%distance[i][j],end="")
        print()

def getLevenshteinOps(text1,text2,equals=wordEquals):
    edits=[]
    #init matrix
    distance=[0]*(len(text1)+1)
    iStart=0
    jStart=0
    for i in range(0,len(text1)+1):
        distance[i]=[0]*(len(text2)+1)
        distance[i][0]=i
    for j in range(0,len(text2)+1):
        distance[0][j]=j
    # compute distance
    for i in range(1,len(text1)+1):
        for j in range(1,len(text2)+1):
            distance[i][j]=min([distance[i-1][j]+1,
                                distance[i][j-1]+1,
                                distance[i-1][j-1]+(0 if equals(text1[i-1],text2[j-1]) else 1)])
#     printDistances(text1,text2,distance)
    # find edits
    i=len(text1)
    j=len(text2)
    while i>0 and j>0:
        minVal=distance[i][j]-1
#         print("minval=%d, i=%d, j=%d"%(minVal,i,j))
        if i>0 and j>0 and distance[i-1][j-1]==minVal:
            iStart=i=i-1
            jStart=j=j-1
            while i>0 and j>0 and distance[i-1][j-1]==minVal-1:
                i-=1
                j-=1
                minVal-=1
            if j==0:
                while i>0 and distance[i-1][0]==minVal-1:
                    i-=1
                    minVal-=1
            elif i==0:
                while j>0 and distance[0][j-1]==minVal-1:
                    j-=1
                    minVal-=1
            edits.append(("REP",i,iStart,j,jStart))
        elif j>0 and distance[i][j-1]==minVal:
            jStart=j=j-1
            while j>0 and distance[i][j-1]==minVal-1:
                j-=1
                minVal-=1
            edits.append(("INS",j,jStart,i))
        elif i>0 and distance[i-1][j]==minVal:
            iStart=i=i-1
            while i>0 and distance[i-1][j]==minVal-1:
                i-=1
                minVal-=1
            edits.append(("DEL",i,iStart))
        else:
            i-=1
            j-=1
    if i>0 and j==0:
        edits.append(("DEL",0,i-1))
    elif j>0 and i==0:
        edits.append(("INS",0,j-1,0))
    return (distance[len(text1)][len(text2)],edits)

## pour faire sortir les corrections en couleur sur un terminal
import os,sys
escape='\u001B[%sm'
red  =[escape%'31'] if sys.stdout.isatty() else []
blue =[escape%'34'] if sys.stdout.isatty() else []
reset=[escape%'0']  if sys.stdout.isatty() else []

# appliquer une combinaison à chaque mot du texte
def deletion(text):
    return combine(text,'\u0336',red)

def insertion(text):
    return combine(text,'\u0332',blue)

def combine(text,combineChar,couleur):
    return ["".join(couleur+[c + combineChar for c in w]+reset) for w in text]

# taken from pyrealb ConstituentEn.py
contractionEnTable = {
    "are+not": "aren't", "can+not": "can't", "did+not": "didn't", "do+not": "don't", "does+not": "doesn't",
    "had+not": "hadn't", "has+not": "hasn't", "have+not": "haven't", "is+not": "isn't", "must+not": "mustn't",
    "need+not": "needn't", "should+not": "shouldn't", "was+not": "wasn't", "were+not": "weren't",
    "will+not": "won't", "would+not": "wouldn't",
    "let+us": "let's",
    "I+am": "I'm", "I+will": "I'll", "I+have": "I've", "I+would": "I'd", "I+had": "I'd",
    "she+will": "she'll", "he+has": "he's", "he+is": "he's", "she+had": "she'd", "she+would": "she'd",
    "he+will": "he'll", "she+has": "she's", "she+is": "she's", "he+would": "he'd", "he+had": "he'd",
    "you+are": "you're", "you+will": "you'll", "you+would": "you'd", "you+had": "you'd", "you+have": "you've",
    "we+are": "we're", "we+will": "we'll", "we+would": "we'd", "we+had": "we'd", "we+have": "we've",
    "they+will": "they'll", "they+are": "they're", "they+would": "they'd", "they+had": "they'd",
    "they+have": "they've",
    "it+is": "it's", "it+will": "it'll", "it+had": "it'd", "it+would": "it'd",
    "there+will": "there'll", "there+has": "there's", "there+is": "there's", "there+have": "there've",
    "that+is": "that's", "that+would": "that'd", "that+had": "that'd", "that+will": "that'll",
    "what+is": "what's"
}

def capitalize(s):
    return s[0].upper()+s[1:]

# invert table and add capitalized version
# CAUTION: some "duplicate" entries (there's => there is / there has) are overriden by
#          inversion process, so some expansions are not recognized.
# here is the list of duplicates for which we put the
# "the one that we thought was the most frequent" one as last, so that it is
# the last value that is kept when the table is built:
#    "I'd", "he's", "she'd", "she's", "he'd", "you'd", "we'd", "they'd", "it'd", "there's", "that'd"
#
# TODO: use these expansions directly in the matching process, but this would involve comparing
#       more than one token in the core of the algorithm
expansionTable = {v:k for k,v in contractionEnTable.items()}
expansionTable.update({capitalize(v): capitalize(k) for k, v in contractionEnTable.items()})

# HACK: expand contractions in text (a lst of strings)
def expandContractions(text):
    i = len(text)-1
    while i>=0:
        ti = text[i]
        if ti in expansionTable:
            text[i:i+1]=expansionTable[ti].split("+")
        i -= 1
    return text

def applyEdits(edits,text1,text2,joinString=" "):
    res=[]
    last1=0
    i=len(edits)-1
    while i>=0:
        curEdit=edits[i]
        op=curEdit[0]
        if op=="REP":
            (_,start1,end1,start2,end2)=curEdit
            res.extend(text1[last1:start1])
            res.extend(deletion(text1[start1:end1+1]))
            res.extend(insertion(text2[start2:end2+1]))
            last1=end1+1
        elif op=="INS":
            (_,start2,end2,start1)=curEdit
            res.extend(text1[last1:start1])
            res.extend(insertion(text2[start2:end2+1]))
            last1=start1
        elif op=="DEL":
            (_,start1,end1)=curEdit
            res.extend(text1[last1:start1])
            res.extend(deletion(text1[start1:end1+1]))
            last1=end1+1
        i-=1
    res.extend(text1[last1:])
    return joinString.join(res)

def compareLevenshtein(s1,s2,equals=wordEquals,joinString=" "):
    text1=list(s1) if joinString=="" else s1.split(joinString)
    text2=list(s2) if joinString=="" else s2.split(joinString)
    (editDist,edits)=getLevenshteinOps(text1,text2,equals)
    return (editDist,applyEdits(edits, text1,text2,joinString))


def test(s1,s2,equals=wordEquals,joinString=" "):
    text1=list(s1) if joinString=="" else s1.split(joinString)
    text1 = expandContractions(text1)
    text2=list(s2) if joinString=="" else s2.split(joinString)
    print("s1:"+str(text1))
    print("s2:"+str(text2))
    (editDist,edits)=getLevenshteinOps(text1, text2,equals)
    print("edit distance:"+str(editDist)+":"+str(edits))
    print(applyEdits(edits, text1, text2,joinString))

def simpleTests():
    # print(deletion(["the","boys","cry"]))
    # test("The number of pandas increases.","Increases that is the panda of the number.")
    # test("Someone who sifts the thistle.","The person who sifts through the thistle.")
    # test("voiture","moteur",charEquals,"")
    # test("The boy cries hard","The boys who cry hard")
    # test("Les élèves sont bien reçus par le maître","Les enfants sont bien élevés")
    # test("Les élèves sont bien reçus par le maître","Les enfants sont bien élevés",charEquals,"")
    # test("The boys who cry hard","The boy cries hard",charEquals,"")
    # print(compareLevenshtein("The man loves the woman", "The woman loved the man"))
    test("We've got a Steven, there's one word that didn't crash my spell-check.",
         "We have gotten a Steven, there is one word that did not crash my spell-check.")

if __name__ == '__main__':
    import sys
    if len(sys.argv)==1:
        simpleTests()
    else: # comparer deux fichiers ligne à lignes
        lines1=open(sys.argv[1]).read().split("\n")
        lines2=open(sys.argv[2]).read().split("\n")
        charMode=len(sys.argv)==4
        if len(lines1) == len(lines2):
            for (l1,l2) in zip(lines1,lines2):
                if charMode:
                    print(compareLevenshtein(l1,l2,charEquals,"")[1])
                else:
                    print(compareLevenshtein(l1,l2)[1])
        else:
            print("fichiers non de la même longueur:%d vs %d"%(len(lines1),len(lines2)))
        
    