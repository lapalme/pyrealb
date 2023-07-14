# from pyrealb import *
from datetime import datetime
from random import sample
from itertools import accumulate
from stats import is_high, player_has_statistics
from Games import Games
from Team import Team
from FStrings import FStrings
from English import English
from French import French


def player_has_interesting_statistics(player) -> bool:
    stats_to_check = {"FGM": 'goals', "FG3M": 'goals3', "TREB": 'rebounds', "AST": 'assists', "PTS": 'points'}
    name = player.name()
    for key in stats_to_check:
        val = getattr(player, stats_to_check[key])()
        if is_high("players", name, key, val):
            return True
    return False


def turning_points(winner, loser) -> (Team, Team, bool, bool, bool, bool):
    winner_pts = winner.get_points()
    loser_pts = loser.get_points()
    overtime = winner.line_scores("OT").points() > 0 or loser.line_scores("OT").points() > 0
    loser_lead_in_first_half = loser_pts["H1"] > winner_pts["H1"]
    loser_lead_in_second_half = loser_pts["H2"] > winner_pts["H2"]
    winner_cum = list(accumulate(list(winner_pts.values())[:4]))
    loser_cum = list(accumulate(list(loser_pts.values())[:4]))
    always_lead = all(winner_cum[i] > loser_cum[i] for i in range(0, 4))
    return (winner, loser, overtime, loser_lead_in_first_half, loser_lead_in_second_half, always_lead)


def next_game(team) -> (datetime, Team, bool, Team):
    # return the info about the next game of the team
    #  [date, team, is-it at home, other team]
    next_game = games[team.next_game_id()]
    if next_game is None:
        return None
    team_name = team.name()
    home_name = next_game.home().name()
    at_home = team_name == home_name
    return (next_game.date(), team, at_home,
            next_game.visitors() if at_home else next_game.home())


def summarize(realizer, game) -> str:
    # determine winner and loser
    home = game.home()
    visitors = game.visitors()
    if home.line_scores("game").points() > visitors.line_scores("game").points():
        winner, loser = home, visitors
    else:
        winner, loser = visitors, home
    paras = []
    # 1 - give the winner and loser scores with location and date information about the game
    paras.append(realizer.show_winner(winner, loser, game.date(),
                                      game.stadium(), game.city()))
    winner_scores = winner.players_scores()
    loser_scores = loser.players_scores()
    # 2 - check for interesting turning points in the game
    t_points = realizer.show_turning_points(*turning_points(winner, loser))
    if len(t_points) > 0:
        paras.append(t_points)
    # 3 - give information about the best players of both teams
    vps = sample(realizer.best_player_VPs, k=len(realizer.best_player_VPs))
    paras.append(
        realizer.show_player_perf(winner_scores[0],
                                  vps[0], winner_scores[0].starter()) +
        realizer.show_player_perf(loser_scores[0],
                                  vps[1], loser_scores[0].starter())
    )
    # 4 - show interesting statistics for each team and their players
    vps = sample(realizer.player_VPs, k=len(realizer.player_VPs))
    iVP = 0
    for team in [winner, loser]:
        # 4.1 - show global team performance
        team_para = [realizer.show_team_perf(team)]
        # 4.2 - show player performance of the team (in decreasing order of points made)
        first = True  # indicate starter only for the first player
        for player in team.players_scores()[1:]:
            if first:
                starter = player.starter()
                first = False
            if player_has_statistics(player.name()) \
                    and player_has_interesting_statistics(player):
                # show interesting statistics about a given player in a given game
                team_para.append(realizer.show_player_perf(player,
                                                           vps[iVP % len(vps)], starter))
                iVP += 1
            starter = False
        paras.append(" ".join(team_para))
    # 5 - give information about the next games for the winner and the loser if available
    next_games = ""
    next_game_info = next_game(winner)
    if next_game_info is not None:
        next_games += realizer.show_next_game(*next_game_info)
    next_game_info = next_game(loser)
    if next_game_info is not None:
        next_games += realizer.show_next_game(*next_game_info)
    if len(next_games) > 0:
        paras.append(next_games)
    return "\n\n".join(paras)


# useful for comparing the generated summary with the reference
# unused for the moment...
from textwrap import wrap


def display_side_by_side(gen_sum, orig_sum, width):
    gen_sum_lines = list(filter(lambda l: len(l) > 0, gen_sum.split("\n")))
    original_sum_lines = orig_sum.split("\n")
    gen_l = len(gen_sum_lines)
    orig_l = len(original_sum_lines)
    for i in range(max(gen_l, orig_l)):
        gen = wrap(gen_sum_lines[i], width=width) if i < gen_l else [""]
        orig = wrap(original_sum_lines[i], width=width) if i < orig_l else [""]
        for j in range(max(len(gen), len(orig))):
            left = gen[j].ljust(width) if j < len(gen) else " " * width
            right = orig[j] if j < len(orig) else " "
            print(left + " | " + right)


def show_summaries(game, realisers, show_data=False, show_refs=False):
    print("*** ", game.show_title(), "\n")
    # show the data used for summarization
    if show_data:
        print(game.home())
        print()
        print(game.visitors())
        print()
    for realizer in realisers:
        realizer.set_language() # must set the appropriate language before each summary
        print("***", realizer.name)
        gen_sum = summarize(realizer, game)
        print(gen_sum)
        print("-" * 25)
    if show_refs:
        print("***", "reference")
        # orig_sum=game.summaries()[0]
        orig_sum = game.obj["references"][0]
        print(orig_sum)
    print("=" * 100)


if __name__ == "__main__":
    games = Games("train")
    nb = 0
    for i in games:
        g = games[i]
        show_summaries(g, [FStrings(), English(), French()])
        nb += 1
        if nb > 10: break
