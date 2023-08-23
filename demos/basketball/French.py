from pyrealb import *
from Realizer import Realizer
from LexicalChoices import LexicalChoices


# Ne disposant pas de corpus français, nous traduisons littéralement en utilisant des termes
# tirés de : https://fr.wikipedia.org/wiki/Lexique_du_basket-ball

class French(Realizer, LexicalChoices):
    def __init__(self, tense="pc"):
        self.tense = tense
        self.name = "French jsRealB"
        # language specifics
        loadFr()
        addToLexicon({"score": {"N": {"g": "m", "tab": "n3"}}})
        addToLexicon({"Houston": {"N": {"g": "m", "tab": "nI", "h": 1}}})
        addToLexicon({"Utah": {"N": {"g": "m", "tab": "nI", "h": 1}}})

    def set_language(self):
        loadFr()

    def t(self):
        return self.tense

    # quelques expressions toutes faites qui reviennent souvent
    def conjunction(self, *elems) -> CP:
        return CP(C("et"), *elems)

    def with_p(self) -> P:
        return P("avec")

    def pts_3(self, n) -> NP:
        return NP(self.no(n),
                  N("panier"),
                  PP(P("à"), self.nb(3, "point")))

    def nb_assists(self, n) -> NP:
        return NP(self.no(n),
                  N("passe").g("f"),  # important de spécifier le genre
                  A("décisif"))

    def m_for_n(self, m, n) -> [Terminal]:
        return [NO(m).lier(), P("sur").lier(), NO(n)]

    def team_np(self, team, with_place=False, wins_losses=False) -> NP:
        return NP(D("le"),
                  Q(team.name()),
                  self.pts(team.wins(), team.losses()).ba("(") if wins_losses else None,
                  PP(P("de"), Q(team.place())) if with_place else None).n("p")

    def game_part(self, part) -> Constituent:
        if part == "game":
            return NP(D("le"), N("partie"))
        if part.startswith("Q"):
            return NP(D("le"), NO(int(part[1])).dOpt({"ord": True}), N("quart"))
        if part.startswith("H"):
            return NP(D("le"), NO(int(part[1])).dOpt({"ord": True}), N("demie"))
        return Q("part:" + str(part))

    #  show_points_details
    def points_details(self, player) -> CP:
        scores = player.scores
        return CP(self.pts(scores.goals(), scores.goals_attempted(), "L"),  # Lancer
                  self.pts(scores.goals3(), scores.goals3_attempted(), "L3"),  # Lancer de 3 points
                  self.pts(scores.free_throws(), scores.free_throws_attempted(), "LF")  # Lancer franc
                  ).ba("(")

    def with_assists(self, details, assists):
        nb_as = self.nb_assists(assists)
        return oneOf(
            lambda: S(details,
                      SP(Adv("tout"), P("en"),
                         VP(V("ajouter").t("pr"), nb_as))),
            lambda: S(CP(C("et"), details, nb_as))
        )

    # show_winner
    def stadium_pp(self, stadium) -> PP:
        return PP(P("à"), D("le"), N("stade"), Q(stadium))

    def city_pp(self, city) -> PP:
        return PP(P("à"), Q(city))

    def team_winning_streak_vp(self, streak_length):
        return VP(V("permettre").t("pr"),
                  Pro("leur"),
                  PP(P("de"),
                     VP(V("enregistrer").t("b")),
                     NP(D("leur"),
                        NO(streak_length).dOpt({"ord": True}),
                        N("série"),
                        PP(P("de"), N("victoire").n("p")))))

    def conference_leader(self, winner_np) -> NP:
        return NP(winner_np.a(","),
                  NP(N("meneur").n("p"),
                     PP(P("dans"),
                        NP(D("leur"),
                           N("conférence")))).a(","))

    def defeat_vp(self) -> VP:
        verb = oneOf("défaire", "dominer", "battre", "surpasser")
        vp = VP(V(verb).t(self.tense).n("p"))
        return vp

    def overtime_pp(self, minutes):
        return PP(P("en"),
                  NO(3).dOpt({"ord": True}) if minutes > 50
                  else NO(2).dOpt({"ord": True}) if minutes > 25 else None,
                  N("période"),
                  A("supplémentaire"))

    #  show_turning_points
    # abréviations tirées de : https://stadeproligne.sportsdirectinc.com/basketball/nba-matchups-glossary.aspx
    def loser_lead_in_first_half(self, winner, loser) -> CP:
        return CP(C("mais"),
                  SP(self.team_np(loser),
                     VP(V("mener"),
                        PP(P("dans"), self.game_part("H1")))),
                  SP(self.team_np(winner),
                     VP(V("parvenir"),
                        P("à"), V("revenir").t("b"))))

    def loser_lead_in_second_half(self, winner, loser) -> CP:
        cp = CP(C("mais"),
                S(self.team_np(loser),
                  VP(V("dominer"),
                     self.team_np(winner),
                     self.pts(loser.get_points('H2'), winner.get_points('H2')).ba("("),
                     PP(P("dans"), self.game_part("H2")))))
        cp.add(oneOf(
            lambda: VP(V("compléter"),
                       NP(D("leur"), N("retour"))).typ({"neg": True, "mod": "poss"}),
            lambda: SP(NP(D("le"), N("gagnant")),
                       VP(V("tenir").t(self.tense), Adv("bon"),
                          PP(P("pour"),
                             NP(D("le"), N("victoire")))))
        ))
        return cp

    def always_lead(self, winner) -> S:
        return S(self.team_np(winner),
                 VP(V("mener"),
                    PP(P("dans"),
                       NP(D("le"),
                          NO(4).dOpt({"nat": True}),
                          N("quart")))))

    def in_overtime(self, winner):
        return S(self.team_np(winner),
                 VP(V("devoir"),
                    V("jouer").t("b"),
                    NP(D("le"), N("prolongation"),
                       PP(P("pour"),
                          V("gagner").t("b"), self.game_part("game")))))

    #   show_team_perf
    def show_goals_vp(self, goals, line_scores) -> VP:
        return VP(V("compter").t(self.tense),
                  CP(C("et"),
                     NP(NO(int(goals * 100 / line_scores.goals_attempted())), Q("pour cent"),
                        PP(P("de"), NP(N("tir").n("p"), A("réussi")))),
                     NP(NO(line_scores.free_throws()), N("lancer").n("p"), A("franc"),
                        PP(P("sur"), NO(line_scores.free_throws_attempted())))))

    def show_turnovers_vp(self, turnovers):
        return VP(C("et"),
                  V("subir").n("p").t(self.tense),
                  self.nb(turnovers, NP(N("perte"), P("de"), N("ballon"))))

    #  show_player_perf
    def best_player_VP(self):
        return oneOf(
            lambda: VP(V("obtenir"), NP(A("bon").f("su"), N("pointage"),
                                        PP(P("de"),
                                           NP(D("le"), N("match"),
                                              P("avec"))))),
            lambda: VP(V("finir"), P("avec")),
            lambda: VP(V("mener").a(","), V("compter").t("pr")),
            lambda: VP(V("mener"),
                       NP(D("mon"), N("équipe")),
                       V("marquer").t("pr")),
            lambda: VP(V("réaliser"), NP(D("un"), A("excellent"), N("performance")), V("compter").t("pr"))
        )

    def player_VP(self):
        return oneOf(
            lambda: VP(V("marquer")),
            lambda: VP(V("finir"), P("avec")),
            lambda: VP(V("terminer"), P("avec")),
            lambda: VP(V("enregistrer")),
            lambda: VP(V("ajouter")),
            lambda: VP(V("contribuer"), AP(D("un"), A("efficace"))),
            lambda: VP(V("avoir"))
        )

    def starter_player(self) -> SP:
        return SP(Pro("qui"),
                  oneOf(
                      lambda: VP(V("débuter"), NP(D("le"), N("partie"))),
                      lambda: VP(V("être"), NP(D("un"), N("partant"))),
                      lambda: VP(V("figurer"), PP(P("dans"),
                                                  NP(D("le"),
                                                     N("alignement"),
                                                     PP(P("de"), N("départ")))))
                  ).t("i"))

    def season_high(self) -> NP:
        np = oneOf(
            NP(D("un"), N("record")),
            NP(D("mon"), A("bon").f("co"), N("score"))
        )
        return np.add(
            oneOf(
                PP(P("pour"), NP(D("le"), N("saison"))),
                PP(P("jusque"), Adv("ici"))
            )
        )

    def nb_minutes_played(self, minutes) -> PP:
        return PP(P("en"), self.nb(minutes, "minute"))

    def goals_made(self, player, goals) -> NP:
        return self.nb(goals, [N("tir"), A("réussi")])

    def three_pointers(self, player, goals3) -> NP:
        return oneOf(lambda: self.pts_3(goals3),
                     lambda: NP(self.m_for_n(goals3,
                                             player.scores.goals3_attempted()),
                                PP(P("depuis"),
                                   NP(D("le"), N("ligne"),
                                      PP(P("de"),
                                         self.nb(3, "point"))))))

    def rebounds(self, rebounds) -> Phrase:
        reb = self.nb(rebounds, "rebond")
        return oneOf(lambda: reb,
                     lambda: VP(reb, V("récupérer").t("pp").n("p")))

    def doubles(self, double) -> VP:
        return VP(V("terminer").t(self.tense),
                  PP(P("avec"),
                     NP(D("un"), Q(double).lier(), N("double"))))

    # show_next_game
    def next_game_home(self, team_1, team_2, next_date) -> S:
        vp = oneOf(
            lambda: VP(V("accueillir")),
            lambda: VP(V("jouer"),
                       PP(P("à"), NP(D("le"), N("maison")), P("contre"))),
            lambda: VP(V("être"),
                       PP(P("à"), N("domicile"), P("contre")))
        )
        return oneOf(
            lambda: S(PP(P("pour"),
                         NP(D("leur"),
                            A("prochain").pos("pre"),
                            N("partie"))).a(","),
                      self.team_np(team_1),
                      vp.add(self.team_np(team_2, True)),
                      next_date),
            lambda: S(NP(D("le"),
                         A("prochain").pos("pre"),
                         N("match"),
                         PP(P("de"),
                            self.team_np(team_1))),
                      VP(V("être"),
                         PP(P("à"), N("domicile")),
                         PP(P("contre"), self.team_np(team_2, True)),
                         next_date))
        )

    def next_game_visitor(self, team_1, team_2, next_date) -> S:
        vp = oneOf(
            lambda: VP(V("visiter")),
            lambda: VP(V("être"),
                       PP(P("sur"), NP(D("le"), N("route")), P("contre"))),
            lambda: VP(V("accueillir"))
        )
        return oneOf(
            lambda: S(AP(next_date.dOpt({"det": False}),
                         A("prochain")).a(","),
                      self.team_np(team_1),
                      vp,
                      self.team_np(team_2, True)),
            lambda: S(Adv("ensuite"),
                      self.team_np(team_1),
                      VP(V("voyager"),
                         PP(P("à"), Q(team_2.place())),
                         PP(P("pour"),
                            V("affronter").t("b"),
                            self.team_np(team_2),
                            next_date)))
        )
