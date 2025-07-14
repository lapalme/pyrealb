import markup, unicodedata, re, datetime
from markup import oneliner as e
import os, sys
# s'assurer d'utiliser la version courante de pyrealb...
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..','src')))

from pyrealb import *
from userinfos import *

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
        load(lang)
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
now = datetime.datetime.now()
page=markup.page()
page.init(title="pyrealb - Documentation",
          css="style.css",
          lang="",
          charset="UTF-8",
          metainfo={"name":"viewport",
                    "content":"width=device-width, initial-scale=1.0",
                    "date":str(now.strftime("%Y-%m-%d  %H:%M:%S"))},
          script=["https://code.jquery.com/jquery-latest.min.js","user.js"],
          footer=f"""Contact: <a href="mailto:lapalme@iro.umontreal.ca">Guy Lapalme</a> 
<a href="http://rali.iro.umontreal.ca">RALI</a>, Université de Montréal, CANADA. {now.strftime("%Y")}.<br/><hr/>
{now.strftime("%Y-%m-%d  %H:%M:%S")}
"""
          )

# top menus
page.span.open(class_="dropdown",id="quicklinks")
page.span("Aller à ↓",lang="fr")
page.span("Goto ↓",lang="en")
page.span("",class_="dropdown-content")
page.span.close()

page.span("["+e.span("FR",lang="en")+e.span("EN",lang="fr")+"]",id="langSelect")

# start of page
page.h1(e.span("pyrealb",class_="jsr")+ " Documentation"+ e.span(" (Version "+pyrealb_version+")",
        style="font-size:70%; font-weight:normal"))

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
load("fr")
page.p(f"""
<span class="jsr">pyrealb</span> peut aussi être utilisé pour créer une page web comme celle-ci dans laquelle 
les exemples ont été réalisés par <span class="jsr">pyrealb</span>  lors de la création de la page,  
{evaluate('DT().dOpt({"day":False,"hour":False,"minute":False,"second":False})')}.""",
lang="fr")
load("en")
page.p(f"""<span class="jsr">pyrealb</span> can be used to build web pages such as this one in which all examples 
 were realized using
<span class="jsr">pyrealb</span> when the page was created, 
{evaluate('DT().dOpt({"day":False,"hour":False,"minute":False,"second":False})')}.""",
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
<p>Des options (section suivante) appliquées à une instance de <code>Terminal</code> (e.g. <code>N</code>, <code>V</code>, ...) spécifiant le genre et le nombre l'emportent sur ces accords automatiques.</p>
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
<p>Options (next section) applied to an instance of <code>Terminal</code> (e.g. <code>N</code>, <code>V</code>, ...) override these automatic agreements.</p>
""",lang="en")

addTable(dependentsSect)
page.div("""
    <p>Le premier paramètre d'une dépendance est un terminal, il doit toujours être spécifié à la création de la dépendance. Les autres paramètres sont optionnels, mais ils doivent être d'autres dépendances..</p> 

    <p><code>coord</code> regroupe des <strong>dépendances de même type</strong> coordonnées par la conjonction 
    donnée comme terminal. Les dépendents seront séparés par une virgule sauf les deux derniers qui seront séparés 
    par la conjonction. <code>coord</code> sans dépendent sera ignoré à la réalisation. <code>coord</code> avec un 
    seul dépendent apparaitra sans la conjonction. Si le terminal est une chaîne vide, alors tous les éléments seront 
    séparés par une virgule.</p> 

    <p>Les accords <em>simples</em> sont effectués automatiquement entre les dépendents:</p>
    <ul>
        <li>Le verbe d'un <code>root</code> s'accorde en personne, en genre et en nombre avec le sujet indiqué par la dépendance <code>subj</code>. Ceci peut être un <code>N</code>, un <code>Pro</code> ou même des dépendents d'un <code>coord</code>. Les attributs et participes passés des verbes copules sont accordés avec leur sujet. Les participes passés des verbes conjugés avec avoir s'accordent avec leur complément d'objet direct s'ils sont placés avant le verbe. Un complément d'objet direct est le terminal d'un <code>comp</code> dont le terminal n'est pas un <code>P</code>.</li>
        <li>Le déterminant d'un <code>det</code> s'accorde en genre et en nombre avec son sujet, i.e. le terminal englobant.</li>
        <li>L'adjectif d'un <code>mod</code> s'accorde en genre et en nombre avec son sujet, i.e. le terminal englobant.</li>
    </ul>
    <p>Position des dépendents: <code>det</code> et <code>subj</code> sont réalisées avant le terminal, alors que 
       <code>mod</code>, <code>comp</code> et <code>coord</code> sont réalisées dans l'ordre où
       elles sont spécifiées. Il est possible de modifier cet ordre en utilisant la méthode <code>.mod("pre")</code> pour 
        forcer une dépendance à apparaître avant, ou <code>.mod("post")</code> pour apparaître après.</p>

""",lang="fr")

page.div("""
    <p>The first parameter of a dependency is a terminal that must be specified when the dependency is created. The other parameters are optional, but they must be dependents.</p> 

    <p><code>coord</code> combines <strong>dependencies of the same type</strong> coordinated by the conjunction given 
    as terminal. Dependencies will comma separated except for the last two that will be separated by the conjunction. 
    A  <code>coord</code> without dependent will not be realized. A <code>coord</code> with a single dependent will 
    be realized without the conjunction. If the terminal is an empty string, then all dependents will be comma separated.</p> 
 
    <p>Simple agreements are realized between dependents:</p>
    <ul>
        <li>A verb agrees in person and number with a subject indicated by a <code>subj</code> dependency,. The subject can be a <code>N</code>, a <code>Pro</code> or dependents of a <code>coord</code>.</li>
        <li>The determiner of a <code>det</code> agrees in number with its determinee, i.e. its enclosing terminal.</li>
    </ul>
    <p>Dependent position: <code>det</code> et <code>subj</code> are realized before the terminal, while
        <code>mod</code>, <code>comp</code> et <code>coord</code> are realized after in the order of their specification. 
        This ordering can be changed using <code>.mod("pre")</code> to force a dependent to be realized before, or 
        <code>.mod("post")</code> to be realized after.
    </p>

""",lang="en")

### Déclinaisons et conjugaisons 
h2_fr("Déclinaisons et conjugaisons","optionsFr");h2_en("Declension and conjugation", "optionsEn")
addTable(optionsSect)
page.p("""Perfect and  continuous tenses for verbs can obtained by setting the 
<a href="#typeChange">sentence type</a> to <code>.typ({perf:true})</code> or <code>.typ({prog:true})</code> 
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
page.p("""Précisions pour le Markdown: le niveau de titre dépend du nombre de <code>#</code>; 
les listes à puces sont obtenues avec <code>.md("+")</code>, les listes ordonnées, 
avec <code>.md("1.")</code> ou tout autre nombre entier suivi d'un point; 
un <i>autolink</i> est créé avec <code>.md("<")</code>; une ligne horizontale avec 
<code>.md("---")</code> et un <i>blockquote</i> avec <code>.md(">")</code>""",lang="fr")
page.p("""Remarks for Markdown: the header level is given by the number of <code>#</code>; 
bulleted lists are created with <code>.md("+")</code>, ordered lists with <code>.md("1.")</code> 
or any other integer followed by a period; an <i>autolink</i> is created with <code>.md("<")</code>; 
an horizontal rule is obtained with <code>.md("---")</code> and a <i>blockquote</i> 
with <code>.md(">")</code>""",lang="en")

h2_fr("Position et pronominalization","modSN");h2_en("Position and pronominalization","npMod")
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
that can be parsed as a number.""",
lang="en")
addTable(numberFormat)
addTable(numberAgreement)

#### *** Programmation ***
h2_fr("Programmation");h2_en("Programming")
page.h3("<code>.add(<em>constituent</em>,<em>position</em>)</code>")
page.p("""
Ajout d'un nouveau <code>constituant</code> comme enfant à une <code>Phrase</code> ou <code>Dependent</code> 
existant. Le paramètre entier 
<code>position</code> est facultatif et spécifie la position (à partir de 0) dans le syntagme. Par défaut, 
l'élément est ajouté à la fin.""",lang="fr")
page.p("""Add a pyrealb <code>Phrase</code> or <code>Dependent</code> <code>element</code> as a child of 
an existing <code>Phrase</code> or <code>Dependent</code>. The second optional parameter 
<code>position</code> is an integer that specifies its position (counting from 0). By default, 
the element is added as the last child.""",lang="en")
addTable(addUse)

page.h3("<code>.remove(<em>position</em>)</code>")
page.p("""
Suppression du constituant à la position spécifiée en comptant à partir de 0.
""",lang="fr")
page.p("""
Remove the constituent at the given position starting from 0. 
""",lang="en")

page.h3("<code>.nbConstituents()</code>")
page.p("""
Retourne le nombre de constituents de la <code>Phrase</code> ou <code>Dependent</code> actuel.
""",lang="fr")
page.p("""
Returns the number of constituents in the current <code>Phrase</code> or <code>Dependent</code>
""",lang="en")

page.h3("<code>.constituents()</code>")
page.p("""
Retourne la liste de constituents de la <code>Phrase</code> ou <code>Dependent</code> actuel.
""",lang="fr")
page.p("""
Returns the list of constituents in the current <code>Phrase</code> or <code>Dependent</code>
""",lang="en")


page.h3("<code>.toSource(indent=-1)</code>")
page.p("""
Cette fonction retourne une version <em>chaîne</em> d'une expression <span class="jsr">pyrealb</span>, 
ceci peut être utile pour la mise au point d'une expression complexe. En passant un nombre positif ou nul (souvent 0) 
comme paramètre, on obtient une expression indentée qui fait ressortir la structure de l'expression.""",
lang="fr")
page.p("""
This function returns a <em>string</em> version of a  <span class="jsr">pyrealb</span> expression, this 
can be useful for debugging complex expressions. When a non negative number (often 0) is given as parameter, 
the string is indented on multiple lines to highlight the structure of the expression.""",
lang="en")

page.h3("<code>Constituent</code> realization",lang="en")
page.h3("Réalisation d'un <code>Constituent</code>",lang="fr")
page.dl("""
<dt><code>str(...)</code></dt>
<dd>Lancer la reéalisation d'un constituent qui dans certains cas modifie la structure d'un ou plusieurs autres constituents.
Dans la majorité des cas, la réalisation est obtenue avec <code>str( )</code> appelé implicitement par <code>print(..)</code>.</dd>
<dt><code>.realize()</code></dt>
<dd>La réalisation peut aussi être lancée explicitement avec la méthode <code>realize()</code>. 
Ceci est pratique lors du déboguage dans certains environnement de programation 
(p.ex. Visual Studio Code ou PyCharm) qui utilisent <code>str(..)</code> pour afficher des valeurs internes pouvant ainsi
changer la structure des constituents au cours de la mise au point, un cas typique de <i>Heisenbug</i>. 
Dans la majorité des cas, <span class="jsr">pyrealb</span> détecte automatiquement l'exécution dans le cadre d'un environnement 
de mise au point Python, et change le comportement de <code>str(..)</code> 
pour qu'il retourne plutôt le source de l'expression (voir <code>.toSource()</code> plus haut) 
ce qui, à l'usage, s'est avéré être très pratique. 
La réalisation doit alors être obtenue en appelant <code>.realize()</code>.
Pour obtenir ce comportement dans tous les cas, on peut utiliser cette affectation <code>Constituent.debug=True</code>.</dd>
<dt><code>+</code> (opérateur préfixe unaire)</dt>
<dd>L'opérateur unaire <code>+</code> peut être utilisé devant un <code>Constituent</code> 
pour imprimer sa réalisation; cette abréviation est surtout utile lors de tests dans une boucle <i>real-eval-print</i>.<dd>
""",lang="fr")
page.dl("""
<dt><code>str(...)</code></dt>
<dd>Launch the realization of a constituent which in some cases modifies the structure of one or more constituents. 
In the majority of cases, realization is obtained with <code>str( )</code> called implicitely by <code>print(..)</code></dd>
<dt><code>.realize()</code></dt>
<dd>Realization can also be launched explicitly with the <code>realize()</code> method.
This is useful when debugging in some programming environments 
(e.g. Visual Studio Code or PyCharm) in which <code>str(..)</code> is used for displaying internal values and thus risk changing 
the constituents during debugging, a typical case of <i>Heisenbug</i>. 
In most cases <span class="jsr">pyrealb</span> detects its execution within a Python debugger and changes
<code>str(..)</code> to return the source of the constituent (see <code>.toSource()</code> above). 
Realization must then be obtained by calling <code>.realize()</code>.
This behavior can be obtained in all cases with the following assignment <code>Constituent.debug=True</code>.</dd>
<dt><code>+</code> (unary prefix operator)</dt>
<dd>The unary <code>+</code> operator can be used in front of a <code>Constituent</code> to print its realization, a useful abbreviation
when testing within a <i>read-eval-print</i> loop.</dd>
""",lang="en")

page.h3("<code>getLanguage()</code>")
page.p("""
Cette fonction retourne le langage courant de réalisation: <code>"fr"</code> pour le français et 
<code>"en"</code> pour l'anglais.""",lang="fr")
page.p("""
This function returns the current realization language: <code>"fr"</code> for French and <code>"en"</code> 
for English.""",lang="en")

page.h3("<code>loadEn(trace), loadFr(trace), load(lang,trace)</code>")
page.p("""
Ces fonctions indiquent la langue à utiliser pour les prochaines réalisations. Il est important d'en appeler au mo«ins
 une avant de débuter la réalisation d'une phrase; <code>lang</code> doit être <code>"en"</code> ou <code>"fr"</code>. 
 Si le paramètre <code>trace</code> est <code>true</code>, (il est <code>false</code> par défaut) un message apparaîtra 
 sur la console à la fin du chargement du lexique et de règles du langage.
""",lang="fr")
page.p("""
These functions sets the current realization language; one of them should be called before starting the realization 
process;  <code>lang</code> must be <code>"en"</code> or <code>"fr"</code>. If the parameter <code>trace</code> 
is <code>true</code>, (it is <code>false</code> by default), a message is written on the console after the loading 
of the lexicon and language rules.
""",lang="en")

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
<code>lambda:</code> in front of it. <code>exp()</code> calls the function and creates a <span class="jsr">pyrealb</span> instance of the 
expression at each call. This allows to <i>delay</i> the evaluation of the expression until it is needed, 
for example once the appropriate language has been loaded. It is also possible to create parameterized expressions.
""",lang="en")
addTable(functionUse)

page.p("""
<b><a href="./Hacking-pyrealb.html">Ce document (en anglais)</a> donne plus de détails sur la modification dynamique de 
constituents en pyrealb.</b>
""",lang="fr")

page.p("""
<b><a href="./Hacking-pyrealb.html">This document</a> gives more details on the dynamic constituent structure modification 
 with pyrealb.</b>
""",lang="en")

#### *** Gestion des lexiques *** 
h2_fr("Gestion des lexiques");h2_en("Lexicon Management")
page.p("""
 <span class="jsr">pyrealb</span> 
intègre déjà deux lexiques assez détaillés: français (plus de 52 500 entrées) et anglais (plus de 34 200 entrées) 
qu'il est possible de consulter et de modifier à l'aide des fonctions suivantes. Lorsque <code>lang</code> (<code>"en"</code> 
ou <code>"fr"</code>) est spécifié, la fonction s'applique au lexique de cette langue, sinon au lexique courant, 
celui du dernier appel à <code>loadEn()</code>, <code>loadFr()</code> ou <code>load()</code>.<br>
<a href="Lexicon-Format-fr.html">Plus d'information sur le format du lexique français.</a>
""",lang="fr")
page.p("""
<span class="jsr">pyrealb</span> 
provides already two comprehensive lexicons: French (more than 52 500 entries) and English (more than 34 200 entries) 
that can be queried and modified with the following functions. When <code>lang</code> (<code>"en"</code> or 
<code>"fr"</code>) is specified, the function is applied to the lexicon of this language, otherwise it applies to 
the current lexicon, the one of the last call to <code>loadEn()</code>, <code>loadFr()</code> or <code>load()</code>.<br>
<a href="Lexicon-Format-en.html">More information about the English lexicon format.</a>
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
<li>Pour déterminer les informations à ajouter, le plus simple est de copier les informations d'un mot du 
lexique qui se conjugue ou se décline de la même façon. L'<i>IDE</i> de <span class="jsr">pyrealb</span> 
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
<li>In order to find the informations to add, the simplest way is to copy the lexicon information 
for a similar word already in the lexicon. 
The <i>IDE</i> provides access to the lexicon information.
</li>
<li>To remove an entry, set <code>newInfos</code> to <code>None</code>.</li>
</ul>
""",lang="en")

page.h3("<code>getLemma(lemma[,lang])</code>")
page.p("""
Retourner les informations du lexique correspondant à <code>lemma</code>.""",lang="fr")
page.p("""
Return lexicon information to <code>lemma</code>. """,lang="en")

page.h3("<code>getLanguage()</code>")
page.p("Retourne le langage de réalisation courant.",lang="fr")
page.p("Returns the current realization language",lang="en")

page.h3("<code>getLexicon()</code>")
page.p("Retourne le lexique courant.",lang="fr")
page.p("Returns the current lexicon.",lang="en")

page.h3("<code>updateLexicon(newLexicon[,lang])</code>")
page.p("""
Fusionner les entrées de <code>newLexicon</code> avec le lexique spécifié. Ceci ajoutera les nouvelles entrées et 
remplacera les entrées existantes par celles du nouveau lexique. La fusion est effectuée au niveau des entrées, 
mais non des catégories.""",lang="fr")
page.p("""
Merge the entries of <code>newLexicon</code> with the specified lexicon. This adds the <span class="jsr">pyrealb</span> entries and replaces 
the existing entries by the ones of the <span class="jsr">pyrealb</span> lexicon. Merging is done at the entry level, not at the category level.""",lang="en")

page.h3("<code>buildLemmataMap(lang)</code>")
page.p("""Créer une table dans laquelle chaque clé est une des formes déclinées ou conjuguées 
de tous les mots du lexique de la langue spécifiée. La valeur associée à une liste d'instances de 
<code>Terminal</code> qui sont réalisées par la clé.
""",lang="fr")
page.p("""Cette table peut être utilisée pour de la génération <i>inverse</i>. Voici quelques appels suivis des résultats après &rArr;
<pre lang="fr"><code>    lemmataFr = buildLemmataMap("fr")
    print(", ".join(e.toSource() for e in lemmataFr["finies"])) &rArr; <i>A("fini").g('f').n('p'), V("finir").t('pp').g('f').n('p')</i>
    print(", ".join(e.toSource() for e in lemmataFr["crus"] if e.isA("N"))) &rArr; <i>N('cru').n("p")</i>
</code></pre>
""",lang="fr")
page.p("""Build a dict in which each key is an inflected form of all the entries in the lexicon of the specified language. 
The associated value is a list of <code>Terminal</code> instances that are realized by the key.
""",lang="en")
page.p("""This dict  can be used for <i>inverse</i> generation. Here are examples of calls with the result shown after &rArr;
<pre lang="en"><code>    lemmataEn = buildLemmataMap("en")
    print(", ".join(e.toSource() for e in lemmataEn["love"])) &rArr; <i>N('love'), V('love').t("b"), V('love').pe(1), V('love').pe(2), V('love').pe(1).n("p"), V('love').pe(2).n("p"), V('love').n("p")</i>
    print(", ".join(e.toSource() for e in lemmataEn["love"] if e.isA("N"))) &rArr; <i>N('love')</i>
</code></pre>
""",lang="en")

page.h3("<code>Constituent.QuoteOOV</code>")
page.p("""
Lorsque cette variable de classe est mise à <code>True</code>, les mots absents du lexique sont considérés 
comme des chaînes verbatim, i.e. <code>Q(...)</code> au lieu de susciter un avertissement et d'être 
affichés entre double crochets. Comme ceci empêche toute lemmatisation, accord ou transformation de 
phrases, il faut utiliser cet indicateur avec parcimonie.
""",lang="fr")
page.p("""
When this class variable is set to <code>True</code>, words that are not in the lexicon are considered as quoted 
strings, i.e. <code>Q(...)</code> instead of raising an warning and be displayed between double square 
brackets. As this prevents any lemmatization, agreement or sentence transformations, this flag should be 
used sparingly.
""",lang="en")


h2_fr("Sélection de variantes");h2_en("Variant selection")
page.h3("<code>oneOf(e<sub>1</sub>,e<sub>2</sub>,...)</code>")
page.p("""
où <code>e<sub>i</sub></code> est est une valeur, choisit un <code>e<sub>i</sub></code> au hasard. En <span 
class="jsr">pyrealb</span>, ces éléments sont souvent des constructeurs correspondant à des structures de 
phrases 
différentes. Si <code>e<sub>1</sub></code> est un tableau alors la sélection est faite dans ce tableau, en ignorant les autres paramètres.
""",lang="fr")
page.p("""
Pour éviter que tous les éléments soient évalués avant la sélection, il suffit de <em>fonctionaliser</em> 
l'expression en une fonction sans paramètre en la préfixant par <code>lambda</code>. Une fois l'élément choisi, <code>oneOf</code> vérifie si la valeur est une fonction et si c'est le cas, il retourne le résultat de l'appel. Par exemple,
<code>oneOf(lambda:N("amour"),lambda:N("amitié"))</code> permet de choisir entre les deux noms sans évaluer les deux 
constructeurs. Dans ce cas, très simple, il aurait été aussi possible d'écrire <code>N(oneOf("amour","amitié"))</code>.
""",lang="fr")
page.p("""
<code>oneOf</code> implante le <a href="https://rosaenlg.org/rosaenlg/4.3.0/mixins_ref/synonyms.html#_choose_randomly_but_try_not_to_repeat" target="_blank">"mode:once" de RosaeNLG</a>: une alternative est choisie au hasard, mais en essayant de ne pas répéter la précédente. Lorsque toutes les alternatives ont été utilisées, le système recommence avec les alternatives initiales, mais en évitant la dernière utilisée afin de ne pas se répéter.
""",lang="fr")
page.p("""
where <code>e<sub>i</sub></code> is a value, selects randomly a <code>e<sub>i</sub></code>. In <span 
class="jsr">pyrealb</span>, these elements are often constructors corresponding to different phrase structures. If <code>e<sub>1</sub></code> is an array, the selection is performed within this array, ignoring other parameters.
""",lang="en")
page.p("""
To avoid the evaluation of all elements before the selection, it is possible to <em>functionalize</em> an expression 
into a function with no formal parameter by prefixing it with <code>lambda</code>. 
Once the element is selected, <code>oneOf</code> checks if the value is a function and, if it is so, it returns the value of the called function. For exemple,
<code>oneOf(lambda:V("love"),lambda:V("like"))</code> allows choosing between the two verbs without evaluating both 
constructors. In this simplistic case, this could have also been written as <code>V(oneOf("love","like"))</code>.
""", lang="en")
page.p("""
<code>oneOf</code> implements the <a href="https://rosaenlg.org/rosaenlg/4.3.0/mixins_ref/synonyms.html#_choose_randomly_but_try_not_to_repeat"  target="_blank">"mode:once" of RosaeNLG</a>: it selects an alternative randomly, but tries not to repeat the same one. When all alternatives have been triggered, it resets but tries not run the last triggered alternative, avoiding repetitions.
""",lang="en")

page.h3("<code>choice(e<sub>1</sub>,e<sub>2</sub>,...)</code>")
page.p("""
Version de la fonction <code>oneOf</code> qui choisit une alternative sans tenir compte des choix précédents. 
C'est la méthode <i>classique</i> d'effectuer des choix aléatoires.
""",lang="fr")
page.p("""
Version of <code>oneOf</code> that selects an alternative into account without taking previous choices. 
This is the <i>classic</i> implementation for making random choices.
""",lang="en")

page.h3("<code>mix(e<sub>1</sub>,e<sub>2</sub>,...)</code>")
page.p("""
<i>permute</i> ses paramètres, ce qui peut être utile pour varier l'ordre des éléments. Si <code>e<sub>1</sub></code> 
est un tableau alors la sélection est faite dans ce tableau, en ignorant les autres paramètres. Comme pour 
<code>oneOf(...)</code>, pour éviter que tous les éléments soient évalués avant la sélection, il suffit de 
<em>fonctionaliser</em> l'expression en une fonction sans paramètre en la préfixant par <code>lambda</code>. Pour 
chaque élément de la liste, <code>mix</code> vérifie si sa valeur est une fonction et si c'est le cas, il le remplace par le 
résultat de l'appel.
""",lang="fr")
page.p("""
<i>shuffles</i> its parameters, which can be useful to vary the order of elements. If <code>e<sub>1</sub></code> is 
an array, the selection is performed within this array, ignoring other parameters. As for <code>oneOf(...)</code>, 
to avoid the evaluation of all elements before the selection, it is possible to <em>functionalize</em> a expression 
into a function with no formal parameter by prefixing it with <code>lambda</code>. 
For each element of the mixed list, <code>mix</code> checks if the value is a function and, if it is so, it replaces 
it by the value of the called function.
""", lang="en")

h2_fr("Traitement en JSON");h2_en("JSON processing")
page.p("""
Pour faciliter l'utilisation de <span class="jsr">pyrealb</span> en sortie d'un système externe. 
Il est possible d'utiliser un format d'entrée JSON <a href="http://rali.iro.umontreal.ca/JSrealB/current/documentation/jsRealB-jsonInput.html">
décrit dans ce document (en anglais)</a> où sont décrites deux API permettant 
d'appeler un serveur <i>node.js</i> <code>jsRealB</code> <a href="http://rali.iro.umontreal.ca/JSrealB/current/documentation/jsRealBfromPython.html">depuis un autre programme Python</a> ou Prolog. 
Il est également possible d'obtenir une expression JSON correspondant à une expression <span class="jsr">pyrealb</span>.
""",
lang="fr")
page.p("""
To simplify the use of <span class="jsr">pyrealb</span> as output of an external system, a JSON input format has been defined. 
<a href="http://rali.iro.umontreal.ca/JSrealB/current/documentation/jsRealB-jsonInput.html">It is described in this document.</a> in which two APIs are described 
for calling a <span class="jsr">pyrealb</span> <i>node.js</i> server <a href="http://rali.iro.umontreal.ca/JSrealB/current/documentation/jsRealBfromPython.html">from another Python</a> or Prolog. 
It is also possible to obtain the JSON expression corresponding to a given <span class="jsr">pyrealb</span> expression.""",
lang="en")

h2_fr("Informations sur la version");h2_en("Informations about the version")
page.h3("<code>pyrealb_version</code>")
page.p(f"Chaine de caractères indiquant le numéro de version de <span class='jsr'>pyrealb</span>, valeur actuelle:"
       f" {pyrealb_version}.",
       lang="fr")
page.p(f"String showing the version number of <span class='jsr'>pyrealb</span>, currently: {pyrealb_version}.",lang="en")

page.h3("<code>pyrealb_datecreated</code>")
page.p(f"Date de la création de la version courante de <span class='jsr'>pyrealb</span> valeur actuelle:"
       f" {str(pyrealb_datecreated)[:10]}.",
       lang="fr")
page.p(f"Creation date of the current <span class='jsr'>pyrealb</span>, currently {str(pyrealb_datecreated)[:10]}.",
       lang="en")

page.h3("<code>Constituent.exceptionOnWarning</code>")
page.p("Si cette variable de classe est mise à <code>True</code>, l'exception <code>PyrealbException</code> sera levée lors de l'émission d'un avertissement. L'appelant peut alors la traiter à son gré.",lang="fr")
page.p("When this class variable is set to <code>True</code>, the <code>PyrealbException</code> exception is raised when a warning is emitted. The caller can décide how to deal with it.",lang="en")

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
<li><a href="https://arxiv.org/pdf/2311.14808" lang="fr">Utilisation de pyrealb pour la génération bilingue 
(document en anglais)</a><a href="https://arxiv.org/pdf/2311.14808" lang="en">Use of pyrealb for Data-to-Text Bilingual
 Generation</a></li>
<li><a href="https://arxiv.org/pdf/2012.15425" lang="fr">Document décrivant l'organisation de <code>jsRealB</code>
(section 6.7 spécifique à <span class='jsr'>pyrealb</span>)</a><a href="https://arxiv.org/pdf/2012.15425" lang="en"
>Document describing the organization of the <code>jsRealB</code> (section 6.7 deals with <span class='jsr'>pyrealb</span></a></li>
<li><a href="http://rali.iro.umontreal.ca/rali/?q=fr/jsrealb-realisateur-bilingue-de-texte" lang="fr">Historique 
des versions de <code>jsRealB</code> et démonstrations</a><a 
href="http://rali.iro.umontreal.ca/rali/?q=en/jsrealb-bilingual-text-realiser" 
lang="en">Previous versions of <code>jsRealB</code> and demos</a></li>
<li><a href="http://rali.iro.umontreal.ca/JSrealB/current/Tutorial/tutorial.html" title="jsRealB tutorial" 
lang="fr">Tutoriel jsRealB (en anglais)</a><a 
href="http://rali.iro.umontreal.ca/JSrealB/current/Tutorial/tutorial.html" 
title="jsRealB tutorial" lang="en">jsRealB Tutorial</a></li>
<li><a href="https://mybinder.org/v2/gh/lapalme/pyrealb-jupyter/HEAD?labpath=pyrealb-fr.ipynb" 
title="Expérience avec pyrealb" lang="fr">Notebook Jupyter</a>
<a href="https://mybinder.org/v2/gh/lapalme/pyrealb-jupyter/HEAD?labpath=pyrealb-en.ipynb" title="Experimenting with 
pyrealb" lang="en">Jupyter Notebook</a></li>
<li><a href="https://github.com/lapalme/pyrealb" lang="fr">Dépot GitHub pyrealb</a>
<a href="https://github.com/lapalme/pyrealb" lang="en">pyreealb GitHub repository</a></li>
<li><a href="Lexicon-Format-fr.html" lang="fr">Format des entrées du lexique</a>
<a href="Lexicon-Format-en.html" lang="en">Format of the lexicon entries</a></li>
<li>Publications:
    <ul>
        <li>G. Lapalme, <em>Data-to-Text Bilingual Generation</em>, Nov 2023, 
        <a href='https://arxiv.org/abs/2311.14808'>https://arxiv.org/pdf/2311.14808</a></li>
        <li><a href="https://aclanthology.org/W15-4719/">Demo paper at ENLG-2015</a></li>
        <li>Daoust, N., and G. Lapalme, <em>JSreal: A Text Realizer for Web Programming</em>, Language Production, 
        Cognition, and the Lexicon - a Festschrift in honor of Michael Zock, Text, Speech and Language Technology, Vol 48: Springer, pp. 363-378, 2014. [<a href="http://rali.iro.umontreal.ca/rali/sites/default/files/publis/JSreal.pdf">PDF</a>]</li>
    </ul>
</li>
""")

if __name__ == "__main__":
    ### créer le fichier de sortie
    outFileN=os.path.abspath(os.path.join(os.path.dirname(__file__), "documentation.html"))
    outFile=open(outFileN,"w",encoding="utf-8")
    print(page,file=outFile)
    print(outFileN, "written")