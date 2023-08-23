from Score import Score

class Player:
    def __init__(self, obj,this_game,team_name):
        self.this_game = this_game
        self.team_name = team_name
        # transform all values from str to int
        self.scores = Score({key:int(obj[key]) for key in Score.score_titles})
        self.my_name = obj["name"]
        self.is_starter = obj["starter"]
        self.has_double = obj["DOUBLE"]
        
    def show(self) -> str:
        scores = self.scores
        return f"{self.starter():{Score.score_width}}|" + \
               f'{"" if self.double() == "none" else self.double()[:Score.score_width]:{Score.score_width}}|' + \
               scores.show()

    def name(self) -> str:
        return self.my_name

    def starter(self) -> bool:
        return self.is_starter

    def double(self) -> str:
        return self.has_double

    @classmethod
    def player_top_line(cls) -> str:
        return "".join(f"{t:^{Score.score_width}}|" for t in ["Strtr","DBL"])+\
            Score.score_top_line()