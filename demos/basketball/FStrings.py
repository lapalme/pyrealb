from random import choice, randint
from stats import is_high

class FStrings:
    def __init__(self):
        self.name = "English FStrings"

    best_player_VPs = ["scored a game high with",
                         "finished with",
                         "lead the way with",
                         "filled the stat sheet, posting",
                         "lead the way off the bench scoring",
                         "had efficient performance scoring",
    ]

    player_VPs = ["scored",
                  "finished with",
                  "ended up with",
                  "recorded",
                  "posted",
                  "added",
                  "contributed an efficient",
                  "had"
    ]

    def show_points_details(self,player) -> str:
        out = f"({player.goals()}-{player.goals_attempted()} FG, "
        out += f"{player.goals3()}-{player.goals3_attempted()} 3Pt, "
        out += f"{player.free_throws()}-{player.free_throws_attempted()} FT)"
        assists = player.assists()
        if assists > 4:
            out += choice((" while adding ", " and ")) + f"{assists} assists"
        return out

    def show_winner(self,winner, loser, g_date, g_stadium, g_city) -> str:
        verb = choice(("defeated", "topped", "overcame", "knocked off"))
        winner_scores = winner.line_scores()
        out = f"The "+winner.show_name()
        if winner.conference_standing()==1:
            out += ", leader in their conference, "
        out += verb +" the "+ loser.show_name()
        if "OT" in winner_scores and winner_scores["OT"].points() > 0:
            out += " in overtime"
        out += f" {winner_scores['game'].points()}-{loser.line_scores()['game'].points()}"
        out += g_date.strftime(" on %A ") + f"at the {g_stadium} in {g_city}. "
        return out



    def show_turning_points(self,winner,loser,overtime,loser_lead_in_first_half,loser_lead_in_second_half,always_lead) -> str:
        out = []
        if loser_lead_in_first_half:
            out.append(f"The {loser.name()} lead in the first half, but the {winner.name()} managed to come back.")
        elif loser_lead_in_second_half:
            out.append((f"The {loser.name()} outscored the {winner.name()} ({loser.get_points()['H2']}-{winner.get_points()['H2']}) "
                       f"in the second half, ")+
                       choice(("but they could not complete their comeback.",
                               f"but the {winner.place()} held on for the win.")))
        elif always_lead:
            out.append(f"The {winner.name()} lead in all four quarters.")
        if overtime:
            out.append(f"The {winner.name()} needed overtime to win the game.")
        return "".join(out)

    def show_team_perf(self, team) -> str:
        name = team.name()
        line_scores = team.line_scores("game")
        goals = line_scores.goals()
        free_throws = line_scores.free_throws()
        out = (f"The {name} show {int(goals * 100 / line_scores.goals_attempted())} percent from the field and "
               f"{free_throws}-of-{line_scores.free_throws_attempted()} free throws")
        turnovers = line_scores.turnovers()
        if is_high("teams", name, "TOV", turnovers):
            out += f" and committed {turnovers} turnovers"
        return out + "."

    def show_player_perf(self, player, vp,starter) -> str:
        def make_coord(elems: [str]) -> str:
            if len(elems) == 0:
                return ""
            if len(elems) == 1:
                return elems[0] + ". "
            return ", ".join(elems[:-1]) + " and " + elems[-1] + ". "

        name = player.name()
        start = name
        if starter and randint(1,2)==1:
            start += " "+choice((f"started this game",f"was a starter",f"was in the starting line-up"))+" and"
        start += f" {vp} {player.points()} points"
        minutes = player.minutes()
        if minutes > 20:  # is_high("players",name, "MIN",minutes):
            start += f" in {minutes} minutes"
        elems = [start]
        c = randint(0, 1)
        if c == 0:
            goals = player.goals()
            if is_high("players",name,"FGM",goals):
                elems.append(choice((f"{goals}-for-{player.goals_attempted()}",f"{goals} goals")))
            goals3 = player.goals3()
            if is_high("players", name, "FG3M", goals3):
                elems.append(choice((f"{goals3} three-pointers",
                                     f"{goals3}-for-{player.goals3_attempted()} from beyond the arc")))
            rebounds = player.rebounds()
            if is_high("players", name, "TREB", rebounds):
                elems.append(choice(("","grabbing "))+f"{rebounds} rebounds")
            assists = player.assists()
            if is_high("players", name, "AST", assists):
                elems.append(f"{assists} assists")
        else:
            elems[0] += " " + self.show_points_details(player)
        double = player.double()
        if double != "none":
            elems.append(f"performed a {double}-double")
        return make_coord(elems)


    def show_next_game(self,date,team_1,is_home,team_2) -> str:
        next_date = date.strftime('%A')
        name1 = team_1.name()
        name2 = team_2.name()
        place2 = team_2.place()
        if is_home:
            verb = choice(("will receive", "will play at home against", "will be at home against"))
            return choice((
                f"For their next game, the {name1} {verb} the {place2} {name2} on {next_date}. ",
                f"The {name1}' next game will be at home against the {name2} next {next_date}. "
            ))
        else:
            if randint(0, 1) == 0:
                verb = choice(("will visit", "will be on the road against", "will host"))
                return f"Next {next_date}, the {name1} {verb} the {place2} {name2}. "
            else:
                return (f"Up next, the {name1} travel to {place2}"
                        f" to take on the {name2} on {next_date}. ")
