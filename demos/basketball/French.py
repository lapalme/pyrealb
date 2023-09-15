from typing import Dict

from pyrealb import *
from Realizer import Realizer
from LexicalChoices import LexicalChoices
import json

from pyrealb import NP


# Ne disposant pas de corpus français, nous traduisons littéralement en utilisant des termes
# tirés de : https://fr.wikipedia.org/wiki/Lexique_du_basket-ball

class French(Realizer, LexicalChoices):
    def __init__(self, tense="pc"):
        self.tense = tense
        self.name = "French jsRealB"
        # language specifics
        loadFr()
        addToLexicon({"score": {"N": {"g": "m", "tab": "n3"}}})
        updateLexicon(json.load(open("data/nba-cities-names.json")))

    def set_language(self):
        loadFr()

    # quelques expressions toutes faites qui reviennent souvent
    def conjunction(self, *elems) -> CP:
        return CP(C("et"), *elems)

    def with_p(self) -> P:
        return P("avec")

    def on_day(self, date) -> DT:
        return DT(date).dOpt({"nat": True, "hour": False, "minute": False, "second": False,
                              "month": False, "date": False, "year": False,
                              "det": false})

    def pts_3(self, n=None) -> NP:
        return NP(self.no(n) if n is not None else None,
                  N(oneOf("tir", "lancer")),
                  PP(P("à"), self.nb(3, "point")))

    def nb_assists(self, n) -> NP:
        return NP(self.no(n),
                  N("passe").g("f"),  # important de spécifier le genre
                  A("décisif"))

    def m_for_n(self, m, n) -> [Terminal]:
        return [NO(m).lier(), P("sur").lier(), NO(n)]

    def team_np(self, team, with_place=False, wins_losses=False) -> NP:
        return NP(D("le"),
                  N(team.name()),
                  self.pts(team.wins(), team.losses()).ba("(") if wins_losses else None,
                  PP(P("de"), N(team.place())) if with_place else None)

    def pts_abbrev(self, name):
        return {"FG": "L",  # lancer
                "FG3": "L3",  # lancer 3
                "FT": "LF",  # lancer franc
                "REB": "R",  # rebond
                "BLK": "C",  # contre
                "AST": "PD",  # passe décisive
                "STL": "I",  # interception
                "TOV": "PB",  # perte de ballon
                "PF": "F",  # faute
                "PTS": "PTS",  # points
                "MIN": "MIN",  # minutes
                }[name]

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
        return PP(P("à"), N(city))

    def team_winning_streak_vp(self, streak_length) -> Phrase:
        return VP(Pro("leur"),
                  V("permettre").t("pr"),
                  oneOf(lambda: PP(P("de"),
                                   VP(V(oneOf("enregistrer", "remporter")).t("b")),
                                   NP(D("leur"),
                                      NO(streak_length).dOpt({"ord": True}),
                                      N("victoire"),
                                      PP(P("de"), N("suite")))),
                        lambda: PP(P("de"),
                                   VP(V("allonger").t("b"),
                                      PP(P("à"), NO(streak_length)),
                                      NP(D("leur"),
                                         N("série"),
                                         PP(P("de"),
                                            N("victoire").n("p")))))
                        ))

    def team_losing_streak_vp(self, team, streak_length) -> Phrase:
        np = NP(D("leur"),
                NO(4).dOpt({"ord": true}),
                N("défaite"), PP(P("de"), N("suite")))
        return S(P("pour"),self.team_np(team),
                 SP(Pro("ce"),
                    VP(V("être"),
                       np)))

    def conference_leader(self, winner_np) -> NP:
        return NP(winner_np.a(","),
                  NP(N("meneur").n("p"),
                     PP(P("dans"),
                        NP(D("leur"),
                           N("conférence")))).a(","))

    def defeat_vp(self, nb_points) -> VP:
        if nb_points > 15:
            verb = oneOf("dominer", "surpasser")
        else:
            verb = oneOf("défaire", "battre")
        return VP(V(verb).t(self.tense))

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
                    PP(P("pendant"),
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


    def show_team_fact(self, team1, team2, fact):
        facts_fr: dict[str, NP] = {
            "goals": NP(N(oneOf("lancer", "tir"))),
            "goals3": NP(N(oneOf("tir", "lancer")),
                         PP(P("à"), NP(NO(3), N("point")))),
            "rebounds": NP(N("rebond")),
            "free_throws": NP(N("lancer").n("p"), A("franc")),
            "assists": NP(N("passe"), A("décisif")),
            "steals": NP(N("interception")),
            "blocks": NP(N("contre")),
            "turnovers": NP(N("perte"), PP(P("de"), N("ballon"))),
            "fouls": NP(N("faute")),
            "points": NP(N("point"))
        }
        (period, score, t1_val, t2_val, diff) = fact
        period_pp = PP(P(oneOf("durant", "pendant")), self.game_part(period))
        if diff < 0:
            team2, team1 = team1, team2
            t2_val,t1_val = t1_val, t2_val
        score_n = score[:-1] if score.endswith("%") else score
        if score_n in facts_fr:
            score_np = facts_fr[score_n].n("p")
        else:
            print("strange score_n",score_n)
        if score.endswith("%"):
            return S(period_pp.a(","),
                     self.team_np(team1),
                     VP(V(oneOf("obtenir","réussir")),
                        NP(D("le"),A("bon").f("co"),score_np,
                           PP(P("en"),N("pourcentage")).a(","),
                           oneOf(
                               lambda: PP(NO(t1_val).a("%"),
                                          oneOf(
                                              lambda:[P("en"),N("comparaison"),P("avec")],
                                              lambda:[P("par"),N("rapport"),P("à")]
                                          ),
                                          NO(t2_val).a("%")),
                               lambda: NP(D("un"),N(oneOf("différence","avantage")),
                                          PP(P("de"),NO(abs(diff)).a("%")))
                           ))
                        ))
        return S(self.team_np(team1),
                 VP(V(oneOf("vaincre","dominer")),
                    self.team_np(team2),
                    PP(P("pour"),score_np.add(D("le"),0)),
                    oneOf(
                        lambda: PP(NO(t1_val),P("à"),NO(t2_val)),
                        lambda: PP(P("par"),NO(abs(diff)))
                    ),
                    period_pp))


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
        np = NP(A("prochain").pos("pre"),
                N(oneOf("partie", "match", "affrontement")))
        return oneOf(
            lambda: S(PP(P("à"), V("venir").t("b"),
                         PP(P("pour"), self.team_np(team_1))).a(","),
                      NP(D("un"), N("match"), P("à"), N("domicile"),
                         PP(P("contre"), N(team_2.place())))),
            lambda: S(PP(P("pour"), np.add(D("leur"), 0)).a(","),
                      self.team_np(team_1),
                      vp.add(self.team_np(team_2, True)),
                      next_date),
            lambda: S(np.add(D("le"), 0)
                      .add(PP(P("de"),
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
                         PP(P("à"), N(team_2.place())),
                         PP(P("pour"),
                            V("affronter").t("b"),
                            self.team_np(team_2),
                            next_date)))
        )
