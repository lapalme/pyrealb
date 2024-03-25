# Text Generation from RDF triples
This demo shows how `pyrealb` can be used to generate English and French sentences from RDF triples. 
## Problem definition
Given a set of triples, the goal is to create an English or French text that conveys their information content. The triples are given with the _non-standard_ format originally defined for the [WebNLG Challenge 2020](https://webnlg-challenge.loria.fr/challenge_2020/) competition. An RDF triple is a line with three fields separated by a vertical bar: *subject*, *predicate* and *object*. A predicate indicates a relation between the subject and the object. 

The following is a set of 7 triples about an astronaut.  The first triple indicates that *Buzz Aldrin* was born in *Glen Ridge, New Jersey*.

```
    Buzz_Aldrin | birthPlace | Glen_Ridge,_New_Jersey
    Buzz_Aldrin | mission | Apollo_11
    Buzz_Aldrin | selectedByNasa | 1963
    Buzz_Aldrin | occupation | Fighter_pilot
    Buzz_Aldrin | almaMater | "Massachusetts Institute of Technology, Sc.D. 1963"
    Apollo_11 | backupPilot | William_Anders
    Apollo_11 | operator | NASA
```
The English and French texts produced by this demo are:

> Buzz Aldrin was born in Glen Ridge, New Jersey, he graduated from Massachusetts Institute of Technology, Sc.D. 1963 and was selected by NASA in 1963.  He became member of Apollo 11 and was a fighter pilot.  Apollo 11 included as back-up pilot William Anders and is operated by NASA.

> Buzz Aldrin est né à Glen Ridge, New Jersey, il a terminé ses études à Massachusetts Institute of Technology, Sc.D. 1963 et a été choisi par NASA en 1963.  Il a été un membre de l'équipe d'Apollo 11 et a été un fighter pilot.  Apollo 11 a compté William Anders comme pilote de réserve et est opéré par NASA.

Both texts are strictly parallel because the they use the same text organization algorithm, only the final language specific realization being different. French output is sometimes a bit awkward because the subject and objects are English words that are most often realized verbatim (e.g. *fighter pilot* above). 

In the following, we only describe the English realization as the French one is most often identical except for the choice of words. Once words have been chosen, the realized text is usually well-formed.  

## Text organization

Merely realizing each triple would lead to a text that would be difficult (and boring) to read. So the first step after reading the triples is to create groups of triples sharing their subject.The above triples are divided into the following two groups (shown _à la_ [Turtle](https://www.w3.org/TR/turtle/)). Each group will be realized with one or more sentences. Within a group, triples are sorted  in *chronological* order: in our example, birth occurs first, then studies and finally the job at NASA. 

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

Sentence patterns are associated with each predicate. There are about 225 associations, created _by hand_ from the most frequent predicates encountered in the training corpus (i.e. those that occurred more than 20 times). Each association is a 3-tuple:

- A numeric value in the [0..100] range is used to sort the predicates in the text. For example, the birth date and place should be presented before other achievements; death date should be presented last.  Here are a few examples of sentence patterns that can be applied to our example triples.
- A boolean flag  that indicates if this predicate is applied to a human subject or not. This is used to choose an appropriate pronoun when sentences are combined.
- A list of sentence patterns each of which is a `lambda` expression with an object as parameter that returns a `VP`. If more than many lambdas are associated with a predicate, one is chosen at random, to allow for variations in the realizations. 

``` python
#### switch for precedence, isHuman, vp patterns
## precedence between 0 and 100 used for sorting predicates before realization
## isHuman : boolean indicating if this predicate applies to a human (useful for pronominalization)
sentencePatterns = {
    ...
    "almaMater":(20,True,[	
        lambda o:VP(V("graduate").t("ps"),PP(P("from"),o)) ,	
        lambda o:VP(V("be").t("ps"),V("award").t("pp"),NP(D("a"),N("degree")),
                    PP(P("from"),o)) ,	
        lambda o:VP(V("earn").t("ps"),NP(D("a"),N("degree")),PP(P("from"),o)) ,	
    ]),	
    ....
    "birthPlace":(3,True,[	
        lambda o:VP(V("be").t("ps"),V("born").t("pp"),PP(P("in"),o)),	
    ]),	
    ....
    "selectedByNasa":(21,True,[	
        lambda o:VP(V("be").t("ps"),V(oneOf("choose","hire","select")).t("pp"),
                    PP(P("by"),(Q("NASA"),PP(P("in"),o)))),	
        lambda o:VP(V("join").t("ps"),Q("NASA"),PP(P("in"),o)),	
    ]),	
}
```

To improve readability, sentences are limited to three predicates included in coordinated phrase. The subject is stated at the beginning and a coordinated sentence is created using a pronoun as subject for the next part of a sentence. For example, the following `pyrealb` structure is created for the first sentence of the text. Note that the order of the predicates is slightly different from the one in the original data.

``` python
S(CP(C("and"),
     S(Q("Buzz Aldrin"),
       VP(V("be").t('ps'),
          V("born").t('pp'),
          PP(P("in"),
             Q("Glen Ridge, New Jersey")))),
     S(Pro("I").g('m'),
       VP(V("graduate").t('ps'),
          PP(P("from"),
             Q("Massachusetts Institute of Technology, Sc.D. 1963")))),
     S(Q(""),
       VP(V("be").t('ps'),
          V("select").t('pp'),
          PP(P("by"),
             Q("NASA"),
             P("in"),
             Q("1963"))))))
```

## Program organization
This demo is derived from our submission to the [WebNLG Challenge 2020](https://webnlg-challenge.loria.fr/challenge_2020/) where the text realization was performed through an API that sent structures to a `jsRealB` server which returned the final text. Here realization is performed directly in Python. [Our paper at the workshop](https://www.aclweb.org/anthology/2020.webnlg-1.16.pdf) describes the symbolic approach used for organizing the text. It also provides a critical review of the data and discusses the suitability of this competition results in a wider Natural Language Generation setting.

The source (especially `WebGenerate.py`) is simplified compared to our original submission: it does not compute any statistics on the corpus, and it does not provide any automatic evaluation scores. It focuses on the text generation process. 

But in this version, more sentence patterns have been added. The most important difference being the fact that triples can also be realized in French.  The system clearly separates the English and French realization using the [bilingual data-to-text generation organization described in this document](https://arxiv.org/pdf/2311.14808.pdf): the `Realizer` class does the overall text organization in a language independent way and the its subclasses `English` and `Francais` deals with the language specific aspects. 

The data provided here is limited to two XML files with 6 and 7 triples because they allow the realization of more interesting texts than those with fewer triples. The files can be read using function `load_benchmark_from_files`  defined in `WebGenerate.py`.

 WebNLG data is also available as a  [HuggingFace dataset](https://huggingface.co/datasets/web_nlg)  loaded using `load_benchmark_from_dataset`  defined  in `WebGenerate.py`.

## Source files
* `benchmark_reader.py` : reader of the XML data files and from the HuggingFace dataset, adapted from the version originally downloaded from the WebNLG 2020 GitHub
* `English.py` : English specific realizer code
* `Francais.py` : French specific realizer code
* `Graph.py` : create the graph of Node corresponding to a set of triples and realize it as a sentence
* `Node.py` : create a single Node corresponding to a URI used as a subject in RDF with all outgoing links with their objects 
* `Realizer.py` : language independent templates and functions for realization; this file can be launched by itself to 
  exercise all templates with dummy subject and object
* `rqDBpedia.py` : send a request to DBPedia to check the gender of a subject or if a subject can be of a specific category
* `WebGenerate.py` : launch the realization process  

## Data files
* `[67]-triples` : a few XML files copied from `dev` corpus of the [WebNLG Challenge 2020](https://webnlg-challenge.loria.fr/challenge_2020/)
* `dbPediaMemo.json` : saved results of previous requests done to DBpedia through `rqDBpedia.py`. This is especially useful because DBpedia does not provide gender information anymore.

Contact: [Guy Lapalme](mailto:lapalme@iro.umontreal.ca)
