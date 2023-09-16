from Games import Games
from Team import Team, period_names
from random import sample
from Score import Score
import re

games = None


def set_games(g):
    global games
    games = g

####################################################################################
#   Computation for "intra-event complex" facts according to the nomenclature of
#   Upadhyay and Massie, Content Type Profiling of Data-to-text Genetation Datasets,
#         COLING 2022
# Compute some word statistics to try to show that the validation and training corpora
# are different from the training in the number of words, but finally inconclusive
# as there were some little differences, but not enough to be convincing
# (although I did not compute the confidence intervals)
def word_stats(game):
    def filter_references(game):
        # show reference sentences without any player name
        player_names = set()
        for t in [game.home(), game.visitors()]:
            for n in t.player_names():
                for w in re.split(r"\W", n):
                    if len(w) > 1:
                        player_names.add(w)
        player_names_re = re.compile(r"\b(" + "|".join(list(player_names)) + r")\b")
        return [sent for sent in game.reference_sentences()[0].split("\n")
                if player_names_re.search(sent) is None]

    sents = game.reference_sentences()[0].split("\n")
    words = [w for s in sents for w in re.split(r"\W",s) if len(w)>0]
    # print(words)
    sentsF = filter_references(game)
    wordsF = [w for s in sentsF for w in re.split(r"\W",s) if len(w)>0]
    # print(wordsF)
    return (game.game_id(),len(sents), sum(map(len,words)),len(sentsF),sum(map(len,wordsF)))

def word_starts_split(split):
    games = Games(split)
    for key in games.keys():
        game = games[key]
        (gid,nb_sents,nb_words,nb_sentsF,nb_words_F)=word_stats(game)
        print(f"{gid:5}\t{game.date().strftime('%Y-%m-%d')}\t"
              f"{nb_sents:5}\t{nb_words}\t{nb_sentsF}\t{nb_words_F}")


# Compute "interesting" statistics between scores of the winner and the loser
def interesting_stats(winner_scores: dict[str,Score], loser_scores: dict[str,Score]) -> [tuple[str,str,int,int,int]]:
    fns = ["goals", "goals3", "free_throws", "rebounds", "assists", "steals","blocks",
           "turnovers","fouls","points"]

    # Absolute and difference thresholds for scores considered interesting for a given quarter
    # the thresholds apply to the scores of both teams and their differences
    # these threshold are multiplied by 1.5 for a half and by 2 for a game
    # Differences are also computed for ratios between "attempted" and "made"
    # in percentage as an int between 0 and 100,
    # for "goals", "goals3" and "free_throws"
    # a fact is a 5-tuple (period,score_name,winner_val,loser_val,difference)
    # the interesting facts are sorted in descending order by the absolute value of the difference
    thresholds = {"assists":10,"steals":3,"blocks":3,"turnovers":6} # specific thresholds
    thresholds_def = 5                                              # default threshold

    def ratio(sc, fn) -> int:
        denom = getattr(sc, fn + "_attempted")()
        if denom == 0: return -1
        num = getattr(sc, fn)()
        if num < 5: return -1
        return round(num * 100 / denom)

    interesting = []
    for period in period_names:
        win_sc = winner_scores[period]
        loser_sc = loser_scores[period]
        for fn in fns:
            win_stat = getattr(win_sc, fn)()
            loser_stat = getattr(loser_sc, fn)()
            # determine "interesting" thresholds
            threshold = thresholds.get(fn,thresholds_def)
            if period == "game": threshold *= 2
            elif period == "H1" or "H2" : threshold = int(threshold*1.5)
            if win_stat > threshold and loser_stat > threshold and abs(win_stat-loser_stat) > threshold:
                if period != "game" or fn != "points" : # ignore repeating global score
                    interesting.append((period,fn,win_stat,loser_stat,win_stat-loser_stat))
        for fn in fns[0:3]: # check for ratio for field goals, three-points and free throws
            win_ratio = ratio(win_sc, fn)
            loser_ratio = ratio(loser_sc,fn)
            if win_ratio>0 and loser_ratio>0 and abs(win_ratio-loser_ratio) > 10:
                interesting.append((period,fn+"%",win_ratio,loser_ratio,win_ratio-loser_ratio))
    return sorted(interesting,key=lambda vals:abs(vals[4]),reverse=True) # sort descending by last value of tuple

# keep only the best interesting facts, at most 5:
#   - keep the tuple with the best difference
#   - remove other tuple of the same period and score to avoid repetition
#   - loop until there are no more facts left
# sort the selected facts "chronologically" by period (first element of the tupple)
def get_most_interesting(interesting) -> [tuple[str,str,int,int,int]]:
    out = []
    # find the most interesting facts
    most_interesting = []
    while len(most_interesting) < 4 and len(interesting) > 0:
        fact = interesting.pop(0)
        most_interesting.append(fact)
        # filter to avoid repeating info about the same aspect or period
        interesting = [f for f in interesting if f[0] != fact[0] and f[1] != fact[1]]
    # sort in order  of the game
    game_order = {"Q1": 1, "Q2": 2, "H1": 3, "Q3": 4, "Q4": 5, "H2": 6, "game": 7}
    most_interesting.sort(key=lambda vals: game_order[vals[0]])
    return most_interesting



if __name__ == "__main__":
    # word_starts_split("test")
    # means computed using Excel
    # sents words   sentsF  wordsF
    # 13,54	1333,28	6,67	619,87	train
    # 14,70	1374,27	7,15	686,00	validation
    # 14,00	1290,66	6,93	659,89	test
    games = Games("validation")
    keys_sample = sample(games.keys(), k=1)
    for key in keys_sample:
        game = games[key]
        print(game.show_title())
        print(game.home().show(False))
        print(game.visitors().show(False))
        interesting = interesting_stats(game.winner().period_scores, game.loser().period_scores)
        print("\n".join(map(str,interesting)))
        print("---- most interesting ---")
        print("\n".join(map(str,get_most_interesting(interesting))))
        # print(word_stats(game))
        # print("=====")
