from pyrealb import *
from random import sample, randint
from stats import is_high
from Realizer import Realizer


# Ne disposant pas de corpus français, nous traduisons littéralement en utilisant des termes
# tirés de : https://fr.wikipedia.org/wiki/Lexique_du_basket-ball

class French(Realizer):
    def __init__(self, tense="pc"):
        self.tense = tense
        self.name = "French jsRealB"
        # language specifics
        loadFr()

    best_player_VPs = [
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

    ]

    player_VPs = [
        lambda: VP(V("marquer")),
        lambda: VP(V("finir"), P("avec")),
        lambda: VP(V("terminer"), P("avec")),
        lambda: VP(V("enregistrer")),
        lambda: VP(V("ajouter")),
        lambda: VP(V("contribuer"), AP(D("un"), A("efficace"))),
        lambda: VP(V("avoir")),
    ]

    # quelques expressions toutes faites qui reviennent
    def pts_3(self, n):
        return NP(self.no(3),
                  N("panier"),
                  PP(P("à"), self.nb(3, "point")))

    def nb_assists(self, n):
        return NP(self.no(n),
                  N("passe").g("f"),  # important de spécifier le genre
                  A("décisif"))

    def m_for_n(self, m, n):
        return [NO(m).lier(), P("sur").lier(), NO(n)]

    def team_np(self, team, with_place=False):
        return NP(D("le"),
                  Q(team.name()),
                  PP(P("de"), Q(team.place())) if with_place else None).n("p")

    def game_part(self, part) -> Constituent:
        if part == "game":
            return NP(D("le"), N("partie"))
        if part.startswith("Q"):
            return NP(D("le"), NO(int(part[1])).dOpt({"ord": True}), N("quart"))
        if part.startswith("H"):
            return NP(D("le"), NO(int(part[1])).dOpt({"ord": True}), N("demie"))
        return Q("part:" + str(part))

    def show_points_details(self, player) -> Phrase:
        cp = CP(self.pts(player.goals(), player.goals_attempted(), "L"),  # Lancer
                self.pts(player.goals3(), player.goals3_attempted(), "L3"),  # Lancer de 3 points
                self.pts(player.free_throws(), player.free_throws_attempted(), "LF")  # Lancer franc
                ).ba("(")
        assists = player.assists()
        if is_high("players", player.name(), "AST", assists):
            nb_as = self.nb_assists(assists)
            if randint(0, 1) == 1:
                return S(cp,
                         SP(Adv("tout"), P("en"),
                            VP(V("ajouter").t("pr"), nb_as)))
            else:
                return S(CP(C("et"), cp, nb_as))
        return S(cp)

    def show_winner(self, winner, loser, g_date, g_stadium, g_city) -> str:
        verb = oneOf("défaire", "dominer", "battre", "surpasser")
        winner_scores = winner.line_scores()
        np = self.team_np(winner)
        if winner.conference_standing() == 1:
            np.a(",")
            np = NP(np,
                    NP(N("meneur").n("p"),
                       PP(P("dans"),
                          NP(D("leur"),
                             N("conférence")))).a(","))
        vp = VP(V(verb).t(self.tense))
        vp.add(self.team_np(loser))
        if "OT" in winner_scores and winner_scores["OT"].points() > 0:
            vp.add(PP(P("en"), N("période"), A("supplémentaire")))
        score = self.pts(winner_scores['game'].points(), loser.line_scores()['game'].points())
        pp_date = self.on_day(g_date).dOpt({"det": False})
        pp_place = PP(P("à"), D("le"), N("stade"), Q(g_stadium))
        pp_city = PP(P("à"), Q(g_city))
        return S(np, vp, score, sample([pp_date, pp_city, pp_place], k=3)).realize()

    # abréviations tirées de : https://stadeproligne.sportsdirectinc.com/basketball/nba-matchups-glossary.aspx
    def show_turning_points(self, winner, loser, overtime, loser_lead_in_first_half, loser_lead_in_second_half,
                            always_lead) -> str:
        out = []
        if loser_lead_in_first_half:
            out.append(CP(C("mais"),
                          SP(self.team_np(loser),
                             VP(V("mener"),
                                PP(P("dans"), self.game_part("H1")))),
                          SP(self.team_np(winner),
                             VP(V("parvenir"),
                                P("à"), V("revenir")))))
        elif loser_lead_in_second_half:
            cp = CP(C("mais"),
                    SP(self.team_np(loser),
                       VP(V("dominer"),
                          self.team_np(winner),
                          self.pts(loser.get_points()['H2'], winner.get_points()['H2']).ba("("),
                          PP(P("dans"), self.game_part("H2")))))
            cp.add(oneOf(
                lambda: VP(V("compléter"),
                           NP(D("leur"), N("retour"))).typ({"neg": True, "mod": "poss"}),
                lambda: SP(NP(D("le"), N("gagnant")),
                           VP(V("tenir").t(self.tense), Adv("bon"),
                              PP(P("pour"),
                                 NP(D("le"), N("victoire")))))
            ))
            out.append(cp)
        elif always_lead:
            out.append(S(self.team_np(winner),
                         VP(V("mener"),
                            PP(P("dans"),
                               NP(D("le"),
                                  NO(4).dOpt({"nat": True}),
                                  N("quart"))))))
        if overtime:
            out.append(S(self.team_np(winner),
                         VP(V("devoir"),
                            V("jouer"),
                            NP(D("le"), N("prolongation"),
                               PP(P("pour"),
                                  V("gagner").t("b"), self.game_part("game"))))))
        return "".join(s.t(self.tense).realize() for s in out)

    def show_team_perf(self, team) -> str:
        name = team.name()
        line_scores = team.line_scores("game")
        goals = line_scores.goals()
        free_throws = line_scores.free_throws()
        np = self.team_np(team)
        vp = VP(V("compter").t(self.tense),
                CP(C("et"),
                   NP(NO(int(goals * 100 / line_scores.goals_attempted())), Q("pour cent"),
                      PP(P("de"), NP(N("tir").n("p"), A("réussi")))),
                   NP(self.m_for_n(free_throws, line_scores.free_throws_attempted()),
                      NP(N("lancer").n("p"), A("franc")))))
        turnovers = line_scores.turnovers()
        if is_high("teams", name, "TOV", turnovers):
            vp.add(VP(C("et"),
                      V("subir").n("p").t(self.tense),
                      self.nb(turnovers, NP(N("perte"), P("de"), N("ballon")))))
        return S(np, vp).realize()

    def show_player_perf(self, player, vp, starter) -> str:
        # player [starter] vp [points] [details]
        # show global information
        name = player.name()
        vp_st = None
        if starter:
            vp_st = SP(Pro("qui"),
                       oneOf(
                           lambda: VP(V("débuter"), NP(D("le"), N("partie"))),
                           lambda: VP(V("être"), NP(D("un"), N("partant"))),
                           lambda: VP(V("figurer"), PP(P("dans"),
                                                       NP(D("le"),
                                                          N("alignement"),
                                                          PP(P("de"), N("départ")))))
                       ).t("i"))
        vp = vp().t(self.tense)
        vp.add(self.nb(player.points(), "point"))
        s = S(Q(name), vp_st, vp)
        minutes = player.minutes()
        if is_high("players",name, "MIN",minutes):
            s.add(PP(P("en"), self.nb(minutes, "minute")))
        # show details
        details = []
        if randint(0, 1) == 0:
            goals = player.goals()
            if is_high("players", name, "FGM", goals):
                details.append(oneOf(NP(self.m_for_n(goals, player.goals_attempted()),Q("L")),
                                     self.nb(goals, "point")))
            goals3 = player.goals3()
            if is_high("players", name, "FG3M", goals3):
                details.append(oneOf(self.pts_3(goals3),
                                     NP(self.m_for_n(goals3, player.goals3_attempted()),
                                        PP(P("depuis"),
                                           NP(D("le"), N("ligne"),
                                              PP(P("de"),
                                                 self.nb(3, "point")))))))
            rebounds = player.rebounds()
            if is_high("players", name, "TREB", rebounds):
                reb = self.nb(rebounds, "rebond")
                details.append(oneOf(lambda: reb,
                                     lambda: VP(reb,V("récupérer").t("pp"))))
            assists = player.assists()
            if is_high("players", name, "AST", assists):
                details.append(self.nb_assists(assists))
            if len(details) > 0:
                details[0].add(P("avec"), 0)
        else:
            details.append(self.show_points_details(player))
        double = player.double()
        if double != "none":
            details.append(NP(V("terminer").t(self.tense),
                              PP(P("avec"),
                                 NP(D("un"), Q(double).lier(), N("double")))))
        return s.add(CP(C("et"), details)).realize()

    def show_next_game(self, date, team_1, is_home, team_2) -> str:
        next_date = self.on_day(date)
        if is_home:
            vp = oneOf(
                lambda: VP(V("accueillir")),
                lambda: VP(V("jouer"),
                           PP(P("à"), NP(D("le"), N("maison")), P("contre"))),
                lambda: VP(V("être"),
                           PP(P("à"), N("domicile"), P("contre")))
            )
            out = oneOf(
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
        else:
            vp = oneOf(
                lambda: VP(V("visiter")),
                lambda: VP(V("être"),
                           PP(P("sur"), NP(D("le"), N("route")), P("contre"))),
                lambda: VP(V("accueillir"))
            )
            out = oneOf(
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
        return out.t("f").realize()
