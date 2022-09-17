# https://sparqlwrapper.readthedocs.io/en/stable/main.html#installation-distribution
from SPARQLWrapper import SPARQLWrapper, JSON,XML
import re

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setReturnFormat(JSON)

typeMemo={}
genderMemo={}
modified=False

# hack to correct a few bad URI of the form ...(xyz abc) -> ...(xyz) and then change spaces by underlines
def cleanURI(uri):
    m=re.match(r'(.*?\(\w+) (.*?)(\).*)',uri)
    if m!=None:
        return m.group(1)+m.group(3)
    return uri.replace(' ','_')

def sendQuery(query):
    global modified
    # print(query)
    modified=True
    try:
        sparql.setQuery(query)
        return sparql.query().convert()
    except Exception as e:
        print("Sparql Exception")
        print(e)
        return None

def isA(subject,category):
    subject=cleanURI(subject)
    category=cleanURI(category)
    sc=subject+"|"+category
    if sc in typeMemo:
        return typeMemo[sc]
    query="""ASK WHERE { <http://dbpedia.org/resource/%s> rdf:type <http://dbpedia.org/ontology/%s> }"""%(subject,category)
    results=sendQuery(query)
    if results==None: 
        typeMemo[sc]=False
        return False
    theType=results["boolean"]
    typeMemo[sc]=theType
    print("*SPARQL* isA(%s,%s):%s"%(subject,category,theType))
    return theType

## In september 2022, it seems that dbpedia.org has "removed" gender information....
## so we rely mainly on previous saved information in 2020 in dbPediamemo.json
def getGender(subject):
    subject=cleanURI(subject)
    if subject in genderMemo: 
        return genderMemo[subject]
    query="""SELECT ?gender
       WHERE { <http://dbpedia.org/resource/%s> <http://xmlns.com/foaf/0.1/gender> ?gender }"""%(subject)
    results=sendQuery(query)
    if results==None:
        genderMemo[subject]=None
        return None
    bindings=results["results"]["bindings"]
    gender=None if len(bindings)==0 else bindings[0]['gender']["value"]
    genderMemo[subject]=gender
    print("*SPARQL* getGender(%s):%s"%(subject,gender))
    return gender

import sys,json,os.path

memoFileName=os.path.abspath(os.path.join(os.path.dirname(__file__), "data/dbPediaMemo.json"))
[typeMemo,genderMemo]=json.load(open(memoFileName,"r",encoding="UTF-8"))
sys.stderr.write(memoFileName+" read\n")
