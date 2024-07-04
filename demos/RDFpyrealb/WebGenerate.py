## Explanation of the system used in WebNLG Challendge 2020:
##    http://rali.iro.umontreal.ca/rali/sites/default/files/publis/WebGen.pdf
from datetime import datetime

from benchmark_reader import Benchmark, select_files
from Graph import Graph
from Realizer import showDefaultRealizers
import os, textwrap
from collections import Counter

path_to_corpus = os.path.abspath(os.path.join(os.path.dirname(__file__),"data"))

def realizeTriples(realizer,entry,sortPred):
    triples = entry.modifiedtripleset.triples
    if sortPred:
        triples.sort(key=lambda t:realizer.getPrecedence(t.p))
    graph=Graph(entry.category,triples)
    print(graph.show())
    return realizer.realize(graph,False)

def load_benchmark_from_files(path_to_corpus,categorie,start,end):
    b = Benchmark()
    ## using files from the data directory
    files = select_files(path_to_corpus,categorie,(start,end+1))
    b.fill_benchmark(files)
    return b

## using HuggingFace dataset
#      https://huggingface.co/datasets/web_nlg
# any of the following config names can be given as second argument
# the tests have mainly been done with "release_v3.0_en"
configs = ["release_v1", "release_v2", "release_v2.1", "release_v2.1_constrained",
           "release_v2_constrained", "release_v3.0_en", "release_v3.0_ru", "webnlg_challenge_2017"]
splits = ["train", "dev", "test"]
def load_benchmark_from_dataset(config, split,categorie,start,end,eid):
    from datasets import load_dataset
    b = Benchmark()
    dataset = load_dataset("web_nlg", config, split=split)
    b.benchmark_from_dataset(dataset, categorie, start, end, eid)
    return b

def process(realizer,categorie,start,end,eid=None,sortPred=False,matchProp=""):
    # b = load_benchmark_from_files(path_to_corpus,categorie,start,end)
    split = "test"
    b = load_benchmark_from_dataset("release_v3.0_en",split,categorie,start,end,eid)
    print("Number of entries:%d in %s split"%(b.entry_count(),split))
    # (subjects,predicates,objects) = b.subjects_predicates_objects()
    # print("*** Subjects\n",subjects)
    # print("*** Predicates\n",predicates)
    # print("*** Objects\n",objects)

    realizer.defaultRealizers = Counter()
    print("[%s predicates]"%("sorted" if sortPred else "unsorted"))
    for entry in b.entries:
        if entry.has_property(matchProp) and (eid is None or entry.id == eid):
            print("\n==== %s: %s.%s" % (entry.size, entry.category, entry.id))
            print("\n".join(entry.list_triples()))
            print("\n".join(textwrap.wrap(realizeTriples(realizer,entry,sortPred),width=120)))
    # print("Default realizer was used: %5d times" % realizer.nbDefaultRealizers)
    showDefaultRealizers(realizer)

def processFile(realizer,fileName, sortPred=False):
    b = Benchmark()
    b.fill_benchmark([fileName])
    realizer.defaultRealizers = Counter()
    print("[%s predicates]"%("sorted" if sortPred else "unsorted"))
    for entry in b.entries:
        print("\n==== %s: %s.%s" % (entry.size, entry.category, entry.id))
        print("\n".join(entry.list_triples()))
        print("\n".join(textwrap.wrap(realizeTriples(realizer,entry,sortPred),width=120)))
    showDefaultRealizers(realizer)


if __name__ == '__main__':
    # import English, Francais
    # en = set(English.English.sentencePatterns.keys())
    # fr = set(Francais.Francais.sentencePatterns.keys())
    # print(sorted(fr.difference(en)))
    # print(sorted(en.difference(fr)))

    # redirect stderr to a file, useful for isolating pyrealb warnings
    # import sys
    # sys.stderr = open("error-log.txt","w")
    # sys.stderr.write(str(datetime.today())+"\n")
    from rqDBPedia import loadDBpediaMemo

    memoFileName = os.path.abspath(os.path.join(os.path.dirname(__file__), "data/dbPediaMemo.json"))
    loadDBpediaMemo(memoFileName)
    # matchProp = "influencedBy|site|layout"
    matchProp = ""
    from English import English
    # process(English(),'Airport',1,1,'Id234',True)
    # process(English(),'Astronaut',7,7,'Id9',True)
    process(English(),'',1,7,None,True,matchProp=matchProp)
    # realizer=English()
    # processFile(realizer,(".","data/7triples/Astronaut.xml"))
    # processFile(realizer,(".","data/Sample-Factual.xml"),True)

    from Francais import Francais
    # process(Francais(),'Airport',1,1,'Id234',True)
    # process(Francais(), 'Astronaut', 7, 7, 'Id9', True)
    process(Francais(),'',1,7,None,True,matchProp=matchProp)
    # realizer=Francais()
    # processFile(realizer,(".","data/Sample-Factual.xml"))
    # processFile(realizer,(".","data/Sample-Factual.xml"),True)


