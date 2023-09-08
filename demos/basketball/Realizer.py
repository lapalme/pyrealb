from pyrealb import *
from stats import is_high
from random import sample
from seasons_stats import is_season_high_player
from BasketballSummarizer import BasketballSummarizer
from LexicalChoices import LexicalChoices
from game_stats import get_most_interesting

#  Language independent realizer
#    language dependent formulations are in subclasses implementing "LexicalChoices" abstract base class
class Realizer(BasketballSummarizer,LexicalChoices):
    # output number in letters if 12 or less
    def no(self, val) -> NO:
        return NO(val).dOpt({"nat": val < 13})

    def nb(self, val, n) -> NP:
        return NP(self.no(val), N(n) if isinstance(n, str) else n)

    def pts(self, val1, val2, postfix=None) -> NP:
        return NP(NO(val1).lier(), NO(val2), Q(postfix) if postfix is not None else None)

    def show_winner(self, winner, loser, g_date, g_stadium, g_city, winning_streak_length) -> str:
        show_wins_losses = True  # oneOf([True,False])
        winner_np = self.team_np(winner, wins_losses=show_wins_losses)
        if winner.conference_standing() == 1:
            winner_np = self.conference_leader(winner_np)
        vp = self.defeat_vp(winner.final_score()-loser.final_score())
        vp.add(self.team_np(loser, wins_losses=show_wins_losses))
        minutes_overtime = winner.minutes_overtime()
        if minutes_overtime > 0:
            vp.add(self.overtime_pp(minutes_overtime))
        score = self.pts(winner.final_score(), loser.final_score())
        date_place_city = sample([PP(self.on_day(g_date)),
                                  self.city_pp(g_city),
                                  self.stadium_pp(g_stadium)], k=3)
        winning_str = None if winning_streak_length <= 2 \
            else self.team_winning_streak_vp(winning_streak_length)
        return S(winner_np, vp, score, date_place_city, winning_str).realize()

    def show_turning_points(self, winner, loser, overtime, loser_lead_in_first_half, loser_lead_in_second_half,
                            always_lead) -> str:
        out = []
        if loser_lead_in_first_half:
            out.append(self.loser_lead_in_first_half(winner, loser))
        elif loser_lead_in_second_half:
            out.append(self.loser_lead_in_second_half(winner, loser))
        elif always_lead:
            out.append(self.always_lead(winner))
        if overtime:
            out.append(self.in_overtime(winner))
        return "".join(S(s.t(self.t())).realize() for s in out)

    def show_team_facts(self,winner,loser,interesting) -> str:
        return "".join(self.show_team_fact(winner, loser, fact).t(self.t()).realize()
                       for fact in get_most_interesting(interesting))

    def show_team_perf(self, team) -> str:
        name = team.name()
        line_scores = team.period_scores["game"]
        goals = line_scores.goals()
        np = self.team_np(team)
        vp = self.show_goals_vp(goals, line_scores)
        turnovers = line_scores.turnovers()
        if is_high("teams", name, "TOV", turnovers):
            vp.add(self.show_turnovers_vp(turnovers))
        return S(np, vp).realize()

    def show_points(self, player) -> [Phrase]:
        details = []
        name = player.name()
        scores = player.scores
        goals = scores.goals()
        if is_high("players", name, "FGM", goals):
            details.append(oneOf(NP(self.m_for_n(goals,
                                                 scores.goals_attempted()),
                                    Q(self.pts_abbrev("FG"))),
                                 self.goals_made(player,goals)))
        goals3 = scores.goals3()
        if is_high("players", name, "FG3M", goals3):
            details.append(self.three_pointers(player, goals3))
        rebounds = scores.rebounds()
        if is_high("players", name, "TREB", rebounds):
            details.append(self.rebounds(rebounds))
        assists = scores.assists()
        if is_high("players", name, "AST", assists):
            details.append(self.nb_assists(assists))
        if len(details) > 0:
            details[0].add(self.with_p(), 0)
        return details

    def show_points_details(self, player) -> Phrase:
        details = self.points_details(player)
        assists = player.scores.assists()
        if is_high("players", player.name(), "AST", assists):
            return self.with_assists(details, assists)

    def show_player_perf(self, player,vp_func,show_starter) -> str:
        # player [starter] vp [points] [details]
        # show global information
        name = player.name()
        vp_st = None
        if show_starter:
            vp_st = self.starter_player()
        vp = vp_func().t(self.t())
        np_pts = self.nb(player.scores.points(), "point")
        if is_season_high_player(player, "PTS", player.scores.points()):
            np_pts.add(self.season_high())
        vp.add(np_pts)
        s = S(Q(name), vp_st, vp)
        minutes = player.scores.minutes()
        if is_high("players", name, "MIN", minutes):
            s.add(self.nb_minutes_played(minutes))
        # show details in either long form or only as a list of numbers
        details = []
        details.append(oneOf(
            lambda: self.show_points(player),
            lambda: self.show_points_details(player)
        ))
        double = player.double()
        if double != "none":
            details.append(self.doubles(double))
        return s.add(self.conjunction(details)).realize()

    def show_next_game(self, date, team_1, is_home, team_2) -> str:
        next_date = self.on_day(date)
        if is_home:
            return self.next_game_home(team_1, team_2, next_date).t("f").realize()
        else:
            return self.next_game_visitor(team_1, team_2, next_date).t("f").realize()
