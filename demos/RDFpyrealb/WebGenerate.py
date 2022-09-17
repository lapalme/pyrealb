## read the corpus
from benchmark_reader import Benchmark, select_files
from Graph import Graph
import os

path_to_corpus = os.path.abspath(os.path.join(os.path.dirname(__file__),"data"))

def realizeTriples(entry,showJSRealExp,sortPred):
    graph=Graph(entry.category,entry.modifiedtripleset.triples,sortPred)
    print(graph.show())
    realization=graph.realize(showJSRealExp)
    print(realization)
    return realization

def process(categorie,start,end,sortPred):
    b = Benchmark()
    files = select_files(path_to_corpus,categorie,(start,end+1))
    b.fill_benchmark(files)
    for entry in b.entries:
        print("\n====%s: %s.%s [%s predicates]"%(entry.size,entry.category,entry.id,
                                                    "sorted" if sortPred else "unsorted"))
        realizeTriples(entry,False,sortPred)

if __name__ == '__main__':
    process('', 6, 7,True)
