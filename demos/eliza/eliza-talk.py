from keywordsFr import elizaInitials, elizaFinals, elizaQuits
from eliza import choose, getTerminals, getKeyword, select, enKeys, getQuestion
from lemmatize import tokenizeFr

user_gender = "m"
eliza_gender = "f"
use_majestic = True
trace = False

def ask(fn,groups):
    print(fn(groups, user_gender).typ({"maje":use_majestic}).realize())

def talkWithElixa():
    ask(choose(elizaInitials),[])
    while True:
        userInput = input()
        if userInput.lower() in elizaQuits:
            ask(choose(elizaFinals),[])
            break
        terminals = [getTerminals(tok) for tok in tokenizeFr(userInput)]
        keyword = getKeyword(terminals)
        if keyword is None:
            ask(select(enKeys["xnone"]["pats"][0]), [])
        else:
            (questionFn, groups) = getQuestion(terminals, keyword, use_majestic, trace)
            if questionFn is not None:
                ask(questionFn, groups)
            else:
                print("****: pas de question trouvée:" + keyword)

if __name__ == "__main__":
    talkWithElixa()