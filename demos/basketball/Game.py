from datetime import datetime
import re
from Player import month_number
from Team import Team


class Game:
    def __init__(self, obj):
        self.obj = obj

    def date(self):
        obj = self.obj
        return datetime(int(obj["game"]["year"]),
                        month_number[obj["game"]["month"]],
                        int(obj["game"]["day"]))

    def game_id(self):
        return self.obj["game"]["game_id"]

    def city(self):
        return self.obj["game"]["city"]

    def stadium(self):
        return self.obj["game"]["stadium"]

    def home(self):
        return Team(self.obj["teams"]["home"])

    def visitors(self):
        return Team(self.obj["teams"]["vis"])

    def summaries(self):
        # each summary is split in "sentences"
        # use references instead of summary because it is not split in tokens
        return [re.sub(r"([a-z])\. ", r"\1.\n", sum.replace(" - ", "-")) for sum in self.obj["references"]]

    def __str__(self):
        sep = "\n" + ("-" * 110) + "\n"
        return self.show_title() + \
               sep + str(self.home()) + sep + str(self.visitors()) + sep + self.show_summaries()

    def show_title(self):
        return f"{self.game_id()}: The {self.home().place()} {self.home().name()} receives" \
               f" the {self.visitors().place()} {self.visitors().name()} on {self.date().strftime('%Y-%m-%d')}"

    def show_summaries(self):
        return "---\n".join(self.summaries())
