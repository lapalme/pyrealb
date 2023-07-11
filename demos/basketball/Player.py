import calendar,datetime

from Score import Score

month_number = {calendar.month_name[i]:i for i in range(1,13)}

class Player(Score):
    def __init__(self,obj):
        self.obj = obj
        super().__init__(obj)

    def name(self):
        return self.obj["name"]
    def starter(self):
        return self.obj["starter"]
    def minutes(self):
        return int(self.obj["MIN"])
    def double(self):
        return self.obj["DOUBLE"]

    def __str__(self):
        return f"{self.starter():{Score.score_width}}|{self.minutes():{Score.score_width}}|" + \
               super().__str__()
