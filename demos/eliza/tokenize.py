from pyrealb import *
import re,sys

trace=False

# only set this flag during development fo this IDE because it takes a while to execute
# and is not needed unless the lexicons or the rules are changed
checkAmbiguities=False

lemmataLang="fr"

def tokenizeFr(sentence):
    elidableFRList = ["ce", "la", "le", "je", "me", "te", "se", "de", "ne", "que", "puisque", "lorsque", "jusque", "quoique"]
    contractionFrTable = {
        "au":"à+le","aux":"à+les","ç'a":"ça+a",
        "du":"de+le","des":"de+les","d'autres":"de+autres",
        "s'il":"si+il","s'ils":"si+ils"}

    # split on non-French letter and apostrophe and remove empty tokens
    words = [w for w in re.split(r"[^a-z'àâéèêëîïôöùüç]",sentence.lower()) if len(w)>0]
    # expand elision and contraction
    i=0
    while i<len(words):
        word = words[i]
        if word not in lemmataFr:
            # word does not exist try to expand elision or contraction
            m = re.fullmatch(r"(.*?)'([haeiouyàâéèêëîïôöùüç].*)",word) # check for apostrophe followed by vowell or h
            if m :
                for elw in elidableFRList: # expand elision
                    if elw.startswith(m.group(1)):
                        words[i:i+1]=[elw,m.group(2)]
                        i+=1
                        break
            else:
                if word in contractionFrTable:
                    words[i:i+1]=contractionFrTable[word].split("+")
                    i+=1
        i+=1
    return words

lemmataFr = buildLemmataMap("fr")

if __name__ == '__main__':
    print("---lemmataFr: OK")
    # add tests fo  lemmatization
    tokens = tokenizeFr("J'ai mangé du pain aujourd'hui à l'hôpital, quoiqu'encore pas assez!")
    print(tokens)
