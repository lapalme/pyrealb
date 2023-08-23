import sys
from statistics import mean, quantiles
import json
from Games import Games
from Score import Score

nb_quantiles = 5

def show_aggregate_scores(title: str, scores, keys: [str]) -> str:
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


def compute_stats(games: Games):
    # CREATE aggregated data to be saved in a json file
    team_game_scores: dict[str, [dict[str, int]]] = {}
    player_scores: dict[str, [dict[str, int]]] = {}

    def add_team_game_score(name: str, score: dict[str, int]):
        if name not in team_game_scores:
            team_game_scores[name] = []
        team_game_scores[name].append(score)

    def add_player_score(name: str, score: dict[str, int]):
        if name not in player_scores:
            player_scores[name] = []
        player_scores[name].append(score)

    def aggregate_scores(scores: dict[str, [dict[str, int]]]) -> dict[str, (float, dict[str, (int, [float])])]:
        new_scores = {}
        for name in scores:
            sc_n: [dict[str, int]] = scores[name]
            nb_values = len(sc_n)
            if nb_values > 1:
                aggr: dict[str, (int, [float])] = {}
                for key in Score.score_titles:
                    if key in sc_n[0]:
                        data: [int] = [row[key] for row in sc_n]
                        aggr[key] = mean(data), quantiles(data, n=nb_quantiles, method="inclusive")
                new_scores[name] = (nb_values, aggr)
        return new_scores

    # collect team and player statistics
    for key in games.keys():
        game = games[key]
        for team in [game.home(), game.visitors()]:
            add_team_game_score(team.name(), team.period_scores["game"].score_dict)
            for player in team.players:
                if player.scores.minutes() > 1 and player.scores.points() > 2:
                    add_player_score(player.name(), player.scores.score_dict)
    # aggregate statistics
    agg_team_game_scores = aggregate_scores(team_game_scores)
    # print(team_game_scores)
    print(show_aggregate_scores(f"{len(agg_team_game_scores)} Teams",
                                agg_team_game_scores,
                                sorted(agg_team_game_scores.keys())))
    agg_player_scores = aggregate_scores(player_scores)
    # print(player_scores)
    print(show_aggregate_scores(f"{len(agg_player_scores)} Players",
                                agg_player_scores,
                                # sort lines by "Family name" taken as the word after the last space.
                                sorted(agg_player_scores.keys(),
                                       key=lambda s: s[s.rindex(" ") + 1:] if " " in s else s)))
    return {"teams": agg_team_game_scores, "players": agg_player_scores}

#  USE aggregated data read from a json file
# aggregated data will go here...
aggregate: dict[str, (float, dict[str, (int, [float])])] = {}

def allTeams() -> [str]:
    return list(aggregate["teams"].keys())

def allPlayers() -> [str]:
    return list(aggregate["players"].keys())

def player_has_statistics(name) -> bool:
    return name in aggregate["players"]

def team_has_statistics(name) -> bool:
    return name in aggregate["teams"]

def getStats(kind, name, stat_type) -> [float]:
    agg = aggregate[kind]
    if name in agg:
        if stat_type in agg[name][1]:
            return agg[name][1][stat_type]
        else:
            print(f"*** {stat_type} not found for {name}", file=sys.stderr)
            return None
    else:
        print(f"*** {name} not found in {kind}", file=sys.stderr)
        return None


def is_in_quantile(kind, name, stat_type, value, nth) -> bool:
    data = getStats(kind, name, stat_type)
    if data is None:
        return False
    if nth == -1:
        return value > data[1][-1]
    elif nth == 1:
        return value < data[1][0]
    else:
        print('quantile should be 1 or -1 but is', nth, file=sys.stderr)
        return False


def is_high(kind, name, stat_type, value) -> bool:
    if value == 0:
        return False
    return is_in_quantile(kind, name, stat_type, value, -1)


def is_low(kind, name, stat_type, value) -> bool:
    if value == 0:
        return False
    return is_in_quantile(kind, name, stat_type, value, 1)


split = "train"
json_file_name = f"./data/{split}-aggregate.json"

if __name__ == "__main__":
    games = Games("train")
    aggregate = compute_stats(games)
    # save the json file
    # json.dump(aggregate,
    #           open(json_file_name, "w", encoding="utf-8"),
    #           ensure_ascii=False)
    # print(f"{json_file_name}:written")
    # perform a few tests
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
