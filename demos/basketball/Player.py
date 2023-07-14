import calendar

from Score import Score

month_number = {calendar.month_name[i]: i for i in range(1, 13)}


class Player(Score):
    def __init__(self, obj):
        self.obj = obj
        super().__init__(obj)

    def name(self) -> str:
        return self.obj["name"]

    def starter(self) -> bool:
        return self.obj["starter"]

    def minutes(self) -> int:
        return int(self.obj["MIN"])

    def double(self) -> str:
        return self.obj["DOUBLE"]

    def __str__(self) -> str:
        return f"{self.starter():{Score.score_width}}|{self.minutes():{Score.score_width}}|" + \
               super().__str__()
