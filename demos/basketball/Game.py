from datetime import datetime
import re, calendar
from Team import Team

month_number = {calendar.month_name[i]: i for i in range(1, 13)}

class Game:
    def __init__(self, obj):
        self.obj = obj
        self.home_team = Team(self.obj["teams"]["home"],self)
        self.visitors_team = Team(self.obj["teams"]["vis"],self)

    def date(self) -> datetime:
        obj = self.obj
        return datetime(int(obj["game"]["year"]),
                        month_number[obj["game"]["month"]],
                        int(obj["game"]["day"]))

    def game_id(self) -> str:
        return self.obj["game"]["game_id"]

    def city(self) -> str:
        return self.obj["game"]["city"]

    def stadium(self) -> str:
        return self.obj["game"]["stadium"]

    def home(self) -> Team:
        return self.home_team

    def visitors(self) -> Team:
        return self.visitors_team

    def winner(self) -> Team:
        if self.home().final_score() > self.visitors().final_score():
            return self.home()
        else:
            return self.visitors()

    def reference_sentences(self) -> [str]:
        # each summary is split in "sentences"
        # use references instead of summary because it is not split in tokens
        return [re.sub(r"([a-z])\. ", r"\1.\n", sum.replace(" - ", "-")) for sum in self.obj["references"]]

    def show(self) -> str:
        sep = "\n" + ("-" * 110) + "\n"
        return self.show_title() + \
               sep + self.home().show() + sep + self.visitors().show() + sep + self.show_references()

    def show_title(self) -> str:
        return f"{self.game_id():>5}:{self.date().strftime('%Y-%m-%d')}: {self.home().place()} {self.home().name()} receives" \
               f" {self.visitors().place()} {self.visitors().name()} "\
               f" [{self.home().final_score()}-{self.visitors().final_score()}]"

    def show_references(self) -> str:
        return "---\n".join(self.reference_sentences())
