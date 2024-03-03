## Explanation of the system used in WebNLG Challendge 2020:
##    http://rali.iro.umontreal.ca/rali/sites/default/files/publis/WebGen.pdf

from benchmark_reader import Benchmark, select_files
from Graph import Graph
import os, textwrap

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
# you can use any of the following config names as a second argument:
configs = ["release_v1", "release_v2", "release_v2.1", "release_v2.1_constrained",
           "release_v2_constrained", "release_v3.0_en", "release_v3.0_ru", "webnlg_challenge_2017"]
splits = ["train", "dev", "test"]
def load_benchmark_from_dataset(config, split,categorie,start,end,eid):
    from datasets import load_dataset
    b = Benchmark()
    dataset = load_dataset("web_nlg", config, split=split)
    b.benchmark_from_dataset(dataset, categorie, start, end, eid)
    return b


def process(realizer,categorie,start,end,eid=None,sortPred=False):
    # b = load_benchmark_from_files(path_to_corpus,'',start,end)
    b = load_benchmark_from_dataset("release_v3.0_en","train",categorie,start,end,eid)
    print("Number of entries:", b.entry_count())
    # (subjects,predicates,objects) = b.subjects_predicates_objects()
    # print("*** Subjects\n",subjects)
    # print("*** Predicates\n",predicates)
    # print("*** Objects\n",objects)

    realizer.nbDefaultRealizers = 0
    for entry in b.entries:
        print("\n==== %s: %s.%s" % (entry.size, entry.category, entry.id))
        print("\n".join(entry.list_triples()))
        print("[%s predicates]"%("sorted" if sortPred else "unsorted"))
        print("\n".join(textwrap.wrap(realizeTriples(realizer,entry,sortPred),width=120)))
    print("Default realizer was used: %5d times" % realizer.nbDefaultRealizers)

if __name__ == '__main__':
    # import English, Francais
    # en = set(English.English.sentencePatterns.keys())
    # fr = set(Francais.Francais.sentencePatterns.keys())
    # print(sorted(fr.difference(en)))
    # print(sorted(en.difference(fr)))

    # redirect stderr to a file, useful for isolating pyrealb warnings
    # import sys
    # sys.stderr = open("error-log.txt","w")

    from English import English
    # process(English(),'Astronaut',7,7,'Id36',True)
    process(English(),'Building',5,5,'Id110',True)
    # process(English(),'',7,7,None,True)

    from Francais import Francais
    # process(Francais(),'University',3,3,'Id49',True)
    process(Francais(), 'Building', 5, 5, 'Id110', True)
    # process(Francais(),'',1,7,None,True)

