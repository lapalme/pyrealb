import markup, unicodedata, re, datetime
from markup import oneliner as e

from context import pyrealb
from pyrealb import *
from userinfos import *
import os

def removeAccent(s):
    return unicodedata.normalize('NFD',s.lower()).encode('ascii', 'ignore').decode("utf-8")

def makeId(s):return removeAccent(s).replace(" ","_")

def h2_fr(text,id_=None):page.h2(text,lang="fr",id=makeId(text) if id_ is None else id_)
def h2_en(text,id_=None):page.h2(text,lang="en",id=makeId(text) if id_ is None else id_)

titres=[
    {"fr":"Nom","en":"Name"},
    {"fr":"Représentation","en":"Representation"},
    {"fr":"Exemple","en":"Example"},
    {"fr":"Réalisation","en":"Realisation"}
]

# execute an assignment or evaluate an expression
def evaluate(s):
    m=re.match(r"(\w+)\s*=",s)
    if m is not None:
        exec(s,globals())
    else:
        exp=eval(s)
        if isinstance(exp,Constituent):
            return exp.realize()
        else:
            return str(exp)

## create a table from the information in userinfos.py and add it to the page 
def addTable(infos):
    for lang in ["fr","en"]:
        loadEn() if lang=="en" else loadFr()
        if infos[lang]!="":
            page.h3(infos[lang],lang=lang)
        page.table.open(lang=lang)
        page.tr("".join(e.th(t[lang]) for t in titres))
        for ex in infos["ex"]:
            if "pattern" in ex:
                if len(ex[lang][0])>0:
                    page.tr(
                        e.td(ex[lang][0],class_="description")+
                        e.td(ex["pattern"],class_="pattern")+
                        e.td(ex[lang][1],class_="example-"+lang)+
                        e.td(evaluate(ex[lang][1]),class_="realisation")
                    )
            else:
                page.tr(
                    e.td(ex[lang])+
                    e.td(ex["group"],colspan=3,class_="pattern"),
                    class_="groupe"
                )
        page.table.close()

## create pronoun tables 
options = { 
    "pe":[1,2,3],
    "g":["m","f"],
    "n":["s","p"],
    "ow":["s","p"],
    "tn":["","refl"],
    "c":["nom","acc","dat","refl"]
}

## create all possible options recursively
def makeOptions(opts):
    if not len(opts):return [""]
    first=opts[0]
    rest=makeOptions(opts[1:])
    out=[]
    for o in options[first]:
        res=f'.pe({o})' if first=="pe" else f'.{first}("{o}")'
        for r in rest:
            out.append(res+r)
    return out

def makeCell(const,terminal,options):
    exp=f'{const}("{terminal}")'+options
    page.td(e.span(eval(exp).realize(),class_="realisation")+
                e.br()+
                e.span(exp,class_="pattern"))

def ajouterTitres(titres):
    page.tr(e.th(titres))
    
def pronomsPersonnels(pro,opts,tnC):
    lOpts=len(opts)
    last=lOpts-1
    for i in range(0,lOpts):
        os=opts[i]
        exp=f'Pro("{pro}")'+os
        citation="on" if pro=="on" else eval(exp).realize()
        page.tr(class_="last" if i==last else "")
        makeCell("Pro",pro,os)
        for j in range(1,len(tnC)):
            makeCell("Pro",citation,tnC[j]+(".pe(1)" if lOpts>1 and i==0 else "")+
                                           ('.g("f")' if os=='.pe(1).g("f").n("s")' and pro=="me" else ""))
        page.tr.close()

def flexionsGenreNombre(const,singPlur,gns):
    for mot in singPlur:
        for j in range(1,4):
            page.tr(class_="last" if j==3 else "")
            exp=f'{const}("{mot}").pe({j})'
            citation=eval(exp).realize()
            makeCell(const,mot,f'.pe({j})')
            for k in range(1,len(gns)):
                makeCell(const,citation,(".pe(1)" if j==1 else "")+gns[k])

def tableauFrancais():
    loadFr()
    ## pronoms toniques
    page.table()
    page.tr(e.th(["lemme","tonique","tonique réfléchi",
            "clitique nominatif","clitique accusatif","clitique datif","clitique réfléchi"]))
    tnC=["",'.tn("")','.tn("refl")','.c("nom")','.c("acc")','.c("dat")','.c("refl")']
    pronomsPersonnels("moi", makeOptions(["g","n","pe"]),tnC)
    pronomsPersonnels("on",[""],tnC)
    page.table.close()
    
    page.p("""Le tableau suivant présente la forme obtenue au-dessus de la 
    spécification <span class="jsr">pyrealb</span>.""")
    
    page.table()
    page.tr(e.th(["lemme","masculin singulier","féminin singulier","masculin pluriel","féminin pluriel"]))
    flexionsGenreNombre("Pro",["mien","nôtre"],[""]+makeOptions(["n","g"]))
    page.table.close()
    
    page.p("""Les déterminants possessifs varient en genre et en nombre à partir de leur 
            forme de base comme le montre le tableau suivant.""")

    page.table()
    page.tr(e.th(["lemme","masculin singulier","féminin singulier","masculin pluriel","féminin pluriel"]))
    flexionsGenreNombre("D",["mon","notre"],[""]+makeOptions(["n","g"]))
    page.table.close()

def englishPossessiveDeterminers():
    genres=options["g"]+["n"]
    for o in ["s","p"]:
        for pe in range(1,4):
            opts=f'.pe({pe}).ow("{o}")'
            if pe==3 and o=="s":
                for g in genres:
                    opts+=f'.g("{g}")'
                    page.tr()
                    makeCell("D","my",opts)
                    page.tr.close()
            else:
                page.tr()
                makeCell("D","my",opts)
    
        
def englishTable():
    loadEn()
    page.table()
    page.tr(e.th(["lemma","tonic","tonic reflexive",
                "clitic nominative","clitic accusative","clitic dative","clitic genitive"]))
    tnC=["",'.tn("")','.tn("refl")','.c("nom")','.c("acc")','.c("dat")','.c("gen")']
    pronomsPersonnels("me",makeOptions(["pe","g","n"]),tnC)
    pronomsPersonnels("it",[""],tnC)
    page.table.close()
    
    page.p("""
Possessive determiners are specified by giving options for the number, the person, 
the gender (when at the third person) and also if the owner (<code>.ow(..)</code>) 
is singular or plural. The following table shows the realization above its 
pyrealb specification.""")
    page.table()
    page.tr(e.th("Possessive determiner"))
    englishPossessiveDeterminers()
    page.table.close()
#### start of HTML generation

page=markup.page()
page.init(title="pyrealb - Documentation",
          css="style.css",
          lang="",
          metainfo={"name":"viewport", 
                    "content":"width=device-width, initial-scale=1.0",
                    "charset":"UTF-8",
                    "date":str(datetime.datetime.now())},
          script=["https://code.jquery.com/jquery-latest.min.js","user.js"],
          footer="""Contact: <a href="mailto:lapalme@iro.umontreal.ca">Guy Lapalme</a> 
<a href="http://rali.iro.umontreal.ca">RALI</a>, Université de Montréal, CANADA. 2021."""
          )

# top menus
page.span.open(class_="dropdown",id="quicklinks")
page.span("Aller à ↓",lang="fr")
page.span("Goto ↓",lang="en")
page.span("",class_="dropdown-content")
page.span.close()

page.span("["+e.span("FR",lang="en")+e.span("EN",lang="fr")+"]",id="langSelect")

# start of page
page.h1(e.span("pyrealb",class_="jsr")+" (Version "+pyrealb_version+") Documentation")

page.p("""<span class="jsr">pyrealb</span> est un réalisateur de texte pour l'anglais et le français écrit en Python.
Des appels de fonctions Python, rappelant les notations de syntaxe en constituants ou en dépendences, 
créent une structure qui sera réalisée en appelant la fonction <code>str()</code>, souvent de façon implicite 
via la fonction <code>print</code>. 
<br/>Pour l'utiliser, une fois le package Python installé selon les 
<a href="https://github.com/lapalme/pyrealb" title="GitHub - lapalme/pyrealb: French and English text realisator">instructions 
données dans le répertoire GitHub</a>,
il suffit d'ajouter la ligne suivante à son programme.""",lang="fr")
page.p("""<span class="jsr">pyrealb</span> is a text realizer for French and English written in Python. 
Calls to Python functions, similar to the syntactic constituency or dependencies notations create a structure 
that can be realized with <code>str()</code> , most often implicitely within a <code>print</code> function.
<br/>Once installed according to 
<a href="https://github.com/lapalme/pyrealb" title="GitHub - lapalme/pyrealb: French and English text realisator">the 
instructions on the GitHub</a>, using it
is only a matter of adding the following line to the program.""",lang="en")
page.code("from pyrealb import *")
page.p("""
<span class="jsr">pyrealb</span> peut aussi être utilisé pour créer une page web comme celle-ci dans laquelle 
les exemples ont été réalisés par <span class="jsr">pyrealb</span>  lors de la création de la page.""",
lang="fr")
page.p("""<span class="jsr">pyrealb</span> can be used to build web pages such as this one in which all examples 
 were realized using
<span class="jsr">pyrealb</span> when the page was created.""",
lang="en")


h2_fr("Constituants");h2_en("Constituents")

addTable(terminalsSect)
addTable(syntagmesSect)

page.div("""
<p>Les accords <em>simples</em> sont effectués entre les constituants d'un syntagme. Un constituant est considéré comme la <i>tête</i> avec lequel les autres sont accordés. La <i>tête</i> est déterminée de la façon suivante:</p>
<ul>
    <li><code>NP</code>: le premier <code>N</code> ou <code>NP</code> en tenant compte de la modification possible par un <code>NO</code>, cet accord est propagé à une subordonnée interne au <code>NP</code>;</li>
    <li><code>AP</code>: le premier <code>A</code>;</li>
    <li><code>VP</code>: le premier <code>V</code>;le verbe est accordé avec le sujet (le premier <code>NP</code> ou <code>Pro</code> de la phrase englobante);</li>
    <li><code>S</code>, <code>SP</code>: accord avec le <em>sujet</em>, soit le premier <code>NP</code>, <code>N</code>, 
        <code>Pro</code> ou <code>CP</code>. Si le <code>Pro</code> est un pronom relatif, le <em>sujet</em> de la subordonnée est utilisé. Des tests spécifiques permettent d'accorder le verbe <code>être/be</code> ainsi que pour tenir compte des sujets coordonnés.</li>
</ul>
<p>Des options (section suivante) spécifiant le genre et le nombre l'emportent sur ces accords automatiques.</p>
""",lang="fr")

page.div("""
<p><em>Simple</em> agreements are dealt with between constituents of a phrase. A constituent is taken as the <i>head</i> with which others agree. The <i>head</i> is found as follows:</p>
<ul>
    <li><code>NP</code>: the first <code>N</code> or <code>NP</code> taking into account an eventual <code>NO</code>, this agreement is propagated to an internal subordinate phrase;</li>
    <li><code>AP</code>: the first <code>A</code>;</li>
    <li><code>VP</code>: the first <code>V</code>; the verb agrees with its subject (the first <code>NP</code> or <code>Pro</code> in the enclosing sentence);</li>
    <li><code>S</code>, <code>SP</code>: agrees with the <em>subject</em>, taken as the first <code>NP</code>, <code>N</code>, 
        <code>Pro</code> or <code>CP</code>. If the <code>Pro</code> is a relative pronoun, the <em>subject</em> of the subordinate is taken. Specific tests take into account the verbs <code>être/be</code> and the coordinate subjects.</li>
</ul>
<p>Options (next section) can override these automatic agreements.</p>
""",lang="en")

addTable(dependentsSect)
page.div("""
    <p>Le premier paramètre d'une dépendance est un terminal. Les autres paramètres doivent être d'autres 
    dépendances.</p> 

    <p><code>coord</code> regroupe des <strong>dépendances de même type</strong> coordonnées par la conjonction 
    donnée comme terminal. Les dépendents seront séparés par une virgule sauf les deux derniers qui seront séparés 
    par la conjonction. <code>coord</code> sans dépendent sera ignoré à la réalisation. <code>coord</code> avec un 
    seul dépendent apparaitra sans la conjonction.</p> 

    <p>Les accords <em>simples</em> sont effectués automatiquement entre les dépendents:</p>
    <ul>
        <li>Le verbe d'un <code>root</code> s'accorde en personne, en genre et en nombre avec le sujet indiqué par la dépendance <code>subj</code>. Ceci peut être un <code>N</code>, un <code>Pro</code> ou même des dépendents d'un <code>coord</code>. Les attributs et participes passés des verbes copules sont accordés avec leur sujet. Les participes passés des verbes conjugés avec avoir s'accordent avec leur complément d'objet direct s'ils sont placés avant le verbe. Un complément d'objet direct est le terminal d'un <code>comp</code> dont le terminal n'est pas un <code>P</code>.</li>
        <li>Le déterminant d'un <code>det</code> s'accorde en genre et en nombre avec son sujet, i.e. le terminal englobant.</li>
        <li>L'adjectif d'un <code>mod</code> s'accorde en genre et en nombre avec son sujet, i.e. le terminal englobant.</li>
    </ul>
""",lang="fr")

page.div("""
    <p>The first parameter of a dependency is a terminal. The other parameters must be dependents.</p> 

    <p><code>coord</code> combines <strong>dependencies of the same type</strong> coordinated by the conjunction given 
    as terminal. Dependencies will comma separated except for the last two that will be separated by the conjunction. 
    A  <code>coord</code> without dependent will not be realized. A <code>coord</code> with a single dependent will 
    be realized without the conjunction.</p> 
 
    <p>Simple agreements are realized between dependents:</p>
    <ul>
        <li>A verb agrees in person and number with a subject indicated by a <code>subj</code> dependency,. The subject can be a <code>N</code>, a <code>Pro</code> or dependents of a <code>coord</code>.</li>
        <li>The determiner of a <code>det</code> agrees in number with its determinee, i.e. its enclosing terminal.</li>
    </ul>
""",lang="en")

### Déclinaisons et conjugaisons 
h2_fr("Déclinaisons et conjugaisons","optionsFr");h2_en("Declension and conjugation", "optionsEn")
addTable(optionsSect)
page.p("""Perfect and  continuous tenses for verbs can obtained by setting the 
<a href="#sentType">sentence type</a> to <code>.typ({perf:true})</code> or <code>.typ({prog:true})</code> 
""",lang="en")

h2_fr("Pronoms");h2_en("Pronouns")
page.p("""
Les pronoms qui sont dans le lexique sont à la 1ère personne du singulier. Pour obtenir les autres, il faut
spécifier la personne, le nombre et éventuellement le genre. Ce mécanisme s'applique aussi pour les
pronoms <code>me</code> et <code>moi-même</code> et pour le déterminant <code>mon</code>.""",lang="fr")
page.p("""
Pronouns in the lexicon are at the first person singular. To get the other forms, the gender, the number and
the person must be specified. The same option mechanism can be used for the pronouns <code>mine</code> and 
<code>myself</code> and
for the determiner <code>my</code>.""",lang="en")
addTable(pronomsSect)

page.div(id="pronomsSect2")
page.h3("""<span lang="fr">Pronoms en modifiant la forme tonique</span>
            <span lang="en">Pronouns from the tonic form</span>""")
page.div(lang="fr")
page.div("""
    <ul>
        <li>la forme tonique <code>.tn(..)</code> avec comme paramètre 
            <ul>
                <li><code>""</code>: pour la forme tonique elle-même</li>
                <li><code>refl</code> pour obtenir la forme réflexive (terminant en
             <code>-même</code>)</li>
            </ul>
         </li>
        <li>la forme clitique <code>.c(..)</code> avec comme paramètre 
            <ul>
                <li><code>nom</code> pour la forme nominative</li>
                <li><code>acc</code> pour la forme accusative (complément d'objet direct)</li>
                <li><code>dat</code> pour la forme datif (complément d'objet indirect)</li>
                <li><code>refl</code> pour la forme réfléchie</li>
            </ul>
        </li>
    </ul>
    <p>Afin de rester compatible avec la méthode de spécification précédente, les formes clitiques 
    et toniques des pronoms doivent spécifier <code>.pe(1)</code> pour le pronom <code>moi</code>. 
    Il en est de même pour les pronoms possessifs <code>mien</code> et <code>nôtre</code> ainsi que pour les déterminants possessifs <code>mon</code> et <code>notre</code>.</p>
    <p>Le tableau suivant présente la forme obtenue au-dessus de la spécification 
    <span class="jsr">pyrealb</span>.</p>
""")
tableauFrancais()
page.div.close() # lang="fr"


page.div(lang="en")
page.div("""
   <ul>
       <li>tonic form <code>.tn(..)</code> with parameter
           <ul>
               <li><code>""</code>: for the tonic form itself</li>
               <li><code>refl</code> to get the reflexive form (ending with
                    <code>self</code>)</li>
           </ul>
        </li>
       <li>clitic form <code>.c(..)</code> with options:
           <ul>
               <li><code>nom</code> for the nominative</li>
               <li><code>acc</code> for the accusative (direct object)</li>
               <li><code>dat</code> for the dative (indirect object)</li>
               <li><code>gen</code> for the genitive (noun complement)</li>
           </ul>
       </li>
   </ul>
   <p>In order to stay compatible with the previous form of specification, when using tonic or clitic form,
      <code>pe(1)</code> must be specified for the pronoun <code>me</code>.</p>
   <p>The following table shows the realized form above the corresponding 
       <span class="jsr">pyrealb</span> expression.</p>
""")
englishTable()
page.div.close() # lang="en"

page.div.close() # id=pronomsSect2

h2_fr("Mise en forme");h2_en("Formatting")
page.p("""
Si l'ajout avant et/ou après un constituent correspond à un signe de ponctuation défini dans les règles, 
l'espacement approprié est ajouté avant et après le signe, sinon la chaîne est ajoutée telle quelle 
sans espacement.""",lang="fr")
page.p("""
If the content added before and/or a constituent is defined in the language rules, 
then the appropriate spacing is added before and after the punctuation sign, 
otherwise the content is added without spacing.""",lang="en")
addTable(formatSect)

h2_fr("Modification du syntagme nominal","modSN");h2_en("noun phrase modification","npMod")
addTable(nPmods)

## *** Modification du type de phrase ***
h2_fr("Modification du type de phrase","changeType");h2_en("Sentence type modification","typeChange")
page.p("""
Les phrases sont construites à la forme active, mais il est possible d'en modifier le type pour obtenir 
des phrases négatives, progressives, interrogatives ou passives.  Ces modifications sont de la 
forme <code>S(...).typ({...})</code> Il est possible de combiner plusieurs modifications en spécifiant 
plusieurs paires clés-valeurs dans l'objet paramètre de <code>type</code>. L'utilisation de contractions 
en anglais telles que <code>I'll</code> pour <code>I will</code> ou 
<code>can't</code> pour <code>cannot</code> peut aussi être spécifiée de cette manière, 
mais cet indicateur est ignoré en français.
""",lang="fr")
page.p("""
Sentences are built at the active voice, but their type can be modified in order to get negative, progressive, 
interrogative or passive sentences. These modifications are indicated by <code>S(...).typ({...})</code>. 
Modifications can be combined by specifying multiple key value pairs in the object which is the parameter 
of <code>type</code>. The use of contractions such as <code>I'll</code> for <code>I will</code> or 
<code>can't</code> for <code>cannot</code> can also be specified in this way. This flag is ignored in French.""",lang="en")
addTable(sentType)


####   *** Date ***
h2_fr("Date","dateFr");h2_en("Date","dateEn")
page.p("""
<code>DT</code> accepte en paramètre soit une date créée par une des fonctions de <code>datetime</code> ou 
une chaîne de caractères de la forme <code>AAAA-MM-JJ hh:mm:ss</code>. Lorsqu'appelé sans paramètre, 
on utilise <code>datetime.today()</code>.
""",lang="fr")
page.p("""
<code>DT</code> takes as parameter either a date créated by one of functions of <code>datetime</code> or a string 
corresponding to <code>YYYY-MM-DD hh:mm:ss</code>. When no parameter is given, <code>datetime.today()</code> is used.
""",lang="en")
addTable(dateCreation)
addTable(dateOption)

#### *** Nombres ***
h2_fr("Nombres");h2_en("Numbers")
page.p("""
On crée un nombre avec <code>NO(...)</code> dont le paramètre est soit un nombre entier ou réel ou une chaîne 
qui peut être analysée comme un nombre.""",lang="fr")
page.p("""
A number is created with <code>NO(...)</code> whose parameter is either a number (integer or real) or a string 
that can be parsed as a number. In English, numbers less than one hundred written in letters can also be used as input.""",
lang="en")
addTable(numberFormat)
addTable(numberAgreement)

#### *** Programmation ***
h2_fr("Programmation");h2_en("Programming")
page.h3("<code>.add(<em>element</em>,<em>position</em>)</code>")
page.p("""
Ajout d'un nouveau syntagme <code>element</code> comme enfant à un syntagme existant. Le paramètre entier 
<code>position</code> est facultatif et spécifie la position (à partir de 0) dans le syntagme. Par défaut, 
l'élément est ajouté à la fin.""",lang="fr")
page.p("""Add a pyrealb phrase <code>element</code> as a child of an existing phrase. The second optional parameter 
<code>position</code> is an integer that specifies its position (counting from 0). By default, 
the element is added as the last child.""",lang="en")
addTable(addUse)

page.h3("<code>.toSource()</code>")
page.p("""
Cette fonction retourne une version <em>chaîne</em> d'une expression <span class="jsr">pyrealb</span>, 
ceci peut être utile pour la mise au point d'une expression complexe. En passant 0 comme paramètre 
à ce fonction, on obtient une expression indentée qui fait ressortir la structure de l'expression.""",
lang="fr")
page.p("""
This function returns a <em>string</em> version of a  <span class="jsr">pyrealb</span> expression, this 
can be useful for debugging complex expressions. When 0 is given as parameter of this function, 
the string is on on multiple lines indented to highlight the underlying structure of the expression.""",
lang="en")

page.h3("<code>getLanguage()</code>")
page.p("""
Cette fonction retourne le langage courant de réalisation: <code>"fr"</code> pour le français et 
<code>"en"</code> pour l'anglais.""",lang="fr")
page.p("""
This function returns the current realization language: <code>"fr"</code> for French and <code>"en"</code> 
for English.""",lang="en")

page.h3("<code>loadEn(trace), loadFr(trace)</code>")
page.p("""
Ces fonctions indiquent la langue à utiliser pour les prochaines réalisations. Il est important d'en 
appeler au moins une avant de débuter la réalisation d'une phrase. Si le paramètre est <code>True</code> 
(<code>False</code> par défaut), 
un message apparaîtra sur la console à la fin du chargement du lexique et de règles du langage.
""",lang="fr")
page.p("""
These functions sets the current realization language; one of them should be called before starting 
the realization process. If the parameter is set to <code>True</code> (<code>False</code> by default),
a message is written on the console after the loading of the lexicon and language tables.""",lang="en")

page.h3("<i>Copie</i> d'une expression",lang="fr")
page.h3("Expression <i>copying</i>",lang="en")
page.p("""
Comme les options modifient un constituant pour toutes les utilisations subséquentes, il est souvent pratique 
de pouvoir garder la version originale pour la réutiliser et la modifier indépendamment.
La façon la plus simple de créer une copie d'une expression <code>exp</code> est d'en faire une fonction à l'aide 
de <code>lambda:exp</code>. L'appel à cette fonction <code>exp()</code> crée une nouvelle instance de l'expression à
chaque appel.  Cette approche permet aussi de <i>retarder</i> l'évaluation d'une expression 
jusqu'au moment où on en a besoin, par exemple une fois le langage approprié a été chargé. Un autre avantage 
d'une fonction est le fait que l'expression peut être paramétrisée.""",lang="fr")
page.p("""
As options modify a constituent for all following uses, it is often convenient to keep the original expression 
intact in order to be able to reuse it and modify it independently. 
The easiest way to create a copy of expression <code>exp</code> is to make a function of it by adding 
<code>lambda:</code> in front of it. <code>exp()</code> calls the function and creates a pyrealb instance of the 
expression at each call. This allows to <i>delay</i> the evaluation of the expression until it is needed, 
for example once the appropriate language has been loaded. It is also possible to create parameterized expressions.
""",lang="en")
addTable(functionUse)

#### *** Gestion des lexiques *** 
h2_fr("Gestion des lexiques");h2_en("Lexicon Management")
page.p("""
 <span class="jsr">pyrealb</span> 
intègre déjà deux lexiques assez détaillés: français (plus de 52 500 entrées) et anglais (plus de 33 900 entrées) 
qu'il est possible de consulter et de modifier à l'aide des fonctions suivantes. Lorsque <code>lang</code> (<code>"en"</code> 
ou <code>"fr"</code>) est spécifié, la fonction s'applique au lexique de cette langue, sinon au lexique courant, 
celui du dernier appel à <code>loadEn()</code> ou <code>loadFr()</code>.
""",lang="fr")
page.p("""
<span class="jsr">pyrealb</span> 
provides already two comprehensive lexicons: French (more than 52 500 entries) and English (more than 33 900 entries) 
that can be queried and modified with the following functions. When <code>lang</code> (<code>"en"</code> or 
<code>"fr"</code>) is specified, the function is applied to the lexicon of this language, otherwise it applies to 
the current lexicon, the one of the last call to <code>loadEn()</code> or <code>loadFr()</code>.
""",lang="en")

page.h3("<code>addToLexicon(lemma[,newInfos][,lang])</code>")
page.div("""
<p lang="fr"> 
 <code>lemma</code> est l'entrée de base et <code>newInfos</code> est
 l'information morphologique selon le format interne à <span
 class="jsr">pyrealb</span>: un objet indiquant le ou les catégories possibles
 et pour chaque catégorie, des propriétés et la table de déclinaison ou
 conjugaison correspondantes.
Par exemple, <code>addToLexicon("pyrealb",{"N":{"g":"m", "pe":3, "tab":"nI"})</code> ajoutera le mot 
<code>pyrealb</code> comme nom masculin invariable au lexique courant. 
Cette fonction peut aussi être appelée avec un seul paramètre qui est un objet dont la clé est le lemme. 
L'exemple précédent peut donc s'écrire: <code>addToLexicon({"pyrealb":{"N":{"g":"m", "pe":3, "tab": "nI"}})</code>. 
<ul>
<li>Si le lemme et la catégorie existent déjà dans le lexique, alors l'entrée pour cette catégorie est remplacée 
par <code>newInfos</code>. </li>
<li>Cette fonction retourne la nouvelle entrée modifié pour <code>lemma</code>.</li>
<li><a href="../data/lexiconFormat.html">Plus d'information (en anglais) sur le format des lexiques</a></li>
<li>Pour déterminer les informations à ajouter, le plus simple est de copier les informations d'un mot du 
lexique qui se conjugue ou se décline de la même façon. L'<a href="../IDE/index.html">IDE de pyrealb</a> 
permet de consulter les informations du lexique.</li>
<li>Pour enlever une entrée d'un lexique, il de mettre <code>newInfos</code> à <code>None</code>.</li>
</ul>
""",lang="fr")
page.div("""
<p> 
 <code>lemma</code> is the basic form and <code>newInfos</code> is the morphologic information according 
 to the internal  <span class="jsr">pyrealb</span> format: an object indicating one or many possible categories. 
 For each category, properties and declension or conjugation are given.
For example, <code>addToLexicon("pyrealb",{"N":{"g":"m", "pe":3, "tab":"nI"})</code> will add 
the <code>pyrealb</code> as a masculine invariable word. This function can also be called with a 
single parameter: an object whose key is the lemma. The previous example could also have been 
written: <code>addToLexicon({"pyrealb":{"N":{"g":"m", "pe":3, "tab":"nI"})</code>.
<ul>  
<li>If the lemma and category are already present in the lexicon, then the category of this entry is 
replaced by <code>newInfos</code>.</li>
<li>This function returns the modified lexicon entry for <code>lemma</code>.</li>
<li><a href="../data/lexiconFormat.html">More information about the lexicon format</a></li>
<li>In order to find the informations to add, the simplest way is to copy the lexicon information 
for a similar word already in the lexicon. 
The <a href="../IDE/index.html">pyrealb IDE</a> provides access to the lexicon information.
</li>
<li>To remove an entry, set <code>newInfos</code> to <code>None</code>.</li>
</ul>
""",lang="en")

page.h3("<code>getLemma(lemma[,lang])</code>")
page.p("""
Retourner les informations du lexique correspondant à <code>lemma</code>.""",lang="fr")
page.p("""
Return lexicon information to <code>lemma</code>. """,lang="en")

page.h3("<code>updateLexicon(newLexicon[,lang])</code>")
page.p("""
Fusionner les entrées de <code>newLexicon</code> avec le lexique spécifié. Ceci ajoutera les nouvelles entrées et 
remplacera les entrées existantes par celles du nouveau lexique. La fusion est effectuée au niveau des entrées, 
mais non des catégories.""",lang="fr")
page.p("""
Merge the entries of <code>newLexicon</code> with the specified lexicon. This adds the pyrealb entries and replaces 
the existing entries by the ones of the pyrealb lexicon. Merging is done at the entry level, not at the category level.""",lang="en")

page.h3("<code>getLanguage()</code>")
page.p("""
Retourne le langage de réalisation courant.""",lang="fr")
page.p("""
Returns the current lexicon.""",lang="en")

h2_fr("Sélection de variantes");h2_en("Variant selection")
page.p("""
La fonction <code>oneOf(e<sub>1</sub>,e<sub>2</sub>,...)</code> où <code>e<sub>i</sub></code> est est une valeur, 
choisit un <code>e<sub>i</sub></code> au hasard. En <code>pyrealb</code>, ces éléments sont souvent des 
constructeurs correspondant à des structures de phrases différentes. Si <code>e<sub>1</sub></code> est une 
liste alors la sélection est faite dans cette liste, en ignorant les autres paramètres.
""",lang="fr")
page.p("""
Pour éviter que tous les éléments soient évalués avant la sélection, il suffit de <em>fonctionaliser</em> 
l'expression en une fonction sans paramètre en la préfixant par <code>lambda:</code>. 
Une fois l'élément choisi, <code>oneOf</code> vérifie si la valeur est une fonction et 
si c'est le cas, il retourne le résultat de l'appel. Par exemple,
<code>ofOne(lambda:N("amour"),lambda:N("amitié"))</code> permet de choisir entre les deux noms sans évaluer 
les deux constructeurs. Dans ce cas, très simple, il aurait été aussi possible d'écrire 
<code>N(oneOf("amour","amitié"))</code>.""",lang="fr")
page.p("""
The function <code>oneOf(e<sub>1</sub>,e<sub>2</sub>,...)</code> where <code>e<sub>i</sub></code> is a value, 
selects randomly a <code>e<sub>i</sub></code>. In <code>pyrealb</code>, these elements are often constructors
corresponding to different phrase structures. If <code>e<sub>1</sub></code> is a list, the selection is performed 
within this list, ignoring other parameters.""",lang="en")
page.p("""
To avoid the evaluation of all elements before the selection, it is possible to <em>functionalize</em> a expression 
into a function with no formal parameter by prefixing it with <code>lambda:</code>. Once the element is selected, 
<code>oneOf</code> checks if the value is a function and, if it is so, it returns the value of the called function. 
For exemple,
<code>oneOf(lambda:V("love"),lambda:V("like"))</code> allows choosing between the two verbs without evaluating 
both constructors. In this simplistic case, this could have also been written as <code>V(oneOf("love","like"))</code>.""",
lang="en")

h2_fr("Traitement en JSON");h2_en("JSON processing")
page.p("""
Pour faciliter l'utilisation de <code>pyrealb</code> en sortie d'un système externe. 
Il est possible d'utiliser un format d'entrée JSON <a href="../data/jsRealB-jsonInput.html">
décrit dans ce document (en anglais)</a> où sont décrites deux API permettant 
d'appeler un serveur <i>node.js</i> <code>jsRealB</code> <a href="jsRealBfromPython.html">depuis un autre programme Python</a> ou Prolog. 
Il est également possible d"obtenir une expression JSON correspondant à une expression <code>pyrealb</code>.""",
lang="fr")
page.p("""
To simplify the use of <code>pyrealb</code> as output of an external system, a JSON input format has been defined. 
<a href="../data/jsRealB-jsonInput.html">It is described in this document.</a> in which two APIs are described 
for calling a <code>pyrealb</code> <i>node.js</i> server <a href="jsRealBfromPython.html">from another Python</a> or Prolog. 
It is also possible to obtain the JSON expression corresponding to a given <code>pyrealb</code> expression.""",
lang="en")

h2_fr("Informations sur la version");h2_en("Informations about the version")
page.h3("<code>pyrealb_version</code>")
page.p("""Indique le numéro de version de <code>pyrealb</code>.""",lang="fr")
page.p("""Gives the version number of <code>pyrealb</code>.""",lang="en")

page.h3("<code>pyrealb_dateCreated</code>")
page.p("""Indique la date de la création de la version courante de <code>pyrealb</code>.""",lang="fr")
page.p("""Gives the creation date of the current <code>pyrealb</code>.""",lang="en")

h2_fr("Relation avec <code>jsRealB</code>","relation_fr");h2_en("Relation with <code>jsRealB</code>","relation_en")
page.p("""
La version JavaScript de <code>jsRealB</code> en est déjà à sa 3e réécriture. 
Elle est le résultat de plusieurs années de développement initiées au RALI en 2015. Le choix de JavaScript avait été
motivé par le fait qu'on cherchait a produire du texte dans un contexte de pages web dynamiques. Plusieurs
systèmes ont ainsi été développés, comme en font foi les multiples démos.  Une version <code>node.js</code> permet
d'utiliser le réalisateur en lot, en dehors d'un navigateur pour exécuter le JavaScript.</p>

<p lang="fr">Python étant devenu au fil des années la <i>lingua franca</i> du traitement de la langue, une
interface Python a été développée afin d'écrire le traitement des données en Python. On crée ainsi
des structures de données en utilisant la même notation que celle utilisée en JavaScript. Ces 
structures sont ensuite sérialisées pour être envoyées à un serveur HTTP <code>node.js</code> qui en retourne 
la réalisation.</p>

<p lang="fr">Cette interface a permis de réaliser plusieurs systèmes, mais cette séparation en deux systèmes en complique 
l'installation. C'est pourquoi il a été décidé de porter le réalisateur en Python. La traduction a été faite
<i>à la main</i> en reprenant la même structure de code avec les mêmes noms de fonctions. Seule la gestion des
dates diffère grandement entre les deux versions. Cette traduction a donc forcé 
une relecture attentive du code JavaScript et, par le fait même, a permis de découvrir quelques erreurs
et maladresses qui ont été corrigées dans la version originale.
""",lang="fr")
page.p("""
The JavaScript version of <code>jsRealB</code> is already at its third rewriting. It is the result of many years 
of developments started at the RALI in 2015. JavaScript was chosen as implementation language because the goal was
to produce text in dynamic web pages. Many such systems have been developed as is shown in the many demos. 
A <code>node.js</code> version allows the realizer to be used in batch outside of a browser to execute the 
JavaScript.</p>

<p lang="en">Python being the <i>lingua franca</i> for natural language processing, a Python interface has
been developed so that the data processing can be done in Python. Python data structures are created using
the same notation used in the JavaScript version. These structures are then serialized to a 
<code>node.js</code> HTTP server which returns the realized text.</p>

<p lang="en">This interface was used in many systems, but this separation into two systems complicates installation.
This is why the realizer was ported to Python. The translation was done <i>manually</i>  by keeping the same
code structure and function names. Only the date implementation differs between the two versions. This translation
process forced a careful review of the original JavaScript code, and by the fact, allowed the discovery of a few
errors and awkwardnesses that were corrected in the original.

""",lang="en")


### *** Informations complémentaires ***
h2_fr("Informations complémentaires","plusDinfo");h2_en("More information","moreInfo")
page.ul("""
<li><a href="https://arxiv.org/pdf/2012.15425.pdf" lang="fr">Document décrivant l'organisation du 
système</a><a href="https://arxiv.org/pdf/2012.15425.pdf" lang="en">Document describing the organization 
of the system</a></li>
<li><a href="http://rali.iro.umontreal.ca/rali/?q=fr/jsrealb-realisateur-bilingue-de-texte" lang="fr">Historique 
des versions et démonstrations</a><a href="http://rali.iro.umontreal.ca/rali/?q=en/jsrealb-bilingual-text-realiser" 
lang="en">Previous versions and demos</a></li>
<li><a href="https://observablehq.com/@lapalme/nouvelles-experiences-avec-jsrealb" 
title="Nouvelles exp&#xE9;riences avec jsRealB / Guy Lapalme / Observable" lang="fr">Notebook Observable</a>
<a href="https://observablehq.com/@lapalme/exprimenting-with-jsrealb" title="Experimenting with jsRealB / Guy Lapalme / Observable" 
lang="en">Observable Notebook</a></li>
<li><a href="../IDE/README.html">Interactive Development Environment</a></li>
<li><a href="http://rali.iro.umontreal.ca/JSrealB/current/Tutorial/tutorial.html" title="jsRealB tutorial" 
lang="fr">Tutoriel (en anglais)</a><a href="http://rali.iro.umontreal.ca/JSrealB/current/Tutorial/tutorial.html" 
title="jsRealB tutorial" lang="en">Tutorial</a></li>
<li><a href="https://github.com/rali-udem/JSrealB" lang="fr">Dépot GitHub</a>
<a href="https://github.com/rali-udem/JSrealB" lang="en">GitHub repository</a></li>
<li><a href="../data/lexiconFormat.html" lang="fr">Format des entrées de lexiques (en anglais)</a>
<a href="../data/lexiconFormat.html" lang="en">Format of the lexicon entries</a></li>
<li>Publications:
    <ul>
        <li><a href="http://rali.iro.umontreal.ca/rali/sites/default/files/publis/JSrealB-ENGL2015.pdf">Demo paper at ENLG-2015</a></li>
        <li>Daoust, N., and G. Lapalme, <em>JSreal: A Text Realizer for Web Programming</em>, Language Production, Cognition, and the Lexicon - a Festschrift in honor of Michael Zock, Text, Speech and Language Technology, Vol 48: Springer, pp. 363-378, 2014. [<a href="http://rali.iro.umontreal.ca/rali/sites/default/files/publis/JSreal.pdf">PDF</a>]</li>
    </ul>
</li>
""")


### créer le fichier de sortie
outFileN=os.path.abspath(os.path.join(os.path.dirname(__file__),"documentation.html"))
outFile=open(outFileN,"w",encoding="utf-8")
print(page,file=outFile)
print(outFileN, "written")