# Text Generation from RDF triples
This demo shows how `pyrealb`  can used to generate sentences from RDF triples. 
It corresponds to our submission to the [WebNLG Challenge 2020](https://webnlg-challenge.loria.fr/challenge_2020/) 
in which the text realization was performed through an API 
that sent structures to a `jsRealB` server which returned the final text. 

[Our paper at the workshop](https://www.aclweb.org/anthology/2020.webnlg-1.16.pdf) describes the symbolic approach used for organizing the text. It also provides a critical review of the data and discusses the suitability of this competition results in a wider Natural Language Generation setting.

The source (especially `WebGenerate.py`) is simplified compared to our original submission: it does not compute any statistics on the corpus nor any automatic evaluation score. It focuses on the text generation process.

The data provided here is limited to two XML files with 6 and 7 triples for which the texts are more interesting.

## Source files
* `benchmark_reader.py` : reader of the XML data files downloaded from the GitHub
* `context.py` :  access to pyrealb functions
* dbPediaMemo.json
* `Graph.py` : create the graph of Node corresponding to a set of triples and realize it as a sentence
* `makeReference.py` : create the subdirectories `references` in the `train` and `dev` data directories
* `Node.py` : create a single Node corresponding to a URI used as a subject in RDF with all outgoing links with their objects 
* `Realize.py` : templates and functions for realization; this file can be launched by itself to exercise all templates with dummy subject and object
* `rqDBpedia.py` : send a request to DBPedia to check the gender of a subject or if a subject can be of a specific category
* `WebGenerate.py` : launch the realization process  

## Data files
* `[67]-triples` : a few XML files copied from `dev` corpus of the 2020 Web Challenge
* `dbPediaMemo.json` : saved results of previous requests done to DBpedia through `rqDBpedia.py`. This is especially useful now that it seems that DPpedia does not provide gender information anymore.