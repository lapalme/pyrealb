import sys
from statistics import mean, quantiles
import json
from Games import Games

#
nb_quantiles = 5

#
# CREATE aggregated data that is then saved in a json file
team_game_scores = {}
player_scores = {}


def add_team_game_score(name, score):
    if name not in team_game_scores:
        team_game_scores[name] = []
    team_game_scores[name].append(score)


def add_player_score(name, score):
    if name not in player_scores:
        player_scores[name] = []
    player_scores[name].append(score)


def aggregate_scores(scores):
    # caution scores are changed in place
    ignored = []
    for name in scores:
        sc_n = scores[name]
        nb_values = len(sc_n)
        if nb_values > 1:
            aggregate = {}
            for key in sc_n[0].keys():
                data = [row[key] for row in sc_n]
                aggregate[key] = mean(data), quantiles(data,n=nb_quantiles,method="inclusive")
            scores[name] = (nb_values, aggregate)
        else:
            ignored.append(name)
    for name in ignored:
        del scores[name]


def show_aggregate_scores(title, scores, keys):
    titles = scores[next(iter(scores))][1].keys()
    line_width = 20 + 6 * (len(titles) + 1)
    # sep = "-" * line_width
    lines = [f"{title} - Mean and last of {nb_quantiles} quantiles".center(line_width),
             "{0}{1}|{2}".format("name".center(20), "NB".center(5), "|".join([t.center(5) for t in titles]))]
    for key in keys:
        (nb, values) = scores[key]
        lines.append(f"{key[:20]:20}" + f"{nb:5}|" + "|".join(f"{m[0]:5.1f}" for m in values.values()))
        lines.append(
            f"{'':>26}" + "|".join((f"{m[1][-1]:5.1f}" if m[1] is not None else " " * 5) for m in values.values()))
    lines.append("*" * line_width)
    return "\n".join(lines)


def compute_stats(games):
    global aggregate
    # collect team and player statistics
    for i in range(0, len(games)):
        game = games[i]
        for team in [game.home(), game.visitors()]:
            add_team_game_score(team.name(), team.line_scores("game").allScores())
            for player in team.players_scores():
                if player.minutes() > 1 and player.points() > 2:
                    add_player_score(player.name(), player.allScores())
    # aggregate statistics
    aggregate_scores(team_game_scores)
    # print(team_game_scores)
    print(show_aggregate_scores(f"{len(team_game_scores)} Teams", team_game_scores, sorted(team_game_scores.keys())))
    aggregate_scores(player_scores)
    # print(player_scores)
    print(show_aggregate_scores(f"{len(player_scores)} Players", player_scores,
                                # sort lines by "Family name" taken as the word after the last space.
                                sorted(player_scores.keys(), key=lambda s: s[s.rindex(" ") + 1:] if " " in s else s)))


#
#  USE aggregated data read from a json file
# aggregated data goes here...
aggregate = None


def player_has_statistics(name):
    return name in aggregate["players"]


def team_has_statistics(name):
    return name in aggregate["teams"]


def getStats(kind, name, stat_type):
    agg = aggregate[kind]
    if name in agg:
        if stat_type == "NB":
            return agg[name][0]
        elif stat_type in agg[name][1]:
            return agg[name][1][stat_type]
        else:
            print(f"*** {stat_type} not found for {name}",file=sys.stderr)
            return None
    else:
        print(f"*** {name} not found in {kind}",file=sys.stderr)
        return None


def is_inquantile(kind, name, stat_type, value, nth):
    data = getStats(kind, name, stat_type)
    if data is None: return False
    if nth == -1:
        return value > data[1][-1]
    elif nth == 1:
        return value < data[1][0]
    else:
        print('quantile should be 1 or -1 but is', nth,file=sys.stderr)
        return False


def is_high(kind, name, stat_type, value):
    if value == 0: return False
    return is_inquantile(kind, name, stat_type, value, -1)


def is_low(kind, name, stat_type, value):
    if value == 0: return False
    return is_inquantile(kind, name, stat_type, value, 1)


split = "train"
json_file_name = f"./data/{split}-aggregate.json"

if __name__ == "__main__":
    games = Games("train")
    compute_stats(games)
    # save the json file
    aggregate = {"teams": team_game_scores, "players": player_scores, }
    json.dump(aggregate,
              open(json_file_name, "w", encoding="utf-8"),
              ensure_ascii=False)
    print(f"{json_file_name}:written")
    # a few tests
    print(getStats("teams", "76ers", "NB"))
    print(getStats("teams", "Heat", "FG3M"))
    print(getStats("teams", "Test", "FG3M"))
    print(getStats("teams", "Heat", "TEST"))
    print(is_low("teams", "Rockets", "FGM", 45))
    print(is_high("teams", "Rockets", "FGM", 45))
    print(is_low("teams", "Rockets", "FGA", 25))
    print(is_high("teams", "Rockets", "FGA", 25))
else:
    # read previously created data
    aggregate = json.load(open(json_file_name, "r", encoding="utf8"))
