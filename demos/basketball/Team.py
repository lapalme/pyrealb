from typing import Union
from Player import Player
from Score import Score

period_names = ["Q1", "Q2", "Q3", "Q4", "OT", "H1", "H2", "game"]


class Team:
    def __init__(self, obj, this_game):
        self.obj = obj
        self.this_game = this_game
        #   patch all the data
        # transform all line scores from str to int
        for key in ["wins", "losses", "conference_standing"]:
            self.obj[key] = int(self.obj[key])
        line_score = obj["line_score"]
        for game_part in line_score:
            for key in Score.score_titles:
                if key in line_score[game_part]:
                    line_score[game_part][key] = int(line_score[game_part][key])
        # patch computation of H1 and H2 values but store them as string as for the other scores
        for key in Score.score_titles:
            if key in line_score["H1"]:
                line_score["H1"][key] = line_score["Q1"][key] + line_score["Q2"][key]
                line_score["H2"][key] = line_score["Q3"][key] + line_score["Q4"][key]
        # patch minutes for game that all have "4" as value...
        line_score["game"]["MIN"] = sum(line_score[k]["MIN"] for k in ["Q1", "Q2", "Q3", "Q4", "OT"])
        self.period_scores = {name: Score(line_score[name]) for name in period_names}
        self.players = [Player(player, this_game, self.name()) for player in obj["box_score"]]

    def show(self, show_players=True) -> str:
        w = Score.score_width + 1
        lines = [("", self.show_name().center(len(Score.score_top_line())))]
        lines.append(("Game".center(20), " " * 2 * w + Score.score_top_line()))
        for key in period_names:
            if key != "OT" or self.period_scores["OT"].minutes() > 0:
                lines.append((key, " " * 2 * w + self.period_scores[key].show()))
        if show_players:
            lines.append(("PLAYER".center(20), Player.player_top_line()))
            for player in self.players_sorted():
                lines.append((player.name(), player.show()))
        return "\n".join(f"{key[:20]:20}|{val}" for key, val in lines)

    def name(self) -> str:
        return self.obj["name"]

    def place(self) -> str:
        return self.obj["place"]

    def wins(self) -> int:
        return self.obj["wins"]

    def losses(self) -> int:
        return self.obj["losses"]

    def conference_standing(self) -> int:
        return self.obj["conference_standing"]

    def previous_game_id(self) -> str:
        return self.obj["previous_game_id"]

    def next_game_id(self) -> str:
        # make next_game_id use the same convention as previous_game_id instead of ""
        return self.obj["next_game_id"] if len(self.obj["next_game_id"]) > 0 else "null"

    #   useful auxiliary methods
    def player_names(self) -> [str]:
        return [player.name() for player in self.players]

    def get_player(self, name: str) -> Player:
        for player in self.players:
            if player.name() == name:
                return player
        return None

    # return players in descending order of points
    def players_sorted(self) -> [Player]:
        return sorted(self.players, key=lambda p: p.scores.points(), reverse=True)

    def show_name(self) -> str:
        return f"{self.place()} {self.name()} ({self.wins()}-{self.losses()})"

    def get_points(self, key: str = None) -> Union[dict[str, int], int]:
        if key is None:
            return {q: self.period_scores[q].points() for q in self.period_scores.keys()}
        if key not in self.period_scores:
            return 0
        return self.period_scores[key].points()

    def final_score(self) -> int:
        return self.period_scores["game"].points()

    def minutes_overtime(self) -> int:
        if "OT" not in self.period_scores:
            return 0
        return self.period_scores["OT"].minutes()
