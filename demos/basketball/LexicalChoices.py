from pyrealb import *
import abc

class LexicalChoices(abc.ABC):
    @abc.abstractmethod
    def conjunction(self,*elems) -> C: pass

    @abc.abstractmethod
    def with_p(self) -> P: pass

    @abc.abstractmethod
    def on_day(self, date) -> DT: pass

    @abc.abstractmethod
    def pts_3(self, n) -> NP: pass

    @abc.abstractmethod
    def nb_assists(self, n) -> NP: pass

    @abc.abstractmethod
    def m_for_n(self, m, n) -> [Terminal]: pass

    @abc.abstractmethod
    def team_np(self, team, with_place=False, wins_losses=False) -> NP: pass

    @abc.abstractmethod
    def pts_abbrev(self,name)->str: pass

    @abc.abstractmethod
    def game_part(self, part) -> Constituent: pass

    #####################################################################
    #  show_winner
    @abc.abstractmethod
    def stadium_pp(self, stadium) -> PP: pass

    @abc.abstractmethod
    def city_pp(self, city) -> PP: pass

    @abc.abstractmethod
    def team_winning_streak_vp(self, streak_length) -> Phrase: pass

    @abc.abstractmethod
    def team_losing_streak_vp(self, team, streak_length) -> Phrase: pass

    @abc.abstractmethod
    def conference_leader(self, winner_np) -> NP: pass

    @abc.abstractmethod
    def defeat_vp(self,nb_points:int) -> VP: pass

    @abc.abstractmethod
    def overtime_pp(self, minutes): pass

    #####################################################################
    #  show_turning_points
    @abc.abstractmethod
    def loser_lead_in_first_half(self, winner, loser) -> CP: pass

    @abc.abstractmethod
    def loser_lead_in_second_half(self, winner, loser) -> CP: pass

    @abc.abstractmethod
    def always_lead(self, winner) -> S: pass

    @abc.abstractmethod
    def in_overtime(self, winner): pass

    #####################################################################
    #   show_team_perf
    @abc.abstractmethod
    def show_goals_vp(self, goals, line_scores) -> VP: pass

    @abc.abstractmethod
    def show_turnovers_vp(self, turnovers): pass

    @abc.abstractmethod
    def show_team_fact(self, winner, loser, fact): pass
    # fact: (period:str,score:str,winner_val:int,loser_val:int,diff:int)

    #####################################################################
    #  show_player_perf
    @abc.abstractmethod
    def best_player_VP(self): pass

    @abc.abstractmethod
    def player_VP(self): pass

    @abc.abstractmethod
    def starter_player(self) -> SP: pass

    @abc.abstractmethod
    def season_high(self) -> NP: pass

    @abc.abstractmethod
    def nb_minutes_played(self, minutes) -> PP: pass

    @abc.abstractmethod
    def goals_made(self, player, goals) -> NP: pass

    @abc.abstractmethod
    def three_pointers(self, player, goals3) -> NP: pass

    @abc.abstractmethod
    def rebounds(self, rebounds) -> Phrase: pass

    @abc.abstractmethod
    def doubles(self, double) -> VP: pass

    @abc.abstractmethod
    def points_details(self, player) -> CP: pass

    @abc.abstractmethod
    def with_assists(self, details, assists) -> S: pass

    #####################################################################
    # show_next_game
    @abc.abstractmethod
    def next_game_home(self, team_1, team_2, next_date) -> S: pass

    @abc.abstractmethod
    def next_game_visitor(self, team_1, team_2, next_date) -> S: pass
