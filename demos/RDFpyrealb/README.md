# Text Generation from RDF triples
This demo shows how `pyrealb` can be used to generate sentences from RDF triples. 
## Overview of the approach
Given seven triples about the astronaut Buzz Aldrin, the goal is to create a text that 
will convey all their information content. 
The triples are shown with the _non-standard_ format used in the [WebNLG Challenge 2020](https://webnlg-challenge.loria.fr/challenge_2020/) competition, but it should be 
self-explanatory. An RDF triple is a line with three fields separated by a vertical bar: **subject**, **predicate** and **object**.

```
    Buzz_Aldrin | birthPlace | Glen_Ridge,_New_Jersey
    Buzz_Aldrin | mission | Apollo_11
    Buzz_Aldrin | selectedByNasa | 1963
    Buzz_Aldrin | occupation | Fighter_pilot
    Buzz_Aldrin | almaMater | "Massachusetts Institute of Technology, Sc.D. 1963"
    Apollo_11 | backupPilot | William_Anders
    Apollo_11 | operator | NASA
```
The output produced by program of this demo is:

    Buzz Aldrin was born in Glen Ridge, New Jersey, he graduated from Massachusetts Institute of Technology, Sc.D. 1963 
    and he joined NASA in 1963.  He became member of Apollo 11 and was a fighter pilot.  Apollo 11 included as back-up
    pilot William Anders and is operated by NASA. 

The first step after reading the triples is to create groups of triples sharing their subject. The above triples are 
divided into the following two groups (shown _à la_ [Turtle](https://www.w3.org/TR/turtle/)). Each group will be realized with one or more sentences.

```
Buzz_Aldrin
   birthPlace Glen_Ridge,_New_Jersey;
   almaMater "Massachusetts Institute of Technology, Sc.D. 1963";
   selectedByNasa 1963;
   mission Apollo_11;
   occupation Fighter_pilot.
Apollo_11
   backupPilot William_Anders;
   operator NASA.
```

Sentence patterns are associated with each predicate. There are about 200 of them, created _by hand_ from the most 
frequent 
predicates encountered in the training corpus. A pattern is a `lambda` expression with an object as parameter that 
returns a `VP`. More than one lambda can be associated with a predicate, one of which is chosen at random, this 
allows for variations in the realizations. 
In order to choose an appropriate pronoun, a flag indicates if this predicate is applied to a human subject or not. 
The numeric value in the [0..100] range is used to sort the predicates in the text. For example, 
the birth date and place should be presented before other achievements; death date should be 
presented last.  Here are a few examples of sentence patterns that can be applied to our example triples.

``` python
#### switch for precedence, isHuman, vp patterns
## precedence between 0 and 100 used for sorting predicates before realization
## isHuman : boolean indicating if this predicate applies to a human (useful for pronominalization)
sentencePatterns = {
    ...
    "almaMater":(20,True,[	
        lambda o:VP(V("graduate").t("ps"),PP(P("from"),o)) ,	
        lambda o:VP(V("be").t("ps"),V("award").t("pp"),NP(D("a"),N("degree")),PP(P("from"),o)) ,	
        lambda o:VP(V("earn").t("ps"),NP(D("a"),N("degree")),PP(P("from"),o)) ,	
    ]),	
    ....
    "birthPlace":(3,True,[	
        lambda o:VP(V("be").t("ps"),V("born").t("pp"),PP(P("in"),o)),	
    ]),	
    ....
    "selectedByNasa":(21,True,[	
        lambda o:VP(V("be").t("ps"),V(oneOf("choose","hire","select")).t("pp"),PP(P("by"),(Q("NASA"),PP(P("in"),o)))),	
        lambda o:VP(V("join").t("ps"),Q("NASA"),PP(P("in"),o)),	
    ]),	
}
```

To improve readability, sentences are limited to three predicates. So the subject is stated at the 
beginning and a 
coordinated sentence is created with the following patterns, using a pronoun as subject for the next part of a 
sentence. For 
example, the following `pyrealb` structure is created for the first sentence of the text. Note that the order of the 
predicates is slightly different from the one in the original data.

``` python
S(CP(C("and"),
     S(Q("Buzz Aldrin"),
       VP(V("be").t('ps'),
          V("born").t('pp'),
          PP(P("in"),
             Q("Glen Ridge, New Jersey")))),
     S(Pro("I").g('m'),
       VP(V("be").t('ps'),
          V("award").t('pp'),
          NP(D("a"),
             N("degree")),
          PP(P("from"),
             Q("Massachusetts Institute of Technology, Sc.D. 1963")))),
     S(Pro("I").g('m'),
       VP(V("join").t('ps'),
          Q("NASA"),
          PP(P("in"),
             Q("1963"))))))
```

## Context
This demo is derived from our submission to the [WebNLG Challenge 2020](https://webnlg-challenge.loria.fr/challenge_2020/) 
where the text realization was performed through an API 
that sent structures to a `jsRealB` server which returned the final text. Here realization is performed directly in 
Python.
[Our paper at the workshop](https://www.aclweb.org/anthology/2020.webnlg-1.16.pdf) describes the symbolic approach 
used for organizing the text. It also provides a critical review of the data and discusses the suitability of this 
competition results in a wider Natural Language Generation setting.

The source (especially `WebGenerate.py`) is simplified compared to our original submission: 
it does not compute any statistics on the corpus, and it does not provide any automatic evaluation scores. 
It focuses on the text generation process.

The data provided here is limited to two XML files with 6 and 7 triples. 

## Source files
* `benchmark_reader.py` : reader of the XML data files downloaded from the GitHub
* `context.py` :  access to pyrealb functions
* `Graph.py` : create the graph of Node corresponding to a set of triples and realize it as a sentence
* `makeReference.py` : create the subdirectories `references` in the `train` and `dev` data directories
* `Node.py` : create a single Node corresponding to a URI used as a subject in RDF with all outgoing links with their objects 
* `Realize.py` : templates and functions for realization; this file can be launched by itself to exercise all templates with dummy subject and object
* `rqDBpedia.py` : send a request to DBPedia to check the gender of a subject or if a subject can be of a specific category
* `WebGenerate.py` : launch the realization process  

## Data files
* `[67]-triples` : a few XML files copied from `dev` corpus of the [WebNLG Challenge 2020](https://webnlg-challenge.loria.fr/challenge_2020/)
* `dbPediaMemo.json` : saved results of previous requests done to DBpedia through `rqDBpedia.py`. This is especially 
  useful because DBpedia does not provide gender information anymore.

Contact: [Guy Lapalme](mailto:lapalme@iro.umontreal.ca)
