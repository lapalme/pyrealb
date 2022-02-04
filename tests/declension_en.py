from context import pyrealb
from pyrealb.all import *
from test import test


def declension_en():
    testsDeclensionEn = {
         "activity":{"N":{"p":"activities"}},
         "all":{"Adv":{"co":"all"}},
         "analysis":{"N":{"p":"analyses"}},
         "audience":{"N":{"p":"audiences"}},
         "avocado":{"N":{"p":"avocados"}},
         "bad":{"A":{"co":"worse",
                     "su":"worst"}},
         "badly":{"Adv":{"co":"worse"}},
         "basis":{"N":{"p":"bases"}},
         "batch":{"N":{"p":"batches"}},
         "berry":{"N":{"p":"berries"}},
         "big":{"A":{"co":"bigger",
                     "su":"biggest"}},
         "box":{"N":{"p":"boxes"}},
         "boy":{"N":{"p":"boys"}},
         "bunch":{"N":{"p":"bunches"}},
         "bus":{"N":{"p":"buses"}},
         "businessman":{"N":{"p":"businessmen"}},
         "calf":{"N":{"p":"calves"}},
         "car":{"N":{"p":"cars"}},
         "cargo":{"N":{"p":"cargoes"}},
         "cattle":{"N":{"p":"cattle"}},
         "chairman":{"N":{"p":"chairmen"}},
         "chief":{"N":{"p":"chiefs"}},
         "child":{"N":{"p":"children"}},
         "choir":{"N":{"p":"choirs"}},
         "church":{"N":{"p":"churches"}},
         "city":{"N":{"p":"cities"}},
         "civil":{"A":{"co":"civiller",
                       "su":"civillest"}},
         "clergy":{"N":{"p":"clergies"}},
         "clothes":{"N":{"p":"clothes"}},
         "coalition":{"N":{"p":"coalitions"}},
         "collection":{"N":{"p":"collections"}},
         "committee":{"N":{"p":"committees"}},
         "commons":{"N":{"p":"commons"}},
         "constituency":{"N":{"p":"constituencies"}},
         "corps":{"N":{"p":"corps"}},
         "council":{"N":{"p":"councils"}},
         "craftsman":{"N":{"p":"craftsmen"}},
         "crew":{"N":{"p":"crews"}},
         "crisis":{"N":{"p":"crises"}},
         "day":{"N":{"p":"days"}},
         "diagnosis":{"N":{"p":"diagnoses"}},
         "economics":{"N":{"p":"economics"}},
         "elite":{"N":{"p":"elites"}},
         "emphasis":{"N":{"p":"emphases"}},
         "establishment":{"N":{"p":"establishments"}},
         "ethics":{"N":{"p":"ethics"}},
         "far":{"A":{"co":"farther",
                     "su":"farthest"}},
         "fat":{"A":{"co":"fatter",
                     "su":"fattest"}},
         "fisherman":{"N":{"p":"fishermen"}},
         "fit":{"A":{"co":"fitter",
                     "su":"fittest"}},
         "flat":{"A":{"co":"flatter",
                      "su":"flattest"}},
         "fleet":{"N":{"p":"fleets"}},
         "foot":{"N":{"p":"feet"}},
         "formula":{"N":{"p":"formulas"}},
         "gang":{"N":{"p":"gangs"}},
         "gentleman":{"N":{"p":"gentlemen"}},
         "glad":{"A":{"co":"gladder",
                      "su":"gladdest"}},
         "go":{"N":{"p":"goes"}},
         "good":{"A":{"co":"better",
                      "su":"best"}},
         "government":{"N":{"p":"governments"}},
         "grim":{"A":{"co":"grimmer",
                      "su":"grimmest"}},
         "half":{"N":{"p":"halves"}},
         "handful":{"N":{"p":"handfuls"}},
         "headquarters":{"N":{"p":"headquarters"}},
         "herd":{"N":{"p":"herds"}},
         "hero":{"N":{"p":"heroes"}},
         "hot":{"A":{"co":"hotter",
                     "su":"hottest"}},
         "household":{"N":{"p":"households"}},
         "housewife":{"N":{"p":"housewives"}},
         "hypothesis":{"N":{"p":"hypotheses"}},
         "jeans":{"N":{"p":"jeans"}},
         "knife":{"N":{"p":"knives"}},
         "lab":{"N":{"p":"labs"}},
         "leadership":{"N":{"p":"leadership"}},
         "life":{"N":{"p":"lives"}},
         "little":{"Adv":{"co":"less"}},
         "loyal":{"A":{"co":"loyaller",
                       "su":"loyallest"}},
         "mad":{"A":{"co":"madder",
                     "su":"maddest"}},
         "man":{"N":{"p":"men"}},
         "management":{"N":{"p":"managements"}},
         "mankind":{"N":{"p":"mankind"}},
         "monarch":{"N":{"p":"monarchs"}},
         "mouse":{"N":{"p":"mice"}},
         "navy":{"N":{"p":"navies"}},
         "neighbourhood":{"N":{"p":"neighbourhoods"}},
         "number":{"N":{"p":"numbers"}},
         "orchestra":{"N":{"p":"orchestras"}},
         "pair":{"N":{"p":"pairs"}},
         "person":{"N":{"p":"persons"}},
         "personnel":{"N":{"p":"personnels"}},
         "police":{"N":{"p":"police"}},
         "policeman":{"N":{"p":"policemen"}},
         "politics":{"N":{"p":"politics"}},
         "potato":{"N":{"p":"potatoes"}},
         "quantum":{"N":{"p":"quanta"}},
         "red":{"A":{"co":"redder",
                     "su":"reddest"}},
         "regiment":{"N":{"p":"regiments"}},
         "roof":{"N":{"p":"roofs"}},
         "sad":{"A":{"co":"sadder",
                     "su":"saddest"}},
         "self":{"N":{"p":"selves"}},
         "senate":{"N":{"p":"senates"}},
         "series":{"N":{"p":"series"}},
         "sheep":{"N":{"p":"sheep"}},
         "shelf":{"N":{"p":"shelves"}},
         "shy":{"A":{"co":"shyer",
                     "su":"shyest"}},
         "slim":{"A":{"co":"slimmer",
                      "su":"slimmest"}},
         "solo":{"N":{"p":"solos"}},
         "species":{"N":{"p":"species"}},
         "spokesman":{"N":{"p":"spokesmen"}},
         "statistics":{"N":{"p":"statistics"}},
         "stimulus":{"N":{"p":"stimuli"}},
         "stomach":{"N":{"p":"stomachs"}},
         "synthesis":{"N":{"p":"syntheses"}},
         "team":{"N":{"p":"teams"}},
         "thesis":{"N":{"p":"theses"}},
         "thief":{"N":{"p":"thieves"}},
         "thin":{"A":{"co":"thinner",
                      "su":"thinnest"}},
         "tomato":{"N":{"p":"tomatoes"}},
         "tooth":{"N":{"p":"teeth"}},
         "well":{"A":{"co":"better",
                      "su":"best"}},
         "wet":{"A":{"co":"wetter",
                     "su":"wettest"}},
         "wife":{"N":{"p":"wives"}},
         "wolf":{"N":{"p":"wolves"}},
         "woman":{"N":{"p":"women"}},
         "wrong":{"A":{"co":"wronger",
                       "su":"wrongest"}},
         "zero":{"N":{"p":"zeros"}},
         "zoo":{"N":{"p":"zoos"}}
        };
        
    testPronounDeclensionEn=[
            ["I",{"I":{"n":"s","ow":"s","g":"m","pe":1}}],
            ["me",{"me":{"n":"s","ow":"s","g":"m","pe":1}}],
            ["mine",{"mine":{"n":"s","ow":"s","g":"m","pe":1}}],
            ["myself",{"myself":{"n":"s","ow":"s","g":"m","pe":1}}],
            ["I",{"you":{"n":"s","ow":"s","g":"m","pe":2}}],
            ["me",{"you":{"n":"s","ow":"s","g":"m","pe":2}}],
            ["mine",{"yours":{"n":"s","ow":"s","g":"m","pe":2}}],
            ["myself",{"yourself":{"n":"s","ow":"s","g":"m","pe":2}}],
            ["I",{"he":{"n":"s","ow":"s","g":"m","pe":3}}],
            ["me",{"him":{"n":"s","ow":"s","g":"m","pe":3}}],
            ["mine",{"his":{"n":"s","ow":"s","g":"m","pe":3}}],
            ["myself",{"himself":{"n":"s","ow":"s","g":"m","pe":3}}],
            ["I",{"she":{"n":"s","ow":"s","g":"f","pe":3}}],
            ["me",{"her":{"n":"s","ow":"s","g":"f","pe":3}}],
            ["mine",{"hers":{"n":"s","ow":"s","g":"f","pe":3}}],
            ["myself",{"herself":{"n":"s","ow":"s","g":"f","pe":3}}],
            ["I",{"it":{"n":"s","ow":"s","g":"n","pe":3}}],
            ["me",{"it":{"n":"s","ow":"s","g":"n","pe":3}}],
            ["mine",{"its":{"n":"s","ow":"s","g":"n","pe":3}}],
            ["myself",{"itself":{"n":"s","ow":"s","g":"n","pe":3}}],
            ["I",{"we":{"n":"p","ow":"p","g":"m","pe":1}}],
            ["me",{"us":{"n":"p","ow":"p","g":"m","pe":1}}],
            ["mine",{"ours":{"n":"p","ow":"p","g":"m","pe":1}}],
            ["myself",{"ourselves":{"n":"p","ow":"p","g":"m","pe":1}}],
            ["I",{"you":{"n":"p","ow":"p","g":"m","pe":2}}],
            ["me",{"you":{"n":"p","ow":"p","g":"m","pe":2}}],
            ["mine",{"yours":{"n":"p","ow":"p","g":"m","pe":2}}],
            ["myself",{"yourselves":{"n":"p","ow":"p","g":"m","pe":2}}],
            ["I",{"they":{"n":"p","ow":"p","g":"m","pe":3}}],
            ["me",{"them":{"n":"p","ow":"p","g":"m","pe":3}}],
            ["mine",{"theirs":{"n":"p","ow":"p","g":"m","pe":3}}],
            ["myself",{"themselves":{"n":"p","ow":"p","g":"m","pe":3}}],
            ["why",{"why":{"n":"p","g":"m","pe":1}}],
            ["who",{"who":{"n":"p","g":"m","pe":1}}],
            ["where",{"where":{"n":"p","g":"m","pe":1}}],
            ["this",{"these":{"n":"p","g":"m","pe":3}}],
            ["that",{"those":{"n":"p","g":"m","pe":3}}],
        ]
        
    testDetDeclensionEn=[
            ["a",{"":{"n":"p","ow":"p","g":"m","pe":1}}],
            ["my",{"our":{"n":"p","ow":"p","g":"m","pe":1}}],
            ["that",{"those":{"n":"p","ow":"p","g":"m","pe":1}}],
            ["what",{"what":{"n":"p","ow":"p","g":"m","pe":1}}],
            ["which",{"which":{"n":"p","ow":"p","g":"m","pe":1}}],
            ["whose",{"whose":{"n":"p","ow":"p","g":"m","pe":1}}],
        ]
    
    def makeTestExpr(exp,expected):
        return {
            "expression":exp,
            "expected": expected,
            "message":f"{exp.toSource()}=>{expected}"
        }
    
    loadEn()
    tests=[]
    
    for word,wordInfo in testsDeclensionEn.items():
        for pos,expected in wordInfo.items():
            if pos=="N":
                tests.append(makeTestExpr(N(word).n("p"), expected["p"]))
            elif pos=="A":
                tests.append(makeTestExpr(A(word).f("co"), expected["co"]))
                tests.append(makeTestExpr(A(word).f("su"), expected["su"]))
            elif pos=="Adv":
                tests.append(makeTestExpr(Adv(word).f("co"),expected["co"]))

    for pro,proInfo in testPronounDeclensionEn:
        for expected,flags in proInfo.items():
            exp=Pro(pro).n(flags["n"]).g(flags["g"]).pe(flags["pe"])
            if "ow" in flags:exp.ow(flags["ow"])
            tests.append(makeTestExpr(exp, expected))
    
    for pro,proInfo in testDetDeclensionEn:
        for expected,flags in proInfo.items():
            exp=D(pro).n(flags["n"]).g(flags["g"]).pe(flags["pe"])
            if "ow" in flags:exp.ow(flags["ow"])
            tests.append(makeTestExpr(exp, expected))
    
    return tests

if __name__ == '__main__':
    test("English declension","en",declension_en,badOnly=True)