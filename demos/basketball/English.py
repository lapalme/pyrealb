from pyrealb import *
from Realizer import Realizer
from LexicalChoices import LexicalChoices

class English(Realizer,LexicalChoices):
    def __init__(self, tense="ps"):
        self.tense = tense
        self.name = "English jsRealB"
        # language specifics
        loadEn()
        addToLexicon({"assist": {"N": {"tab": "n1"}}})
        addToLexicon({"three-pointer": {"N": {"tab": "n1"}}})
        addToLexicon({"free throw": {"N": {"tab": "n1"}}})
        addToLexicon({"outscore": {"V": {"tab": "v3"}}})

    def set_language(self):
        loadEn()


    def t(self) -> str:
        return self.tense

    # frequent recurring expressions
    def conjunction(self,*elems) -> CP:
        return CP(C("and"),*elems)

    def with_p(self) -> P:
        return P("with")

    def pts_3(self, n) -> NP:
        return self.nb(n, "three-pointer")

    def nb_assists(self, n) -> NP:
        return self.nb(n, "assist")

    def m_for_n(self, m, n) -> [Terminal]:
        return [NO(m).lier(), P("for").lier(), NO(n)]

    def team_np(self, team, with_place=False, wins_losses=False) -> NP:
        return NP(D("the"),
                  Q(team.place()) if with_place else None,
                  Q(team.name()),
                  self.pts(team.wins(), team.losses()).ba("(") if wins_losses else None
                  ).n("p")

    def game_part(self, part) -> Constituent:
        if part == "game":
            return NP(D("the"), N("game"))
        if part.startswith("Q"):
            return NP(D("the"), NO(int(part[1])).dOpt({"ord": True}), N("quarter"))
        if part.startswith("H"):
            return NP(D("the"), NO(int(part[1])).dOpt({"ord": True}), N("half"))
        return Q("part:" + str(part))

    #  show_points_details
    def points_details(self, player) -> CP:
        scores = player.scores
        return CP(self.pts(scores.goals(), scores.goals_attempted(), "FG"),
                  self.pts(scores.goals3(), scores.goals3_attempted(), "3Pt"),
                  self.pts(scores.free_throws(), scores.free_throws_attempted(), "FT")
                  ).ba("(")

    def with_assists(self, details, assists) -> S:
        nb_as = self.nb_assists(assists)
        return  oneOf(
            lambda: S(details,
                      SP(C("while"),
                         VP(V("add").t("pr"), nb_as))),
            lambda: S(CP(C("and"), details, nb_as))
        )

    #  show_winner
    def stadium_pp(self, stadium) -> PP:
        return PP(P("at"), D("the"), Q(stadium))

    def city_pp(self, city) -> PP:
        return PP(P("in"), Q(city))

    def team_winning_streak_vp(self, streak_length) -> VP:
        return VP(V("give").t("pr"),
                  Pro("them").n("p").c("dat"),
                  NP(D("my").ow("p"),
                     NO(streak_length).dOpt({"ord": True}),
                     A("straight"),
                     N("victory")))

    def conference_leader(self, winner_np) -> NP:
        return NP(winner_np.a(","),
                  NP(N("leader"),
                     PP(P("in"),
                        NP(D("my").ow("p"),
                           N("conference")))).a(","))

    def defeat_vp(self) -> VP:
        verb =  oneOf("defeat", "top", "overcome", "knock")
        vp = VP(V(verb).t(self.tense))
        if verb == "knock":
            vp.add(P("off"))
        return vp

    def overtime_pp(self, minutes):
        return PP(P("in"),
                  A("triple") if minutes > 50 else A("double") if minutes > 25 else None,
                  N("overtime"))

    #  show_turning_points
    def loser_lead_in_first_half(self, winner, loser) -> CP:
        return CP(C("but"),
                  SP(self.team_np(loser),
                     VP(V("lead"),
                        PP(P("in"), self.game_part("H1")))),
                  SP(self.team_np(winner),
                     VP(V("manage"),
                        V("come").t("b-to"),
                        Adv("back"))))

    def loser_lead_in_second_half(self, winner, loser) -> CP:
        cp = CP(C("but"),
                SP(self.team_np(loser),
                   VP(V("outscore").t(self.tense),
                      self.team_np(winner),
                      self.pts(loser.get_points('H2'), winner.get_points('H2')),
                      PP(P("in"), self.game_part("H2")))))
        cp.add( oneOf(
            lambda: VP(V("complete"),
                       NP(D("my").ow("p"), N("come-back"))).typ({"neg": True, "mod": "poss"}),
            lambda: SP(NP(D("the"), N("winner")),
                       VP(V("hold").t(self.tense),
                          PP(P("for"),
                             NP(D("the"), N("win")))))
        ))
        return cp

    def always_lead(self, winner) -> S:
        return S(self.team_np(winner),
                 VP(V("lead").t(self.tense),
                    PP(P("in"),
                       NP(D("all"), NO(4).dOpt({"nat": True}), N("quarter")))))

    def in_overtime(self, winner):
        return S(self.team_np(winner),
                 VP(V("need").t(self.tense),
                    NP(N("overtime"),
                       VP(V("win").t("b-to"), self.game_part("game")))))

    #   show_team_perf
    def show_goals_vp(self, goals, line_scores) -> VP:
        return VP(V("show").t(self.tense),
                  CP(C("and"),
                     NP(NO(int(goals * 100 / line_scores.goals_attempted())), Q("percent"),
                        PP(P("from"), NP(D("the"), N("field")))),
                     NP(self.pts(line_scores.free_throws(), line_scores.free_throws_attempted()),
                        N("free throw").n("p"))))

    def show_turnovers_vp(self, turnovers):
        return VP(C("and"),
                  V("commit").t(self.tense),
                  self.nb(turnovers, "turnover"))

    #  show_player_perf
    def best_player_VP(self) -> VP:
        return  oneOf(
            lambda: VP(V("score"), NP(D("a"), N("game"), Adv("high"), P("with"))),
            lambda: VP(V("finish"), P("with")),
            lambda: VP(V("lead"), NP(D("the"), N("way")).a(","), V("post").t("pr")),
            lambda: VP(V("lead"),
                       NP(D("the"), N("way"),
                          PP(P("off"), NP(D("the"), N("bench"))), V("score").t("pr"))),
            lambda: VP(V("have"), NP(D("a"), A("efficient"), N("performance")), V("score").t("pr"))
        )

    def player_VP(self) -> VP:
        return  oneOf(
            lambda: VP(V("score")),
            lambda: VP(V("finish"), P("with")),
            lambda: VP(V("end"), P("up"), P("with")),
            lambda: VP(V("record")),
            lambda: VP(V("post")),
            lambda: VP(V("add")),
            lambda: VP(V("contribute"), AP(D("a"), A("efficient"))),
            lambda: VP(V("have"))
        )

    def starter_player(self) -> SP:
        return SP(Pro("who"),
                   oneOf(
                      lambda: VP(V("start"), NP(D("this"), N("game"))),
                      lambda: VP(V("be"), NP(D("a"), N("starter"))),
                      lambda: VP(V("be"), PP(P("in"),
                                             NP(D("the"),
                                                V("start").t("pr"),
                                                N("line-up"))))
                  ).t("ps"))

    def season_high(self) -> NP:
        return oneOf(
            NP(D("a"), N("season"), Adv("high")),
            NP(D("a"),A("personal"),N("record"),
               PP(P("for"),NP(D("the"),N("season"))))
        )

    def nb_minutes_played(self, minutes) -> PP:
        return PP(P("in"), self.nb(minutes, "minute"))

    def goals_made(self, player, goals) -> NP:
        return self.nb(goals,"goal")

    def three_pointers(self, player, goals3) -> NP:
        return  oneOf(lambda: self.pts_3(goals3),
                       lambda: NP(self.m_for_n(goals3,
                                               player.scores.goals3_attempted()),
                                  PP(P("from"), P("beyond"),
                                     NP(D("the"), N("arc")))))

    def rebounds(self, rebounds) -> Phrase:
        reb = self.nb(rebounds, "rebound")
        return  oneOf(lambda: reb,
                       lambda: VP(reb, V("grab").t("pp")))

    def doubles(self, double) -> VP:
        return VP(V("perform").t(self.tense),
                  NP(D("a"), Q(double).lier(), N("double")))

    # show_next_game
    def next_game_home(self, team_1, team_2, next_date) -> S:
        vp =  oneOf(
            lambda: VP(V("receive")),
            lambda: VP(V("play"),
                       PP(P("at"), N("home"), P("against"))),
            lambda: VP(V("be"),
                       PP(P("at"), N("home"), P("against")))
        )
        return  oneOf(
            lambda: S(PP(P("for"),
                         NP(D("my").ow("p"),
                            D("next"),
                            N("game"))).a(","),
                      self.team_np(team_1),
                      vp.add(self.team_np(team_2, True)).add(next_date)),
            lambda: S(self.team_np(team_1).a("' "),
                      D("next"), N("game"),
                      VP(V("be"),
                         PP(P("at"), N("home")),
                         PP(P("against"), self.team_np(team_2, True)),
                         next_date))
        )

    def next_game_visitor(self, team_1, team_2, next_date) -> S:
        vp =  oneOf(
            lambda: VP(V("visit")),
            lambda: VP(V("be"),
                       PP(P("on"), NP(D("the"), N("road")), P("against"))),
            lambda: VP(V("host"))
        )
        return  oneOf(
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
                               next_date))))
        )
