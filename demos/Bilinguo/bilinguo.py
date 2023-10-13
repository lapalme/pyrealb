import re, random

from pyrealb import *
from sentences import sentences

# return a list of shuffled indices for a list
def getIndices(lst):
    l = len(lst)
    return random.sample(range(l),k=l)

# split a string into tokens taking into account French accented letters
# because of the parentheses in the regex all tokens are kept.
# Tokens with only spaces are removed
def tokenize(s):
    return [tok.strip() for tok in re.split(r"([^a-zA-Zà-üÀ-Ü]+)",s) if len(tok.strip())>0]

# get value of parameter and evaluate it in the appropriate language if it is a function
def getParam(lang,val):
    if callable(val):
        load(lang)
        return val()
    return val

def makeStructs(sent, src,tgt):
    # for a given sentence sent, generate an exercise with the given source and target languages
    # HACK: the word selection is done by shuffling a new list of indices (so that the corresponding src and tgt words are selected)
    #       and taking (shifting) the first indices of this list when needed either for a word or a distractor
    #       Because currently inflection is done within the jsRealB structure, it is not applied to the corresponding distractor
    #       this would imply to reorganize the way the specifications are given
    [srcIdx,tgtIdx] = [0,1] if src=="fr" else [1,0]
    # build the list of parameters and distractors for the target language
    params=[]
    distractors=[]
    for ps in sent["params"]:
        # if (!Array.isArray(ps[0]))ps=ps.map(e=>[e,e]) # src and tgt values are the same
        indices = getIndices(ps)
        idx=indices.pop(0)
        param=[0,0]
        param[srcIdx]=getParam(src,ps[idx][srcIdx])
        param[tgtIdx]=getParam(tgt,ps[idx][tgtIdx])
        params.append(param)
        if len(indices)>0:
            if isinstance(param[tgtIdx],str) and len(param[tgtIdx])>1:
                distractor=ps[indices.pop(0)][tgtIdx]
                if distractor not in distractors:
                    distractors.append(distractor)
                elif isinstance(param[tgtIdx],Constituent):
                    distractors.append(tokenize(getParam(tgt,ps[indices.pop(0)][tgtIdx]).realize()))

    # create source and target structure
    load(src)
    srcStruct = sent[src](*[p[srcIdx] for p in params])
    load(tgt)
    tgtStruct = sent[tgt](*[p[tgtIdx] for p in params])
    return [srcStruct,tgtStruct,distractors,sent["id"]]

def makeSentences(sent,src,tgt):
    t = oneOf([{"fr":"p","en":"p"},{"fr":"pc","en":"ps"},{"fr":"f","en":"f"}])
    typ = oneOf([{},{"neg":True},{"prog":True},{"mod":"poss"},{"int":"yon"},{"int":"tag"}])
    res={}
    [res[src],res[tgt],res["distractors"],_id]=makeStructs(sent,src,tgt)
    res[src].t(t[src]).typ(typ)
    res[tgt].t(t[tgt]).typ(typ)
    res["t"] = t[src]
    res["typ"] = typ
    return res


def showSentences(sent,src,tgt):
    sents=makeSentences(sent,src,tgt)
    res=[];
    res.append(sents[src].realize(src))
    res.append(sents[tgt].realize(tgt))
    res.append(", ".join(sents["distractors"]))
    print("%5s %-2s %-15s : %s"%(sent["id"],sents["t"],repr(sents["typ"])," || ".join(res)))

def instructions(lang):
    if lang=="fr":
        print(S(VP(V("traduire").t("ip").pe(2).n("p"),
                   PP(P("en"), N("anglais")),
                   NP(D("le"), N("phrase").n("p"),
                      PP(P("en"), N("français"))),
                   PP(P("en"), V("utiliser").t("pr"),
                      D("certain").n("p"),
                      PP(P("de"), NP(D("le"), N("mot").n("p"),
                                     V("suggérer").t("pp")))))).realize())
        print(S(VP(V("taper").t("ip").pe(2).n("p"),
                   N("fin").ba('"'),
                   PP(P("pour"),V("terminer").t("b")))).realize())
    else:
        print(S(VP(V("translate").t("ip").pe(2).n("p"),
                   PP(P("in"), N("English")),
                   NP(D("the"), N("sentence").n("p"),
                      PP(P("in"), N("French"))),
                   PP(V("use").t("pr"),
                      D("some").n("p"),
                      PP(P("of"), NP(D("the"),
                                     V("suggest").t("pp"),
                                     N("word").n("p")))))).realize())
        print(S(VP(V("type").t("ip").pe(2).n("p"),
                   N("end").ba('"'),
                   PP(V("exit").t("b-to")))).realize())

def play(src,tgt):
    load(src)
    instructions(src)
    ncpas=", n'est-ce pas?" # HACK: consider this as a single token when at the end
    while True:
        sents = makeSentences(random.sample([sentences[1]],k=1)[0],src,tgt)
        expected = sents[tgt].realize(tgt).strip()
        if expected.endswith(ncpas):
            tokens = tokenize(expected[:-len(ncpas)])+[ncpas]
        else:
            tokens = tokenize(expected)
        tokens += sents["distractors"]
        random.shuffle(tokens)
        answer = input(sents[src].realize(src) +"\n" + ", ".join(tokens)+"\n > ")
        if answer == "fin" or answer=="end": break
        print("   "+expected+":"+("OK" if answer.strip()==expected else "KO"))


if __name__ == "__main__":
    play("en","fr")
    # for sent in sentences:
    #     showSentences(sent, "fr", "en")
    #     showSentences(sent, "en", "fr")

