
class Score:
    score_titles = ["MIN", "FGM", "FGA", "FG3M", "FG3A", "FTM", "FTA", "OREB", "TREB", "AST", "STL", "BLK", "TOV", "PF",
                    "PTS", "+/-"]
    score_width = 5

    def __init__(self, score_dict):
        self.score_dict = score_dict

    def show(self) -> str:
        return "|".join([f"{self.score_dict[k] if k in self.score_dict else '':{Score.score_width}}"
                         for k in Score.score_titles])

    def minutes(self) -> int:
        return self.score_dict["MIN"]

    def goals(self) -> int:
        return self.score_dict["FGM"]

    def goals_attempted(self) -> int:
        return self.score_dict["FGA"]

    def goals3(self) -> int:
        return self.score_dict["FG3M"]

    def goals3_attempted(self) -> int:
        return self.score_dict["FG3A"]

    def free_throws(self) -> int:
        return self.score_dict["FTM"]

    def free_throws_attempted(self) -> int:
        return self.score_dict["FTA"]

    def offensive_rebounds(self) -> int:
        return self.score_dict["OREB"]

    def rebounds(self) -> int:
        return self.score_dict["TREB"]

    def assists(self) -> int:
        return self.score_dict["AST"]

    def steals(self) -> int:
        return self.score_dict["STL"]

    def blocks(self) -> int:
        return self.score_dict["BLK"]

    def turnovers(self) -> int:
        return self.score_dict["TOV"]

    def fouls(self) -> int:
        return self.score_dict["PF"] if "PF" in self.score_dict else 0

    def plus_minus(self) -> int:
        return self.score_dict["+/-"]

    def points(self) -> int:
        return self.score_dict["PTS"]

    def allScores(self) -> dict[str, int]:
        return {key: int(self.score_dict[key]) for key in Score.score_titles
                     if key in self.score_dict}

    @classmethod
    def score_top_line(cls) -> str:
        return "|".join(s.center(Score.score_width) for s in Score.score_titles)
