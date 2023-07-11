from Player import Player
from Score import Score

class Team:
    def __init__(self, obj):
        self.obj = obj
        # patch computation of H1 and H2 values but store them as string for further processing
        scores = self.obj["line_score"]
        for key in Score.score_titles:
            if key in scores["H1"]:
                scores["H1"][key] = str(int(scores["Q1"][key])+int(scores["Q2"][key]))
                scores["H2"][key] = str(int(scores["Q3"][key])+int(scores["Q4"][key]))

    def __str__(self):
        w = Score.score_width+1
        lines = [("",self.show_name().center(len(Score.score_top_line())))]
        lines.append(("Game".center(20),  " "*2*w + Score.score_top_line()))
        for key in ["Q1","Q2","Q3","Q4","OT","game"]:
            if key !="OT" or self.line_scores("OT").points()>0:
                lines.append((key, " "*2*w + str(self.line_scores(key))))
        lines.append(("PLAYER".center(20), f" STRT| MIN |" + Score.score_top_line()))
        for bs in self.players_scores():
            lines.append((bs.name(), str(bs)))
        return "\n".join(f"{key[:20]:20}|{val}" for key, val in lines)

    def name(self):
        return self.obj["name"]

    def place(self):
        return self.obj["place"]

    def wins(self):
        return int(self.obj["wins"])

    def losses(self):
        return int(self.obj["losses"])

    def previous_game_id(self):
        return int(self.obj["previous_game_id"]) if self.obj["previous_game_id"] != 'null' else 0

    def conference_standing(self):
        return int(self.obj["conference_standing"])

    def next_game_id(self):
        return int(self.obj["next_game_id"]) if len(self.obj["next_game_id"]) > 0 else 0

    def line_scores(self, key=None):
        if key is None:
            return {key: Score(self.obj["line_score"][key]) for key in self.obj["line_score"].keys()}
        return Score(self.obj["line_score"][key])

    def get_points(self) -> [int]:
        # accumulation of points after each quarter [0-3], overtime[4] and half-time [5,6]
        pts = {q: self.line_scores(q).points() for q in ["Q1", "Q2", "Q3", "Q4", "OT","H1","H2"]}
        # pts["H1"] = pts["Q1"] + pts["Q2"]
        # pts["H2"] = pts["Q3"] + pts["Q4"]
        return pts

    # return box scores in descending order of points
    def players_scores(self):
        return [Player(bs_obj) for bs_obj in sorted(self.obj["box_score"],
                                                    key=lambda o: int(o["PTS"]), reverse=True)]

    def show_name(self):
        return f"{self.place()} {self.name()} ({self.wins()}-{self.losses()})"

