from pyrealb import *
from opts_feats import opts2feats,tense2feats, getTabCounters
import re

stanzaVerbFile = "./french/verb.txt"
stanzaVerbs = set(w.strip().lower() for w in open(stanzaVerbFile,"r").readlines())
nbMissing = 0
# verbes = ["aimer", "avoir", "chanter", "chercher", "demander", "devenir", "devoir", "donner", "dormir", "être",
#           "finir", "jouer", "lever", "lire", "manger", "ouvrir", "parler", "pouvoir", "regarder", "voir",
#           "voler", "vouloir"]
trace = True

def keep(entry):
    if "V" in entry:
        return "niveau" in entry["V"] and entry["V"]["niveau"]<=1
    else:
        return False

lexicon = getLexicon("fr")
verbes = [lemma for (lemma,entry) in lexicon.items() if keep(entry)]

def tokenize(sent):
    tokens = re.split(r"(\W)",sent)
    i=0
    while i<len(tokens)-1:
        if tokens[i+1]=="'": # combiner apostrophe avec le précédent
            tokens[i]+="'"
            tokens.pop(i+1)
        elif tokens[i]==" ": #ignorer les blancs
            tokens.pop(i)
        i+=1
    return tokens[:-1] #irgnorer le dernier blanc

# create a UD structures
#  simple tenses
def makeUDsent_TempsSimples(sent_id, sent, infos,
                           pron_form,pron_lemma,pron_feats,
                           verb_form,verb_lemma,verb_feats):
    verb_misc = "_" if verb_form in stanzaVerbs else "missing"
    return f"""# text = {sent}
# sent_id = {sent_id}
# pyrealb-infos = {infos}
1	{pron_form}	{pron_lemma}	PRON	PRP	{pron_feats}	2	nsubj	_	_
2	{verb_form}	{verb_lemma}	VERB	VBP	{verb_feats}	0	root	_	{verb_misc}
3	.	.	PUNCT	.	_	2	punct	_	_
"""

def makeUDsent_TempsComposes(sent_id, sent, infos,
                            pron_form,pron_lemma,pron_feats,
                            aux_form,aux_lemma,aux_feats,
                            verb_form,verb_lemma,verb_feats):
    verb_misc = "_" if verb_form in stanzaVerbs else "missing"
    aux_misc  = "_" #if aux_form in stanzaVerbs else "missing"
    return f"""# text = {sent}
# sent_id = {sent_id}
# pyrealb-infos = {infos}
1	{pron_form}	{pron_lemma}	PRON	PRP	{pron_feats}	3	nsubj	_	_
2	{aux_form}	{aux_lemma}	AUX	_	{aux_feats}	3	aux:tense	_	{aux_misc}
3	{verb_form}	{verb_lemma}	VERB	VBP	{verb_feats}	0	root	_	{verb_misc}
4	.	.	PUNCT	.	_	3	punct	_	_
"""

def makeUDsent_ParticipePresent(sent_id, sent, infos,
                                pron_form,pron_lemma,pron_feats,
                                aux_form,aux_lemma,aux_feats,
                                verb_form,verb_lemma,verb_feats):
    verb_misc = "_" if verb_form in stanzaVerbs else "missing"
    aux_misc  = "_" #if aux_form in stanzaVerbs else "missing"
    return f"""# text = {sent}
# sent_id = {sent_id}
# pyrealb-infos = {infos}
1	{pron_form}	{pron_lemma}	PRON	PRP	{pron_feats}	3	nsubj	_	_
2	{aux_form}	{aux_lemma}	AUX	_	{aux_feats}	3	cop:tense	_	{aux_misc}
3	{verb_form}	{verb_lemma}	VERB	VBP	{verb_feats}	0	root	_	{verb_misc}
4	.	.	PUNCT	.	_	3	punct	_	_
"""

def makeUDsent_ParticipePasse(sent_id, sent, infos,
                              pron_form,pron_lemma,pron_feats,
                              aux_form,aux_lemma,aux_feats,
                              verb_form,verb_lemma,verb_feats):
    verb_misc = "_" if verb_form in stanzaVerbs else "missing"
    aux_misc  = "_" #if aux_form in stanzaVerbs else "missing"
    return f"""# text = {sent}
# sent_id = {sent_id}
# pyrealb-infos = {infos}
1	{pron_form}	{pron_lemma}	PRON	PRP	{pron_feats}	3	nsubj	_	_
2	{aux_form}	{aux_lemma}	AUX	_	{aux_feats}	3	aux:pass:tense	_	{aux_misc}
3	{verb_form}	{verb_lemma}	VERB	VBP	{verb_feats}	0	root	_	{verb_misc}
4	.	.	PUNCT	.	_	3	punct	_	_
"""

aux_temps = {"pc":"p","pq":"i","fa":"f","cp":"c","pr":"p"}
def makeSentences(infos, verb_lemma, tense):
    sent_id = f"{verb_lemma}-{tense}"
    uds = []
    for (pe,n) in [(1,"s"),(2,"s"),(3,"s"),(1,"p"),(2,"p"),(3,"p")]:
        pron_lemma = Pro("moi").pe(pe).n(n)
        pron_ton = pron_lemma.clone().tn("").realize()
        pron = pron_lemma.c("nom")
        pron_opts = {"pe":pe,"n":n,"c":"nom"}
        if tense in {"p","ps","i","f","c"}:
            verb = V(verb_lemma).t(tense).pe(pe).n(n)
            try:
                verb_form = verb.realize()
            except Exception as error:
                if trace: print("***", error)
                continue
            # if verb_form.startswith("[["):continue
            verb_opts = {"t":tense, "pe":pe, "n":n}
            sent = S(pron,VP(verb)).realize()
            if trace and pe==1 and n=="s": print(sent)
            tokens = tokenize(sent)
            uds.append(makeUDsent_TempsSimples(f"{sent_id}-{pe}{n}",sent,infos,
                                               tokens[0],pron_ton,opts2feats(pron_opts),
                                               tokens[1],verb_lemma,opts2feats(verb_opts)))
        elif tense in {"pc","pq","fa","cp","pr"}:
            aux_lemma = "être" if tense=="pr" or getLemma(verb_lemma)["V"]["aux"]=="êt" else "avoir"
            aux = V(aux_lemma).t(aux_temps[tense]).pe(pe).n(n)
            aux_form = aux.realize()
            aux_opts = {"t":aux_temps[tense],"pe":pe,"n":n}
            verb = V(verb_lemma).t("pr" if tense == "pr" else "pp")
            try:
                verb_form = verb.realize()
            except Exception as error:
                if trace: print("***", error)
                continue
            if verb_form.startswith("[["):continue;
            verb_opts = {"t":"pr" if tense == "pr" else "pp"}
            if tense == "pr":
                sent = S(pron,VP(V(aux_lemma),V(verb_lemma).t(tense))).realize()
            else:
                sent = S(pron,VP(V(verb_lemma).t(tense))).realize()
            tokens = tokenize(sent)
            if trace and pe == 1 and n == "s": print(sent)
            makeUD = makeUDsent_ParticipePresent if tense == "pr" else makeUDsent_TempsComposes
            uds.append(makeUD(f"{sent_id}-{pe}{n}",sent,infos,
                              tokens[0], pron_ton, opts2feats(pron_opts),
                              tokens[1],aux_lemma,opts2feats(aux_opts),
                              tokens[2], verb_lemma, opts2feats(verb_opts)))
        else:
            print(f"** strange tense:{tense} for {verb_lemma}")
    return uds

def makeSentencesPP(infos, verb_lemma, tense):
    sent_id = f"{verb_lemma}-{tense}"
    uds = []
    for (pe,n,g) in [(3,"s","m"),(3,"s","f"),(3,"p","m"),(3,"p","f")]:
        pron_lemma = Pro("moi").pe(pe).n(n).g(g)
        pron_ton = pron_lemma.clone().tn("").realize()
        pron = pron_lemma.c("nom")
        pron_opts = {"pe":pe,"n":n,"g":g,"c":"nom"}
        aux_lemma = "être"
        aux = V(aux_lemma).t("p").pe(pe).n(n)
        aux_form = aux.realize()
        aux_opts = {"t": "p", "pe": pe, "n": n}
        verb = V(verb_lemma).t("pp").n(n).g(g)
        try:
            verb_form = verb.realize()
        except Exception as error:
            if trace: print("***", error)
            continue
        verb_opts = {"t":"pp","g":g,"n":n}
        sent = S(pron,VP(V(aux_lemma),V(verb_lemma).t(tense))).realize()
        if trace and g == "f" and n == "p": print(sent)
        tokens=tokenize(sent)
        uds.append(makeUDsent_ParticipePasse(f"{sent_id}-{pe}{n}", sent, infos,
                                             tokens[0], pron_ton, opts2feats(pron_opts),
                                             tokens[1], aux_lemma, opts2feats(aux_opts),
                                             tokens[2], verb_lemma, opts2feats(verb_opts)))
    return uds


# generate for each "interesting" tenses
def makeVerb(verb_lemma):
    entry = lexicon[verb_lemma]
    tab = entry['V']['tab']
    verbFile.write(f"{verb_lemma}\t{tab}\t{counters_fr[tab]}\n")
    infos = ", ".join(entry.keys())+f"\t{tab}\t{counters_fr[tab]}"
    return [*makeSentences(infos, verb_lemma, "p"),
            *makeSentences(infos, verb_lemma, "pc"),
            *makeSentences(infos, verb_lemma, "pr"),
            *makeSentencesPP(infos, verb_lemma, "pp")
           ]


if __name__ == "__main__":
    loadFr()
    Constituent.exceptionOnWarning = True
    lexicon = getLexicon("fr")
    counters_fr = getTabCounters("fr")
    verbFile = open("french1stGrade.txt","w",encoding="utf-8")
    french1stGradeFile = open("french1stGrade.conllu","w",encoding="utf-8")
    for verbe in verbes:
        french1stGradeFile.write("\n".join(makeVerb(verbe))+"\n")
        if trace: print("---")
    print(len(verbes),"verbes créés sur ",french1stGradeFile.name)