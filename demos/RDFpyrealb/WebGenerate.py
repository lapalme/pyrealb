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

from datasets import load_dataset


def process(realizer,categorie,start,end,eid=None,sortPred=False):
    b = Benchmark()
    ## using files from the data directory
    # files = select_files(path_to_corpus,categorie,(start,end+1))
    # b.fill_benchmark(files)

    ## using HuggingFace dataset
    #      https://huggingface.co/datasets/web_nlg
    # you can use any of the following config names as a second argument:
    configs = ["release_v1", "release_v2", "release_v2.1", "release_v2.1_constrained",
               "release_v2_constrained", "release_v3.0_en", "release_v3.0_ru", "webnlg_challenge_2017"]
    splits = ["train", "dev", "test"]
    dataset = load_dataset("web_nlg", "release_v3.0_en", split="train")
    b.benchmark_from_dataset(dataset, categorie, start, end, eid)
    print("Number of entries:", b.entry_count())
    # (subjects,objects) = b.subjects_objects()
    # print("subjects",subjects)
    # print("objects",objects)

    realizer.nbDefaultRealizers = 0
    for entry in b.entries:
        print("\n==== %s: %s.%s [%s predicates]"%(entry.size,entry.category,entry.id,
                                                    "sorted" if sortPred else "unsorted"))
        print("\n".join(textwrap.wrap(realizeTriples(realizer,entry,sortPred),width=120)))
    print("Default realizer was used: %5d times" % realizer.nbDefaultRealizers)

if __name__ == '__main__':
    from English import English
    process(English(),'Astronaut',7,7,'Id36',True)
    from Francais import Francais
    process(Francais(),'Astronaut',7,7,'Id36',True)

