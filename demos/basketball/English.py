from pyrealb import *
from Realizer import Realizer
from LexicalChoices import LexicalChoices
import json

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
        updateLexicon(json.load(open("data/nba-cities-names.json")))

    def set_language(self):
        loadEn()

    # frequent recurring expressions
    def conjunction(self,*elems) -> CP:
        return CP(C("and"),*elems)

    def with_p(self) -> P:
        return P("with")

    def on_day(self, date) -> DT:
        return DT(date).dOpt({"nat": True, "hour": False, "minute": False, "second": False,
                              "month": False, "date": False, "year": False,
                              "det": true})

    def pts_3(self, n) -> NP:
        return self.nb(n, "three-pointer")

    def nb_assists(self, n) -> NP:
        return self.nb(n, "assist")

    def m_for_n(self, m, n) -> [Terminal]:
        return [NO(m).lier(), P(oneOf("for","of")).lier(), NO(n)]

    def team_np(self, team, with_place=False, wins_losses=False) -> NP:
        return NP(D("the"),
                  N(team.place()) if with_place else None,
                  N(team.name()),
                  self.pts(team.wins(), team.losses()).ba("(") if wins_losses else None
                  ).n("p")

    def pts_abbrev(self,name)->str:
        return name

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
        return PP(P("in"), N(city))

    def team_winning_streak_vp(self, streak_length) -> Phrase:
        np = NP(D("my").ow("p"),
                NO(streak_length).dOpt({"ord": True}),
                A("straight"),
                N(oneOf(["victory","win"])))
        return oneOf(
            lambda: VP(V("give").t("pr"),
                       Pro("them").n("p").c("dat"),
                       np),
            lambda: NP(Q("en"),N("route"),
                       PP(P("to"),
                          np)),
            lambda : VP(V("extend").t("pr"),
                        NP(D("my").ow("p"),
                           N("winning"),N("streak"),
                           PP(P("to"),
                              NP(NO(streak_length).nat(),
                                 N("game")))
                           )
                        )
        )

    def team_losing_streak_vp(self, team, streak_length) -> Phrase:
        np = NP(D("my").ow("p"),
                NO(streak_length).dOpt({"ord": True}),
                A("straight"),
                N(oneOf(["loss", "defeat"])))
        return S(P("for"),self.team_np(team),
                 Pro("it").c("nom"),
                 VP(V("be").t(self.tense),
                    np))

    def conference_leader(self, winner_np) -> NP:
        return NP(winner_np.a(","),
                  NP(N("leader"),
                     PP(P("in"),
                        NP(D("my").ow("p"),
                           N("conference")))).a(","))

    def defeat_vp(self,nb_points) -> VP:
        if nb_points>15:
            verb = V(oneOf("defeat","top","dominate"))
        else:
            verb = oneOf(
                lambda:V("overcome"),
                lambda:[V("knock"),P("off")],
                lambda:[V("take"),P("down")]
            )
        return VP(verb).t(self.tense)

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
        return oneOf(
            lambda: S(self.team_np(winner),
                      VP(V("lead").t(self.tense),
                         PP(P("in"),
                            NP(D("all"), NO(4).dOpt({"nat": True}), N("quarter"))))),
            lambda: S(Pro("this"),
                      VP(V("be").t(self.tense),
                         NP(D("a"),
                            V("dominate").t("pr"),
                            N("win"),
                            PP(P("for"),
                               self.team_np(winner)))).a(","),
                      SP(C("as"),
                         Pro("it").c("nom"),
                         VP(V("come").t(self.tense),
                            PP(P("in"),
                               NP(N("wire").lier(),
                                  P("to").lier(),
                                  N("wire"),
                                  N("fashion"))))))
        )

    def in_overtime(self, winner):
        return S(self.team_np(winner),
                 VP(V("need").t(self.tense),
                    NP(N("overtime"),
                       VP(V("win").t("b-to"), self.game_part("game")))))

    def show_team_fact(self, team_1, team_2, fact):
        (period, score, t1_val, t2_val, diff) = fact
        period_pp = PP(P(oneOf("during", "over", "in")), self.game_part(period))
        if diff < 0:
            team_2, team_1 = team_1, team_2
            t2_val, t1_val = t1_val, t2_val
        score_n = score[:-1] if score.endswith("%") else score
        if score_n in {"goals", "rebounds", "assists", "steals", "blocks", "turnovers", "fouls", "points"}:
            score_np= NP(N(score_n[:-1]).n("p")) # HACK remove s to get the lemma and set plur
        elif score_n == "goals3":
            score_np = NP(N("three-pointer").n("p"))
        elif score_n == "free_throws":
            score_np = NP(N("free throw").n("p"))
        else:
            print("strange score_n",score_n)
        if score.endswith("%"):
            return S(period_pp.a(","),
                     self.team_np(team_1),
                     VP(V(oneOf("obtain","get")),
                        NP(D("a"),A("good").f("co"),score_np,N("percentage").a(","),
                           oneOf(
                               lambda: PP(NO(t1_val).a("%"),P("to"),NO(t2_val).a("%")),
                               lambda: NP(D("a"),N(oneOf("difference","advantage")),
                                          PP(P("of"),NO(abs(diff)).a("%")))
                           ))
                        ))
        return S(self.team_np(team_1),
                 VP(V(oneOf("overcome","dominate")),
                    self.team_np(team_2),
                    PP(P("for"),score_np),
                    oneOf(
                        lambda: PP(NO(t1_val),P("to"),NO(t2_val)),
                        lambda: PP(P("by"),NO(abs(diff)))
                    ),
                    period_pp))

    #   show_team_perf
    def show_goals_vp(self, goals, line_scores) -> VP:
        return VP(V("show").t(self.tense),
                  CP(C("and"),
                     NP(NO(int(goals * 100 / line_scores.goals_attempted())), Q("percent"),
                        PP(P("from"), NP(D("the"), N("field")))),
                     NP(self.pts(line_scores.free_throws(), line_scores.free_throws_attempted()),
                        oneOf(lambda : N("free throw").n("p"),
                              lambda: NP(N("attempt").n("p"),
                                         PP(P("at"),NP(D("the"),
                                                       N("charity"),
                                                       N("stripe"))))))))

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
                          V("score").t("pr"))),
            lambda: VP(V("have"),
                       NP(D("a"), A("efficient"), N("performance")),
                       V("score").t("pr"))
        )

    def player_VP(self) -> VP:
        return  oneOf(
            lambda: VP(V("score")),
            lambda: VP(V("finish"), P("with")),
            lambda: VP(V("end"), P("up"), P("with")),
            lambda: VP(V("record")),
            lambda: VP(V("post")),
            lambda: VP(V("add")),
            lambda: VP(V("contribute")),
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
        vp = oneOf(
            lambda: VP(V("receive")),
            lambda: VP(V("host")),
            lambda: VP(V("take"),P("on")),
            lambda: VP(V("play"),N("host"),P("to")),
            lambda: VP(V("return"),PP(P("to"),N("action"))),
            lambda: VP(V("be"),
                       PP(P("at"), N("home"), P("against")))
        )
        return oneOf(
            lambda: S(PP(P("on"),N("deck"),
                         PP(P("for"),self.team_np(team_1))),
                      VP(V("be"),
                         NP(D("a"),N("home"),N("match")),
                         PP(P("versus"),N(team_2.place())))),
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
            lambda: VP(V("travel"),
                       V("play").t("b-to"))
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
                         PP(P("to"), N(team_2.place())),
                         VP(V("take").t("b-to"),
                            PP(P("on"),
                               self.team_np(team_2),
                               next_date))))
        )
