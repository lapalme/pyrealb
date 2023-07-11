class Score:
    score_titles = ["MIN", "FGM", "FGA", "FG3M", "FG3A", "FTM", "FTA", "OREB", "TREB", "AST", "STL", "BLK", "TOV", "PF", "PTS",
                    "+/-"]
    score_width = 5

    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        all_scores=self.allScores()
        return "|".join([f"{all_scores[k] if k in all_scores else '':{Score.score_width}}" for k in Score.score_titles])

    def goals(self):
        return int(self.obj["FGM"])

    def goals_attempted(self):
        return int(self.obj["FGA"])

    def goals3(self):
        return int(self.obj["FG3M"])

    def goals3_attempted(self):
        return int(self.obj["FG3A"])

    def free_throws(self):
        return int(self.obj["FTM"])

    def free_throws_attempted(self):
        return int(self.obj["FTA"])

    def offensive_rebounds(self):
        return int(self.obj["OREB"])

    def rebounds(self):
        return int(self.obj["TREB"])

    def assists(self):
        return int(self.obj["AST"])

    def steals(self):
        return int(self.obj["STL"])

    def blocks(self):
        return int(self.obj["BLK"])

    def turnovers(self):
        return int(self.obj["TOV"])

    def fouls(self):
        return int(self.obj["PF"])

    def plus_minus(self):
        return int(self.obj["+/-"])

    def points(self):
        return int(self.obj["PTS"])

    def allScores(self):
        return {key: int(self.obj[key]) for key in Score.score_titles if key in self.obj}

    @classmethod
    def score_top_line(cls):
        return "|".join(s.center(Score.score_width) for s in Score.score_titles)
