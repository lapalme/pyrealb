from pyrealb import *
from random import sample, randint

from pyrealb import VP

from stats import is_high
from Realizer import Realizer


class English(Realizer):
    def __init__(self, tense="ps"):
        self.tense = tense
        self.name = "English jsRealB"
        # language specifics
        loadEn()
        addToLexicon({"assist": {"N": {"tab": "n1"}}})
        addToLexicon({"three-pointer": {"N": {"tab": "n1"}}})
        addToLexicon({"free throw": {"N": {"tab": "n1"}}})
        addToLexicon({"outscore": {"V": {"tab": "v3"}}})

    best_player_VPs = [
        lambda: VP(V("score"), NP(D("a"), N("game"), Adv("high"), P("with"))),
        lambda: VP(V("finish"), P("with")),
        lambda: VP(V("lead"), NP(D("the"), N("way")).a(","), V("post").t("pr")),
        lambda: VP(V("lead"),
                   NP(D("the"), N("way"),
                      PP(P("off"), NP(D("the"), N("bench"))), V("score").t("pr"))),
        lambda: VP(V("have"), NP(D("a"), A("efficient"), N("performance")), V("score").t("pr"))
    ]

    player_VPs = [
        lambda: VP(V("score")),
        lambda: VP(V("finish"), P("with")),
        lambda: VP(V("end"), P("up"), P("with")),
        lambda: VP(V("record")),
        lambda: VP(V("post")),
        lambda: VP(V("add")),
        lambda: VP(V("contribute"), AP(D("a"), A("efficient"))),
        lambda: VP(V("have")),
    ]

    def pts_3(self, n):
        return self.nb(n, "three-pointer")

    def nb_assists(self, n):
        return self.nb(n, "assist")

    def m_for_n(self, m, n):
        return [NO(m).lier(), P("for").lier(), NO(n)]

    def team_np(self, team, with_place=False):
        return NP(D("the"),
                  Q(team.place()) if with_place else None,
                  Q(team.name())).n("p")

    def game_part(self, part):
        if part == "game":
            return NP(D("the"), N("game"))
        if part.startswith("Q"):
            return NP(D("the"), NO(int(part[1])).dOpt({"ord": True}), N("quarter"))
        if part.startswith("H"):
            return NP(D("the"), NO(int(part[1])).dOpt({"ord": True}), N("half"))
        return Q("part:" + str(part))

    def show_points_details(self, player) -> Phrase:
        cp = CP(self.pts(player.goals(), player.goals_attempted(), "FG"),
                self.pts(player.goals3(), player.goals3_attempted(), "3Pt"),
                self.pts(player.free_throws(), player.free_throws_attempted(), "FT")
                ).ba("(")
        assists = player.assists()
        if is_high("players", player.name(), "AST", assists):
            nb_as = self.nb(assists, "assist")
            if randint(0, 1) == 1:
                return S(cp,
                         SP(C("while"),
                            VP(V("add").t("pr"), nb_as)))
            else:
                return S(CP(C("and"), cp, nb_as))
        return S(cp)

    def show_winner(self, winner, loser, g_date, g_stadium, g_city) -> str:
        verb = oneOf("defeat", "top", "overcome", "knock")
        winner_scores = winner.line_scores()
        np = self.team_np(winner)
        if winner.conference_standing() == 1:
            np.a(",")
            np = NP(np,
                    NP(N("leader"),
                       PP(P("in"),
                          NP(D("my").ow("p"),
                             N("conference")))).a(","))
        vp = VP(V(verb).t(self.tense))
        if verb == "knock":
            vp.add(P("off"))
        vp.add(self.team_np(loser))
        if "OT" in winner_scores and winner_scores["OT"].points() > 0:
            vp.add(PP(P("in"), N("overtime")))
        score = self.pts(winner_scores['game'].points(), loser.line_scores()['game'].points())
        pp_date = PP(self.on_day(g_date))
        pp_place = PP(P("at"), D("the"), Q(g_stadium))
        pp_city = PP(P("in"), Q(g_city))
        return S(np, vp, score, sample([pp_date, pp_city, pp_place], k=3)).realize()

    def show_turning_points(self, winner, loser, overtime, loser_lead_in_first_half, loser_lead_in_second_half,
                            always_lead) -> str:
        out = []
        if loser_lead_in_first_half:
            out.append(CP(C("but"),
                          SP(self.team_np(loser),
                             VP(V("lead"),
                                PP(P("in"), self.game_part("H1")))),
                          SP(self.team_np(winner),
                             VP(V("manage"),
                                V("come").t("b-to"),
                                Adv("back")))))
        elif loser_lead_in_second_half:
            cp = CP(C("but"),
                    SP(self.team_np(loser),
                       VP(V("outscore"),
                          self.team_np(winner),
                          self.pts(loser.get_points()['H2'], winner.get_points()['H2']),
                          PP(P("in"), self.game_part("H2")))))
            cp.add(oneOf(
                lambda: VP(V("complete"),
                           NP(D("my").ow("p"), N("come-back"))).typ({"neg": True, "mod": "poss"}),
                lambda: SP(NP(D("the"), N("winner")),
                           VP(V("hold").t(self.tense),
                              PP(P("for"),
                                 NP(D("the"), N("win")))))
            ))
            out.append(cp)
        elif always_lead:
            out.append(S(self.team_np(winner),
                         VP(V("lead"),
                            PP(P("in"),
                               NP(D("all"), NO(4).dOpt({"nat": True}), N("quarter"))))))
        if overtime:
            out.append(S(self.team_np(winner),
                         VP(V("need"),
                            NP(N("overtime"),
                               VP(V("win").t("b-to"), self.game_part("game"))))))
        return "".join(s.t(self.tense).realize() for s in out)

    def show_team_perf(self, team) -> str:
        name = team.name()
        line_scores = team.line_scores("game")
        goals = line_scores.goals()
        free_throws = line_scores.free_throws()
        np = self.team_np(team)
        vp = VP(V("show").t(self.tense),
                CP(C("and"),
                   NP(NO(int(goals * 100 / line_scores.goals_attempted())), Q("percent"),
                      PP(P("from"), NP(D("the"), N("field")))),
                   NP(self.pts(free_throws, line_scores.free_throws_attempted()),
                      N("free throw").n("p"))))
        turnovers = line_scores.turnovers()
        if is_high("teams", name, "TOV", turnovers):
            vp.add(VP(C("and"),
                      V("commit").t(self.tense),
                      self.nb(turnovers, "turnover")))
        return S(np, vp).realize()

    def show_player_perf(self, player, vp, show_starter) -> str:
        # player [starter] vp [points] [details]
        # show global information
        name = player.name()
        vp_st = None
        if show_starter:
            vp_st = SP(Pro("who"),
                       oneOf(
                           lambda: VP(V("start"), NP(D("this"), N("game"))),
                           lambda: VP(V("be"), NP(D("a"), N("starter"))),
                           lambda: VP(V("be"), PP(P("in"),
                                                  NP(D("the"),
                                                     V("start").t("pr"),
                                                     N("line-up"))))
                       )).t("ps")
        vp = vp().t(self.tense)
        vp.add(self.nb(player.points(), "point"))
        s = S(Q(name), vp_st, vp)
        minutes = player.minutes()
        if is_high("players", name, "MIN", minutes):
            s.add(PP(P("in"), self.nb(minutes, "minute")))
        # show details in either long form or only as a list of numbers
        details = []
        if randint(0, 1) == 1:
            goals = player.goals()
            if is_high("players", name, "FGM", goals):
                details.append(oneOf(NP(self.m_for_n(goals,
                                                     player.goals_attempted()), Q("FG")),
                                     self.nb(goals, "point")))
            goals3 = player.goals3()
            if is_high("players", name, "FG3M", goals3):
                details.append(oneOf(self.pts_3(goals3),
                                     NP(self.m_for_n(goals3,
                                                     player.goals3_attempted()),
                                        PP(P("from"), P("beyond"),
                                           NP(D("the"), N("arc"))))))
            rebounds = player.rebounds()
            if is_high("players", name, "TREB", rebounds):
                reb = self.nb(rebounds, "rebound")
                details.append(oneOf(lambda: reb,
                                     lambda: VP(reb, V("grab").t("pp"))))
            assists = player.assists()
            if is_high("players", name, "AST", assists):
                details.append(self.nb_assists(assists))
            if len(details) > 0:
                details[0].add(P("with"), 0)
        else:
            details.append(self.show_points_details(player))
        double = player.double()
        if double != "none":
            details.append(NP(V("perform").t(self.tense),
                              NP(D("a"), Q(double).lier(), N("double"))))
        return s.add(CP(C("and"), details)).realize()

    def show_next_game(self, date, team_1, is_home, team_2) -> str:
        next_date = self.on_day(date)
        if is_home:
            vp = oneOf(
                lambda: VP(V("receive")),
                lambda: VP(V("play"),
                           PP(P("at"), N("home"), P("against"))),
                lambda: VP(V("be"),
                           PP(P("at"), N("home"), P("against")))
            )
            out = oneOf(
                lambda: S(PP(P("for"),
                             NP(D("my").ow("p"),
                                D("next"),
                                N("game"))).a(","),
                          self.team_np(team_1),
                          vp.add(self.team_np(team_2, True)).add(next_date)
                          ),
                lambda: S(self.team_np(team_1).a("' "),
                          D("next"), N("game"),
                          VP(V("be"),
                             PP(P("at"), N("home")),
                             PP(P("against"), self.team_np(team_2, True)),
                             next_date))
            )
        else:
            vp = oneOf(
                lambda: VP(V("visit")),
                lambda: VP(V("be"),
                           PP(P("on"), NP(D("the"), N("road")), P("against"))),
                lambda: VP(V("host"))
            )
            out = oneOf(
                lambda: S(AdvP(Adv("next"),
                               next_date.dOpt({"det": False}).a(",")),
                          self.team_np(team_1),
                          vp,
                          self.team_np(team_2, True)),

                lambda: S(AdvP(Adv("up"), Adv("next")),
                          self.team_np(team_1),
                          VP(V("travel"),
                             PP(P("to"), Q(team_2.place())),
                             VP(V("take").t("b-to"),
                                PP(P("on"),
                                   self.team_np(team_2),
                                   next_date)))))
        return out.t("f").realize()
