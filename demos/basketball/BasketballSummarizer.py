import abc
class BasketballSummarizer(abc.ABC):
    @abc.abstractmethod
    def show_winner(self, winner, loser, g_date, g_stadium, g_city,
                    winning_streak_length) -> str: pass
    @abc.abstractmethod
    def show_turning_points(self, winner, loser, overtime, loser_lead_in_first_half,
                            loser_lead_in_second_half, always_lead) -> str: pass
    @abc.abstractmethod
    def show_team_perf(self, team) -> str:pass
    @abc.abstractmethod
    def show_player_perf(self, player, vp_func, show_starter) -> str: pass
    @abc.abstractmethod
    def show_next_game(self, date, team_1, is_home, team_2) -> str: pass
