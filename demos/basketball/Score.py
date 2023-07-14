class Score:
    score_titles = ["MIN", "FGM", "FGA", "FG3M", "FG3A", "FTM", "FTA", "OREB", "TREB", "AST", "STL", "BLK", "TOV", "PF",
                    "PTS",
                    "+/-"]
    score_width = 5

    def __init__(self, obj):
        self.obj = obj

    def __str__(self) -> str:
        all_scores = self.allScores()
        return "|".join([f"{all_scores[k] if k in all_scores else '':{Score.score_width}}" for k in Score.score_titles])

    def goals(self) -> int:
        return int(self.obj["FGM"])

    def goals_attempted(self) -> int:
        return int(self.obj["FGA"])

    def goals3(self) -> int:
        return int(self.obj["FG3M"])

    def goals3_attempted(self) -> int:
        return int(self.obj["FG3A"])

    def free_throws(self) -> int:
        return int(self.obj["FTM"])

    def free_throws_attempted(self) -> int:
        return int(self.obj["FTA"])

    def offensive_rebounds(self) -> int:
        return int(self.obj["OREB"])

    def rebounds(self) -> int:
        return int(self.obj["TREB"])

    def assists(self) -> int:
        return int(self.obj["AST"])

    def steals(self) -> int:
        return int(self.obj["STL"])

    def blocks(self) -> int:
        return int(self.obj["BLK"])

    def turnovers(self) -> int:
        return int(self.obj["TOV"])

    def fouls(self) -> int:
        return int(self.obj["PF"])

    def plus_minus(self) -> int:
        return int(self.obj["+/-"])

    def points(self) -> int:
        return int(self.obj["PTS"])

    def allScores(self) -> dict[str, int]:
        return {key: int(self.obj[key]) for key in Score.score_titles if key in self.obj}

    @classmethod
    def score_top_line(cls) -> str:
        return "|".join(s.center(Score.score_width) for s in Score.score_titles)
