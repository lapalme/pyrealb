from datetime import datetime
from random import sample
from itertools import accumulate
from stats import is_high, player_has_statistics
from textwrap import wrap

from Games import Games
from Team import Team
from seasons_stats import winning_streak, losing_streak, set_games
from game_stats import interesting_stats
from FStrings import FStrings
from English import English
from French import French

games = None  # to be filled later in either make_sample or in main, used by next_game()


def player_has_interesting_statistics(player) -> bool:
    stats_to_check = {"FGM": 'goals', "FG3M": 'goals3', "TREB": 'rebounds', "AST": 'assists', "PTS": 'points'}
    if player.scores.points() <= 2:  # ignore a player that scored 2 points or less
        return False
    name = player.name()
    for key in stats_to_check:
        val = getattr(player.scores, stats_to_check[key])()
        if is_high("players", name, key, val):
            return True
    return False


def turning_points(winner, loser) -> (Team, Team, bool, bool, bool, bool):
    overtime = winner.get_points("OT") > 0 or loser.get_points("OT") > 0
    loser_lead_in_first_half = loser.get_points("H1") > winner.get_points("H1")
    loser_lead_in_second_half = loser.get_points("H2") > winner.get_points("H2")
    winner_points = [winner.get_points("Q" + i) for i in "1234"]
    winner_cum = list(accumulate(winner_points))
    loser_points = [loser.get_points("Q" + i) for i in "1234"]
    loser_cum = list(accumulate(loser_points))
    # print(f"{winner.name():10}",winner_points,winner_cum)
    # print(f"{loser.name():10}",loser_points,loser_cum)
    always_lead = all(winner_cum[i] > loser_cum[i] for i in range(0, 4))
    return (winner, loser, overtime, loser_lead_in_first_half,
            loser_lead_in_second_half, always_lead)


# diff_threshold = 5  # threshold for an "interesting" difference in scores
# def game_unfolding(winner, loser):
#     diffs_q = [0]  # dummy 0 element
#     for i in [1, 2, 3, 4]:
#         q = "Q" + str(i)
#         diffs_q.append(winner.get_points(q) - loser.get_points(q))
#     diffs_h = [0]  # dummy 0 element
#     for i in [1, 2]:
#         h = "H" + str(i)
#         # difference in % field goals, field goals 3 or in number of rebounds
#         diffs_h.append(winner.get_points(h) - loser.get_points(h))


def next_game(team) -> (datetime, Team, bool, Team):
    # return the info about the next game of the team
    #  [date, team, is-it at home, other team]
    next_g = games[team.next_game_id()]
    if next_g is None:
        return None
    team_name = team.name()
    home_name = next_g.home().name()
    at_home = team_name == home_name
    return (next_g.date(), team, at_home,
            next_g.visitors() if at_home else next_g.home())


def summarize(realizer, game) -> str:
    # determine winner and loser
    home = game.home()
    visitors = game.visitors()
    if game.winner() == home:
        winner, loser = home, visitors
    else:
        winner, loser = visitors, home

    paras = []
    # 1 - give the winner and loser scores with location and date of the game
    winning_streak_length = winning_streak(game.game_id(), winner.name())
    paras.append(realizer.show_winner(winner, loser, game.date(),
                                      game.stadium(), game.city(),
                                      winning_streak_length))
    losing_streak_length = losing_streak(game.game_id(), winner.name())
    if losing_streak_length > 3:
        paras.append(realizer.team_losing_streak_vp(loser, losing_streak_length))

    # 2 - check for turning points and interesting facts during the game
    game_para = []
    t_points = realizer.show_turning_points(*turning_points(winner, loser))
    if len(t_points) > 0:
        game_para.append(t_points)
    interesting = interesting_stats(winner.period_scores, loser.period_scores)
    int_facts = realizer.show_team_facts(winner, loser, interesting)
    game_para.extend(int_facts)
    if len(game_para) > 0:
        paras.append("".join(game_para))

    # 3 - give information about the best players of both teams
    winner_players = winner.players_sorted()
    loser_players = loser.players_sorted()
    paras.append(
        realizer.show_player_perf(winner_players[0],
                                  realizer.best_player_VP,
                                  winner_players[0].starter()) +
        realizer.show_player_perf(loser_players[0],
                                  realizer.best_player_VP,
                                  loser_players[0].starter())
    )

    # 4 - show interesting statistics for each team and their players
    for team in [winner, loser]:
        # 4.1 - show global team performance
        team_para = [realizer.show_team_perf(team)]
        # 4.2 - show player performance of the team in decreasing order of points
        # statistics for the best player have given above, so we start at index 1
        players = team.players_sorted()
        if player_has_statistics(players[1].name()) \
                and player_has_interesting_statistics(players[1]):
            # indicate starter only for the second-best player
            team_para.append(
                realizer.show_player_perf(players[1],
                                          realizer.player_VP, players[1].starter()))
        for player in players[2:]:
            if player_has_statistics(player.name()) \
                    and player_has_interesting_statistics(player):
                team_para.append(
                    realizer.show_player_perf(player, realizer.player_VP, False))
        paras.append(" ".join(team_para))

    # 5 - give information about the next games for the winner and the loser
    next_games = ""
    next_game_info = next_game(winner)
    if next_game_info is not None:
        next_games += realizer.show_next_game(*next_game_info)
    next_game_info = next_game(loser)
    if next_game_info is not None:
        next_games += realizer.show_next_game(*next_game_info)
    if len(next_games) > 0:
        paras.append(next_games)
    return "\n\n".join("\n".join(wrap(para, width=paragraph_width)) for para in paras)


# useful for comparing the generated summary with the reference
# unused for the moment...
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


paragraph_width = 90


def show_summaries(game, realizers, show_data=False, show_refs=False) -> str:
    out = ["*** " + game.show_title() + "\n"]
    # show the data used for summarization
    if show_data:
        out.append(game.home().show())
        out.append("")
        out.append(game.visitors().show())
        out.append("")
    for realizer in realizers:
        realizer.set_language()  # must set the appropriate language before each summary
        out.append("*** " + realizer.name)
        gen_sum = summarize(realizer, game)
        out.append(gen_sum)
        out.append("-" * 25)
    if show_refs:
        out.append("*** " + "Reference summary")
        # orig_sum=game.references()[0]
        orig_sum = game.obj["references"][0]  # the real reference...
        out.append("\n".join(wrap(orig_sum.replace(" - ", "-"), width=paragraph_width)))
    out.append("=" * 100)
    return "\n".join(out)


def make_sample(split, k=10):
    import os
    import glob
    global games
    games = Games(split)
    set_games(games)
    out_dir = f"output/{split}"
    for f in glob.glob(out_dir+"/*"):
        os.remove(f)
    print(out_dir, "directory now empty")
    keys_sample = sample(games.keys(), k=k)
    for key in keys_sample:
        out_file = open(f"{out_dir}/{key}.txt", "w", encoding="utf-8")
        out_file.write(show_summaries(games[key], [English(), French(), FStrings()], show_data=True, show_refs=True))
        out_file.close()
        print(out_file.name, "written")


if __name__ == "__main__":
    for split in ["train", "validation", "test"]:
        make_sample(split, k=10)

    # for a single test...
    # split = "train"
    # games = Games(split)
    # set_games(games)
    # # keys_sample = sample(games.keys(), k=10)
    # keys_sample = ["1"]
    # print(f"Split: {split}")
    # for key in keys_sample:
    #     print(show_summaries(games[key], [
    #         English(),
    #         French(),
    #         FStrings(),
    #     ], show_data=False, show_refs=False))
