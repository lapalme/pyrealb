# script for submission to the 
#   GEM Shared Task at the Generation Challenges (INLG'24)
#   Shared Task - GEM 2024
#      https://gem-benchmark.com/shared_task

import os,sys,re
from collections import Counter
from benchmark_reader import Benchmark
from Graph import Graph
from English import English
from Realizer import showDefaultRealizers
from rqDBPedia import loadDBpediaMemo, saveDBpediaMemo

# change the following to access the corpus
path_to_corpus = os.path.abspath(os.path.join("/Users","lapalme","Dropbox","GEM-2024","data"))

def process(path,fileName,show=False):
    b = Benchmark()
    b.fill_benchmark([(path,fileName)])
    realizer = English()
    realizer.defaultRealizers = Counter()
    results = []
    nbTriples = 0
    for entry in b.entries:
        nbTriples += int(entry.size)
        # if int(entry.size)<7:continue
        triples = entry.modifiedtripleset.triples
        triples.sort(key=lambda t: realizer.getPrecedence(t.p))
        graph = Graph(entry.category, triples)
        # if len(graph.subjects)==1:continue
        if show:print(f"id: {entry.id}\n"+graph.show())
        out = realizer.realize(graph,False)
        if show: print(out)
        results.append(out)

    total = showDefaultRealizers(realizer)
    print(f"Default realizer was used: {total} times over "
          f"{nbTriples} triples ({round(total*100/nbTriples)}%)")
    print(f"{len(results)} sentences realized")
    # uncomment the following to save results
    # outFilename = re.sub(r"^(.*?_).*", r"RDFpyrealb_\1en.txt", fileName)
    # outPath = path_to_corpus + "/" + outFilename
    # out = open(outPath,"w")
    # out.write("\n".join(results))
    # out.write("\n")
    # print(f"{len(results)} sentences written on {outPath}")

fileNames = ["D2T-1-CFA_WebNLG_CounterFactual.xml",
             "D2T-1-FA_WebNLG_Factual.xml",
             "D2T-1-FI_WebNLG_Fictional.xml",
             "D2T-2-CFA_Wikidata_CounterFactual.xml",
             "D2T-2-FA_Wikidata_Factual.xml",
             "D2T-2-FI_Wikidata_Fictional.xml"]

#  For checking that the number of realized sentences matches the number of entries
def checkOutputs():
    for fileName in fileNames:
        print(fileName)
        b=Benchmark()
        b.fill_benchmark([(path_to_corpus,fileName)])
        c = Counter()
        nb = len(b.entries)
        for entry in b.entries:
            c[int(entry.size)]+=1
        print("".join([f"{i}:{c[i]}:{c[i]*100/nb:.0f}% " for i in range(1,8)]),nb)
        outFilename = re.sub(r"^(.*?_).*",r"RDFpyrealb_\1en.txt",fileName)
        outPath = path_to_corpus + "/" + outFilename
        file = open(outPath, "r")
        nbLines = len(file.read().split("\n"))-1
        if (nb != nbLines):
            print(f"{nb} entries different from {nbLines}")
        else:
            print(f"{nb} entries same as number of lines")


if __name__ == '__main__':
    memoFileName = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                "data","dbPediaMemo-24.json"))
    loadDBpediaMemo(memoFileName)
    # process a single file
    process(path_to_corpus,"D2T-1-FA_WebNLG_Factual.xml",False)
    # process all files
    # for fileName in fileNames:
    #     process(path_to_corpus,fileName)
    # saveDBpediaMemo()
    # checkOutputs()
