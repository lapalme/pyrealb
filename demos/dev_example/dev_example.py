from pyrealb import *
import datetime, sys

exemplesFr = []
exemplesEn = []
dependancesFr = []
dependenciesEn = []
constituentEnFr = []


def makeExamples():
    global exemplesFr, exemplesEn, dependancesFr, dependancesFr, constituentEnFr
    loadFr()
    addToLexicon({"John": {"N": {"g": "m", "tab": "n4"}}})
    addToLexicon({"Mary": {"N": {"g": "f", "tab": "n16"}}})
    pomme = NP(D("le"), N("pomme"));
    gars = NP(D("le"), N("garçon").n("p"));

    exemplesFr = [
        [N("chat"),
         "chat"],
        [Pro("moi").c("acc"),
         "me"],
        [Pro("moi").tn(""),
         "moi"],
        [NP(D("le"), N("chat")),
         "le chat"],
        [S(NP(D('le'), N('chat').n("p"))),
         "Les chats. "],
        [V("aller").t("ps").pe(2).n("p"),
         "allâtes"],
        [V("aller").t("pc").pe(3).n("s"),
         "est allé"],
        [VP(V("aller").t("f").pe(1).n("p")).typ({"neg": True}),
         "n'irons pas"],
        [VP(V("aller").t("pq").pe(2).n("s")).typ({"neg": True}),
         "n'étais pas allé"],
        [S(NP(D("le"), N("chat").g("f").n("p")),
           VP(V("manger"),
              NP(D("le"), N("souris")))),
         "Les chattes mangent la souris. "],
        [S(NP(D("le"), N("chat").g("f").n("p")),
           VP(V("manger"),
              NP(D("le"), N("souris")))).typ({"pas": True}),
         "La souris est mangée par les chattes. "],
        [S(NP(D('le'), A("blanc"),
              N('chat').g("f").n("p").tag("b").tag("i")),
           VP(V('dévorer').t('pc'),
              NP(D('le'),
                 N('souris'),
                 A("gris"), "Wow!").tag("a", {"href": "http:#wikipedia.org/cat", "target": "_blank"}))
           ).typ({"neg": True}),
         'Les <i><b>chattes</b></i> blanches n\'ont pas dévoré <a href="http:#wikipedia.org/cat" target="_blank">la souris grise Wow!</a>'],
        [S(NP(D('le'),
              N('souris').n("p")),
           VP(V('être'),
              AP(A('gris')))).typ({"neg": True}),
         "Les souris ne sont pas grises. "],
        [S(Pro("je").n("p").pe(2),
           VP(V("avoir").t("cp"),
              NP(NO(2), A("beau"), N("ami").g("f")))).typ({"neg": "plus"}),
         "Vous n'auriez plus eu 2 belles amies. "],
        [S(NP(N("John")),
           VP(V("évanouir").aux("êt").t("pc")),
           PP(P("à"), DT("1979-05-21T10:05:00"))).typ({"neg": True}),
         "John ne s'est pas évanoui au lundi 21 mai 1979 à 10 h 5 min 0 s. "],
        [S(CP(C("et"), NP(N("John")), NP(N("Mary"))),
           VP(V("évanouir").t("pc")),
           PP(P("à"), DT("1979-05-21T10:05:00"))).typ({"neg": True}),
         "John et Mary ne se sont pas évanouis au lundi 21 mai 1979 à 10 h 5 min 0 s. "],
        [S(VP().add(V("aimer")).add(pomme)).add(gars, 0),
         "Les garçons aiment la pomme. "],
        [S(CP(C("et"), NP(D("le"), N("fruit"))).add(pomme).add(gars),
           VP(V("venir").t("pc"),
              Adv("hier"))),
         "Le fruit, la pomme et les garçons sont venus hier. "],
        [S(CP(C("et"), NP(D("le"), N("orange"))).add(pomme),
           VP(V("arriver").t("pc"),
              Adv("hier"))),
         "L'orange et la pomme sont arrivées hier. "],
        [S(Pro("je"),
           VP(V("manger").t("pc"),
              NP(D("le"), N("pomme")))),
         "Il a mangé la pomme. "],
        [S(Pro("je"),
           VP(V("manger").t("pc"),
              NP(D("le"), N("pomme")).tag("i").pro())),
         "Il <i>l'</i> a mangée. "],
        [S(NP(D("le"), N("pomme").tag("i"),
              SP(Pro("qui"),
                 VP(V("manger").aux("êt").t("pc"))))),
         "La <i>pomme</i> qui est mangée. "],
        [NP(D("le"), N("pomme").tag("i"),
            SP(Pro("que"),
               Pro("je"),
               VP(V("manger").t("pc")))),
         "la <i>pomme</i> qu'il a mangée"],
        [S(NP(D("le"), N("pomme").tag("i"),
              SP(Pro("que"),
                 Pro("je"),
                 VP(V("manger").t("pc")))).pro()),
         "Elle. ",
         "Conversion d'un '.pro' au premier niveau, n'est pas traitée"],
        [S(NP(D("le"), N("enfant").n("p")), VP(V("manger"), NP(D("le"), N("gâteau")))).typ({"pas": True}),
         "Le gâteau est mangé par les enfants. "],
        [S(Pro("je").pe(1).n("p"), VP(V("agir").t("pc"), AdvP(Adv("conformément"),
                                                              PP(P("à"), NP(D("le"), N("loi")))))).typ({"neg": True}),
         "Nous n'avons pas agi conformément à la loi. "],
        [S(NP(D('le'),
              N('souris'),
              SP(Pro('que'),
                 NP(D('le'),
                    N('chat').n("p")),
                 VP(V('manger').t('pc')))),
           VP(V('être'),
              AP(A('gris')))),
         "La souris que les chats ont mangée est grise. "],
        [DT(),
         None],
        [DT().nat(false),
                        None],
    [DT().dOpt({"rtime": True}),
                    None],
    [NO(1.847584).dOpt({"mprecision": 0}),
     "2"],
    [NO(1.847584).dOpt({"mprecision": 4}),
     "1,8476"],
    [NO(1.847584).dOpt({"raw": false}),
     "1,85"],
    [NO(1.847584).dOpt({"raw": True}),
     "1.847584"],
    [NO(125).dOpt({"nat": True}),
     "cent vingt-cinq"],
    [NO(10).dOpt({"ord": True}),
     "dixième"],
    [NP(NO(0), N("avion")),
     "0 avion"],
    [NP(NO(2), N("avion")),
     "2 avions"],
    [NP(NO(1.5), N("livre")),
     "1,5 livre"],
    [NP(NO(2.4), N("livre")),
     "2,4 livres"],
    [NP(NO(2), A("rouge"), N("avion")),
     "2 avions rouges"],
    # [N("pomme").g("w"),
    #     "pomme"],
    # [S(Pro("lui").c("nom"),
    #    VP(V("donner").t("pc"),
    #       NP(D("un"), N("pomme")).pro(),
    #       PP(P("à"), NP(D("le"), A("jeune"), N("femme"))
    #          ))),
    #  "Il l'a donnée à la jeune femme. "],
    # [S(Pro("lui").c("nom"),
    #    VP(V("donner").t("pc"),
    #       NP(D("un"), N("pomme")).pro(),
    #       PP(P("à"), NP(D("le"), A("jeune"), N("femme"))).pro())),
    #  "Il la lui a donnée. "],
    # [S(Pro("je").pe(1),
    #    VP(V("mettre").t("pc"),
    #       NP(D("le"), N("lettre")),
    #       PP(P("sur"), NP(D("le"), N("table"))).pro())),
    #  "J'y ai mis la lettre. "],
    # [S(Pro("je").pe(1),
    #    VP(V("mettre").t("pc"),
    #       NP(D("le"), N("lettre")).pro(),
    #       PP(P("sur"), NP(D("le"), N("table"))).pro())).typ({"neg": True}),
    #  "Je ne l'y ai pas mise. "],
    # # exemples du papier "Architecture..."
    # # Figure 6
    # [S(Pro("lui").c("nom"),
    #    VP(V("donner").t("pc"),
    #       NP(D("un"), N("pomme")).pro())),
    #  "Il l'a donnée. "],
    # # Table 1 - 1
    # [S(Pro("lui").c("nom"),
    #    VP(V("donner").t("pc"),
    #       NP(D("un"), N("pomme")).pro())).typ({"neg": True}),
    #  "Il ne l'a pas donnée. "],
    # # Table 1 - 2
    # [S(Pro("lui").c("nom"),
    #    VP(V("donner").t("pc"),
    #       NP(D("un"), N("pomme")).pro(),
    #       PP(P("à"), NP(D("le"), N("fille"))))).typ({"neg": True}),
    #  "Il ne l'a pas donnée à la fille. "],
    # # Table 1 - 3
    # [S(Pro("lui").c("nom"),
    #    VP(V("donner").t("pc"),
    #       NP(D("un"), N("pomme")).pro(),
    #       PP(P("à"), NP(D("le"), N("fille"))).pro())).typ({"neg": True}),
    #  "Il ne la lui a pas donnée. "],
    # # Table 1 - 4
    # [S(Pro("lui").c("nom"),
    #    VP(V("donner").t("pc"),
    #       NP(D("un"), N("pomme")).pro(),
    #       PP(P("à"), NP(D("le"), N("fille"))).pro())).typ({"neg": True, "pas": True}),
    #  "Elle ne lui a pas été donnée par lui. "],
    # # position des pronoms devant le verbe
    # [S(Pro('lui').c("nom"),
    #    VP(V('donner').t("pc"),
    #       NP(D('un'), N('chat')).pro(),
    #       Pro("elle").c("dat"))),
    #  "Il le lui a donné. "],
    # # modifications globales de propriétés
    # [S(NP(D("le"), N("chat").g("f")),
    #    VP(V("manger"),
    #       NP(D("le"), N("souris")))).t("f"),
    #  "La chatte mangera la souris. "],
    # [S(CP(C("et"),
    #       Pro("elle").tn(""),
    #       Pro("moi").tn("")),
    #    VP(V("aller"),
    #       PP(P("à"),
    #          NP(D("le"), N("plage"))))).t("pc"),
    #  "Elle et moi sommes allés à la plage. "],
    # # changement de personne dans le déterminant
    # [S(NP(D("notre").pe(2), N("chef")),
    #    VP(V("aller"))),
    #  "Votre chef va. "],
    # # nouveau type de question "yon" par inversion du sujet
    # [S(NP(D('le'),  # 54
    #       N('chat')),
    #    VP(V('manger'),
    #       NP(D('le'),
    #          N('souris')))).typ({int: "yon"}),
    #  "Le chat mange-t-il la souris? "],
    # [S(NP(D('le'),  # 55
    #       N('chat')),
    #    VP(V('manger'),
    #       NP(D('le'),
    #          N('souris')))).typ({int: "yon", "neg": True}),
    #  "Le chat ne mange-t-il pas la souris? "],
    # [S(NP(D('le'),  # 56
    #       N('chat')),
    #    VP(V('manger'),
    #       NP(D('le'),
    #          N('souris')))).typ({int: "yon", "pas": True}),
    #  "La souris est-elle mangée par le chat? "],
    # [S(Pro("je"),  # 57
    #    VP(V('manger'),
    #       NP(D('le'),
    #          N('fromage')))).typ({int: "yon"}),
    #  "Mange-t-il le fromage? "],
    # [S(Pro("je"),  # 58
    #    VP(V('manger').t("pc"),
    #       NP(D('le'),
    #          N('fromage')))).typ({int: "yon"}),
    #  "A-t-il mangé le fromage? "],
    # # question tag
    # [S(Pro("je"),  # 59
    #    VP(V('manger').t("pc"),
    #       NP(D('le'),
    #          N('fromage')))).typ({int: "tag"}),
    #  "Il a mangé le fromage, n'est-ce pas? "],
    # # adverb position
    # [S(Pro('je').pe(2),  # 60
    #    VP(V('travailler').t("pc"),
    #       Adv('bien'))).typ({"mod": "nece"}),
    #  "Tu as dû bien travailler. "],
    # [S(Pro('je'),  # 61
    #    VP(V('aller').t("pc"),
    #       Adv('hier'),
    #       PP(P('à'),
    #          NP(D('le'),
    #             N('maison'))))).typ({"neg": True}),
    #  "Il n'est pas allé hier à la maison. "],
    # [S(Pro('je'),  # 62
    #    VP(V('aller').t("pc"),
    #       Adv('souvent'),
    #       PP(P('à'),
    #          NP(D('le'),
    #             N('maison'))),
    #       Adv('sûrement'))).typ({"neg": True}),
    #  "Il n'est pas souvent allé à la maison sûrement. "],
    # [S(Pro('je'),  # 63
    #    VP(V('aller').t("pc"),
    #       Adv('souvent').pos("post"),
    #       PP(P('à'),
    #          NP(D('le'),
    #             N('maison'))))).typ({"neg": True}),
    #  "Il n'est pas allé souvent à la maison. "],
    # [S(NP(D('le'),  # 64
    #       N('chat')),
    #    VP(V('manger'),
    #       Adv('bien'),
    #       Adv('souvent'),
    #       NP(D('le'),
    #          N('souris')))).typ({"pas": True}),
    #  "La souris est bien souvent mangée par le chat. "],
    # [S(Pro("tout"),
    #    VP(V("sembler").t("pa"),
    #       V("fonctionner").t("bp"))),
    #  "Tout eut semblé avoir fonctionné. "],
    # [S(Pro("lui"),
    #    VP(V("manger"),
    #       NP(D("le"), N("fromage")))).typ({"pas": True}),
    #  "Le fromage est mangé par lui. "],
    # [NP(NO(2), N("fille"), CP(C("et"), A("joli"), A("vieux"))),
    #  "2 filles jolies et vieilles"],
    # [NP(CP(C("ou"), NO(2), NO(3)), N("fille"), CP(C("et"), A("jeune"), A("joli"))),
    #  "2 ou 3 filles jeunes et jolies"],

    ];

    #  exemples en anglais
    # loadEn();
    # apple = NP(D("a"), N("apple"));
    # appleC = apple.clone();
    # appleF = lambda: NP(D("a"), N("apple"))
    # addToLexicon({"John": {"N": {"g": "m", "tab": "n4"}}})
    # addToLexicon({"Mary": {"N": {"g": "f", "tab": "n4"}}})
    #
    # exemplesEn = [
    #     [V("love"), "loves"],  # 0
    #     [V("have").t("ps"), "had"],  # 1
    #     [V("be").pe(3), "is"],  # 2
    #     [VP(V("love")).typ({"neg": True}), "does not love"],  # 3
    #     [VP(V("love")).typ({"int": "yon"}), "does love? "],  # 4
    #     [VP(V("love")).typ({"prog": True}), "is loving"],  # 5
    #     [VP(V("love")).typ({"mod": "poss"}), "can love"],  # 6
    #     # examples from the "Architecture..." paper
    #     # Figure 1
    #     [S(Pro("him").c("nom"),  # 7
    #        VP(V("eat"),
    #           NP(D("a"), N("apple").n("p")).tag("em")
    #           )), "He eats <em>apples</em>. "],
    #     #  Figure 1 (with global modification)
    #     [S(Pro("him").c("nom"),  # 8
    #        VP(V("eat"),
    #           NP(D("a"), N("apple").n("p")).tag("em")
    #           )).t("ps"),
    #      "He ate <em>apples</em>. "],
    #     # Figure 4
    #     [S(Pro("him").c("nom"),  # 9
    #        VP(V("eat"),
    #           NP(D("a"), N("apple").n("p"))
    #           )).typ({"neg": True}), "He does not eat apples. "],
    #     # Figure 5
    #     [S(Pro("him").c("nom"),  # 10
    #        VP(V("eat"),
    #           NP(D("a"), N("apple").n("p"))
    #           )).typ({"neg": True, "pas": True}),
    #      "Apples are not eaten by him. "],
    #     # Section 6.1
    #     [S(Pro("him").c("nom"), VP(V("eat"),  # 11
    #                                NP(D("a"), N("apple").n("p")).add(A("red")))
    #        ).add(Adv("now").a(","), 0),
    #      "Now, he eats red apples. ",
    #      "Conversion does not handle 'add' correctly"],
    #     # Section 6.2
    #     [S(CP(C("and"), NP(D("the"), N("apple")),  # 12
    #           NP(D("the"), N("orange")),
    #           NP(D("the"), N("banana"))),
    #        VP(V("be"), A("good"))),
    #      "The apple, the orange and the banana are good. "],
    #     [S(CP(C("and"), NP(D("the"), N("apple"))),  # 13
    #        VP(V("be"), A("good"))),
    #      "The apple is good. "],
    #     # Section 6.3
    #     [S(Pro("him").c("nom"),  # 14
    #        CP(C("and"),
    #           VP(V("eat"), apple), VP(V("love"), appleC.pro()))),
    #      "He eats an apple and loves it. "],
    #     # this example is not exactly what is in the paper, but I have not managed to make it work properly
    #     [S(NP(D("a"), N("apple")).pro(), VP(V("be"), A("red"))),  # 15
    #      "It is red. "],
    #     [S(Pro("him").c("nom"),  # 16
    #        CP(C("and"),
    #           VP(V("eat"), appleF()),
    #           VP(V("love"), appleF().pro()))),
    #      "He eats an apple and loves it. "],
    #     [S(appleF(), VP(V("be"), A("red"))),  # 17
    #      "An apple is red. "],
    #     [S(Pro("him").c("nom"),  # 18
    #        CP(C("and"),
    #           VP(V("eat"), appleF()),
    #           VP(V("love"), appleF().clone().pro()))),
    #      "He eats an apple and loves it. "],
    #     [S(appleF(), VP(V("be"), A("red"))),  # 19
    #      "An apple is red. "],
    #     # Section 6.4
    #     [S(Pro("him").c("nom"),  # 20
    #        VP(V("eat"),
    #           NP(D("a"), N("apple").tag("a", {"href": "https:#en.wikipedia.org/wiki/Apple"})))),
    #      'He eats an <a href="https:#en.wikipedia.org/wiki/Apple">apple</a>. '],
    #     # Section 6.6
    #     [NP(NO(1).dOpt({"nat": True}), N("plane")),  # 21
    #      "one plane"],
    #     [NP(NO(3).dOpt({'nat': True}), N("plane")),  # 22
    #      "three planes"],
    #     [S(AP(D("the"),  # 23
    #           A("large").f("su"),
    #           PP(P("of"),
    #              NP(D("the"),
    #                 N("trainer").n("p"))).a(",")),
    #        NP(D("this").n("s"),  # check propagation of the number (this should not be these)
    #           N("addition").n("s"))),
    #      "The largest of the trainers, this addition. ",
    #      "Peculiar structure of constituents for which the dependents are not strickly equivalent "],
    #     # question tag
    #     [S(Pro("him").c("nom"),  # 24
    #        VP(V("eat"),
    #           NP(D("a"), N("apple").n("p")).tag("em")
    #           )).typ({int: "tag"}),
    #      "He eats <em>apples</em>, doesn't he? "],
    #     [S(Pro("him").c("nom"),  # 25
    #        VP(V("eat"),
    #           NP(D("a"), N("apple").n("p")).tag("em")
    #           )).typ({"neg": True, int: "tag"}),
    #      "He does not eat <em>apples</em>, does he? "],
    #     [S(Pro("him").c("nom"),  # 26
    #        VP(V("eat").t("f"),
    #           NP(D("a"), N("apple").n("p")).tag("em")
    #           )).typ({int: "tag"}),
    #      "He will eat <em>apples</em>, won't he? "],
    #     [S(Pro('him').c("nom"),  # 27
    #        VP(V('love'),
    #           Adv('really'),
    #           Pro('him').g("f").c("acc"))).typ({"perf": True, "mod": "poss"}),
    #      "He can really have loved him. "],
    #     [S(NP(D("the"), N("cat")).n("p"),
    #        VP(V("sit").t("ps"),
    #           PP(P("on"),
    #              NP(D("the"), N("mat"))))).typ({int: "tag", "neg": True}),
    #      "The cats did not sit on the mat, did they? "],
    #     [CP(C("or"),
    #         NP(D("a"), N("elevator")),
    #         NP(D("a"), N("eucalyptus"))),
    #      "an elevator or a eucalyptus"],
    #     [S(VP(V("go").t('ip'), Adv("away"))).typ({"int": "tag"}),
    #      "Go away, won't you? "],
    #     [S(Pro("them"),
    #        VP(V("eat"),
    #           NP(D("the"), N("cheese")))).typ({"pas": True}),
    #      "The cheese is eaten by them. "],
    # ]

    # # dépendances en français
    # loadFr()
    # addToLexicon("Mauritanie", {"N": {"g": "f", "tab": ["n16"]}})
    # addToLexicon("Algérie", {"N": {"g": "f", "tab": ["n16"]}})
    # addToLexicon("Maroc", {"N": {"g": "m", "tab": ["n1"]}})
    #
    # dependancesFr = [
    #     [root(V("pleuvoir"),
    #           subj(Pro("lui").c("nom")),
    #           mod(P("dans"),
    #               comp(N("maison"),
    #                    det(D("mon").pe(1))))), "Il pleut dans ma maison. "],  # 0
    #     [root(V("bâtir").t("ps"),
    #           subj(Pro("moi").c("nom")),
    #           comp(N("cabane").n("p"),
    #                det(D("un")),
    #                mod(A("petit")),
    #                mod(A("rouge"))),
    #           mod(P("en"),
    #               mod(Q("1998")))), "Je bâtis des petites cabanes rouges en 1998. "],  # 1
    #     [root(V("manger"),
    #           subj(Pro("vous").c("nom")),
    #           coord(C("et"),
    #                 comp(N("pomme"),
    #                      det(D("un"))),
    #                 comp(N("orange"),
    #                      det(D("un"))).n("p"))),
    #      "Vous mangez une pomme et des oranges. "],  # 2
    #     [root(V("être"),
    #           subj(Pro("ce")),
    #           mod(Adv("alors")),
    #           comp(Q("Alba"),
    #                coord(C("et"),
    #                      mod(V("reprendre"),
    #                          subj(Pro("qui")),
    #                          comp(N("contrôle"),
    #                               det(D("le")),
    #                               comp(P("de"),
    #                                    comp(N("situation"),
    #                                         det(D("le")))))),
    #                      mod(V("réprimer"),
    #                          subj(Pro("qui")),
    #                          comp(N("révolte"),
    #                               det(D("un")),
    #                               comp(P("de"),
    #                                    comp(N("peuple"),
    #                                         det(D("le")))),
    #                               comp(P("devant"),
    #                                    comp(N("cour"),
    #                                         det(D("le")),
    #                                         mod(A("royal"))))))))),
    #      "C'est alors Alba qui reprend le contrôle de la situation et qui réprime une révolte du peuple devant la cour royale. "],
    #     # 3
    #     [root(V("courir"),
    #           coord(C("et"),
    #                 subj(N("chat"),
    #                      det(D("le"))),
    #                 subj(N("chien"),
    #                      det(D("le"))))),
    #      "Le chat et le chien courent. "],  # 4
    #     [root(V("avoir"),
    #           subj(Pro("lui").c("nom")),
    #           comp(N("peur"),
    #                comp(P("de"),
    #                     comp(N("araignée"),
    #                          det(D("le")))))),
    #      "Il a peur de l'araignée. "],  # 5
    #     [root(V("être"),
    #           mod(C("mais")).pos("pre"),
    #           subj(N("réalité"),
    #                det(D("le"))),
    #           comp(C("que"),
    #                comp(V("être"),
    #                     subj(N("Mauritanie"),
    #                          det(D("le"))),
    #                     coord(C("ou"),
    #                           comp(N("Maroc"),
    #                                det(D("le"))),
    #                           comp(N("Algérie"),
    #                                det(D("le"))))).typ({"neg": True}))),
    #      "Mais la réalité est que la Mauritanie n'est pas le Maroc ou l'Algérie. "],  # 6
    #     [root(V("manger"),
    #           subj(N("garçon"),
    #                det(D("le"))).n("p").pro(),
    #           coord(C("et"),
    #                 comp(N("pomme"),
    #                      det(D("un"))),
    #                 comp(N("orange"),
    #                      det(D("un"))).n("p"))),
    #      "Ils mangent une pomme et des oranges. "],  # 7
    #     [root(V("pleuvoir"),
    #           subj(Pro("lui").c("nom")),
    #           mod(P("dans"),
    #               comp(N("maison"),
    #                    det(D("mon").pe(1)))).pro()), "Il y pleut. "],  # 8
    #     [root(V("bâtir").t("ps"),
    #           subj(Pro("moi").c("nom")),
    #           comp(N("cabane").n("p"),
    #                det(D("un")),
    #                mod(A("petit")),
    #                mod(A("rouge"))).pro(),
    #           mod(P("en"),
    #               mod(Q("1998")))), "Je les bâtis en 1998. "],  # 9
    #     [root(V("manger"),
    #           subj(N("souris"),
    #                det(D("le"))),
    #           comp(N("fromage"),
    #                det(D("le")))).typ({"pas": True}),
    #      "Le fromage est mangé par la souris. "],  # 10
    #     [root(V("bâtir").t("ps"),
    #           comp(Pro("lui").c("acc")),
    #           mod(P("en"),
    #               mod(Q(1998)))).typ({"pas": True}),
    #      "Il fut bâti en 1998. "],  # 11
    #     [root(V("vendre"),
    #           subj(N("livre"),
    #                det(D("le"))),
    #           mod(Adv("bien"))).typ({"refl": True}),
    #      "Le livre se vend bien. "],  # 12
    #     [root(V("donner").t("pc"),
    #           subj(Pro("lui").c("nom")),
    #           comp(N("pomme"),
    #                det(D("un"))).pro()
    #           ).typ({"neg": True, "pas": True}),
    #      "Elle n'a pas été donnée par lui. "],  # 13
    #     [root(V("donner").t("p"),
    #           subj(Pro("lui").c("nom")),
    #           coord(C("et"),
    #                 comp(N("pomme"), det(D("un"))),
    #                 comp(N("poire"), det(D("un"))).n("p"))
    #           ).typ({"neg": True, "pas": True}),
    #      "Une pomme et des poires ne sont pas données par lui. "],  # 14
    #     [root(V('travailler').t("pc"),
    #           comp(Adv('bien')),
    #           subj(Pro('je').pe(2))).typ({"mod": "nece"}),
    #      "Tu as dû bien travailler. "],  # 15
    #     [root(V("manger").t("pc"),
    #           subj(N("souris"),
    #                det(D("le"))),
    #           comp(N("fromage"),
    #                det(D("le")))).typ({int: "wad", "pas": True}),
    #      "Par quoi le fromage a-t-il été mangé? "],  # 16
    #     [root(V('manger'),
    #           comp(N('fromage'),
    #                det(D('le'))),
    #           subj(Pro('elles'))).typ({"pas": True}),
    #      "Le fromage est mangé par elles. "],
    #     [root(N("fille"),
    #           coord(C("ou"),
    #                 det(NO(2)),
    #                 det(NO(3))),
    #           coord(C("et"),
    #                 mod(A("jeune")),
    #                 mod(A("joli"))).pos("pre")),
    #      "2 ou 3 jeunes et jolies filles. "],
    # ]

    # English dependences
    # loadEn()
    # dependenciesEn = [
    #     [root(V("walk"),
    #           subj(N("man"),
    #                det(D("a")))), "A man walks. "],  # 0
    #     [root(V("be"),
    #           subj(V("practice").t("pr"),
    #                comp(N("joke"),
    #                     det(D("my").pe(2).ow("s")))),
    #           mod(A("crucial"))), "Practicing your joke is crucial. "],  # 1
    #     [root(V("eat"),
    #           subj(Pro("him").c("nom")),
    #           comp(N("apple"),
    #                det(D("a"))).n("p").tag("em")).t("ps"), "He ate <em>apples</em>. "],  # 2
    #     [root(V("come").t("pr"),
    #           comp(P("into"),
    #                comp(N("area"),
    #                     det(D("the")))),
    #           comp(P("to"),
    #                comp(V("see").t("b"),
    #                     comp(N("concert"),
    #                          det(D("a"))).n("p")))),
    #      "Coming into the area to see concerts. "],  # 3
    #     [root(V("be").t("ps"),
    #           subj(Pro("it")),
    #           comp(P("from"),
    #                mod(Q("John"))),
    #           comp(C("that"),
    #                comp(V("hear").t("ps"),
    #                     subj(Pro("me").c("nom").g("f")),
    #                     comp(N("news"),
    #                          det(D("the")))))),
    #      "It was from John that she heard the news. "],  # 4
    #     [root(V("be"),
    #           subj(N("man"),
    #                det(D("every")),
    #                mod(V("be"),
    #                    subj(Pro("that")),
    #                    mod(V("miss").t("pr")))),
    #           comp(V("punish").t("pp")),
    #           comp(P("for"),
    #                mod(Pro("you")))),
    #      "Every man that is missing is punished for you. "],  # 5
    #     [root(V("stop").t("ps"),
    #           mod(Adv("nearly")).pos("pre"),
    #           subj(Pro("it")),
    #           comp(V("rain").t("pr"))).typ({"perf": True}),
    #      "Nearly it had stopped raining. "],  # 6 (differeent word order)
    #     [root(V("waste").t("ps"),
    #           mod(C("if"),
    #               comp(V("have").t("ps"),
    #                    subj(Pro("I")).pe(1),
    #                    comp(N("chance"),
    #                         det(D("a")),
    #                         mod(A("similar"))))).a(",").pos("pre"),
    #           subj(Pro("I").pe(1)),
    #           comp(Pro("it"))).typ({"mod": "will", "neg": True}),
    #      "If I had a similar chance, I would not waste it. "],  # 7
    #     [root(V("walk"),
    #           subj(N("man"),
    #                det(D("a"))).pro()), "He walks. "],  # 8
    #     [root(V("be"),
    #           subj(V("practice").t("pr"),
    #                comp(N("joke"),
    #                     det(D("my").pe(2).ow("s"))).pro()),
    #           mod(A("crucial"))), "Practicing it is crucial. "],  # 9
    #     [root(V("eat"),
    #           subj(Pro("him").c("nom")),
    #           comp(N("apple"),
    #                det(D("a"))).n("p").pro().tag("em")).t("ps"), "He ate <em>them</em>. "],  # 10
    #     [root(V("applaud").t("f"),
    #           comp(Pro("this"))).typ({"mod": "nece", "pas": True}), "This shall be applauded. "],  # 11
    #     [root(V("remember"),
    #           subj(Pro("you"))).typ({"int": "yon"}), "Do you remember? "],  # 12
    #     [root(V('eat'),  # 13
    #           comp(N('apple').n("p"), det(D('a'))).tag("em"),
    #           subj(N("man"), det(D("the")))).typ({"neg": False, "int": "tag"}),
    #      "The man eats <em>apples</em>, doesn't he? "],
    #     [coord(C("but"), root(V("laugh").t('ps'), subj(N("John"))),
    #            root(V("smack").t('ps'), subj(N("Mary")),
    #                 coord(C("and"), comp(N("butler"), det(D("the"))),
    #                       comp(N("maid"), det(D("the")))))),
    #      "John laughed but Mary smacked the butler and the maid. "],
    #     [root(V('move').t("p").pe(3).n("s"),
    #           subj(N('star').n("s"),
    #                det(D('the')),
    #                mod(N('north')).pos("pre")),
    #           comp(N('sky').n("s"),
    #                mod(P('in')).pos("pre"),
    #                det(D('the'))),
    #           comp(N('hemisphere').n("s"),
    #                mod(P('in')).pos("pre"),
    #                det(D('the')),
    #                mod(A('northern')).pos("pre")),
    #           comp(N('night').n("s"),
    #                det(D('each')))).typ({"neg": True, "int": "why"}),
    #      "Why does the north star not move in the sky in the northern hemisphere each night? "],
    #     [root(V('eat'),
    #           comp(N('cheese'),
    #                det(D('the'))),
    #           subj(Pro('him'))).typ({"pas": True}),
    #      "The cheese is eaten by him. "],
    # ]
    #
    # # bilingual example
    # loadFr();
    # dest = NP(D("le"), N("monde"));
    # loadEn();
    # constituentEnFr = \
    #     S(Pro("I").pe(1),
    #         VP(V("say"),
    #          "hello",
    #         PP(P("to"), dest.tag("b"))))

def showEx(exemple):
    print(exemple[0].realize())


def testAllEx(fn, exemples):
    for ex in exemples:
        fn(ex)


# test a single expression (useful for launching the debugger on a given expression
# proper language must be chosen before calling... because the parameter is evaluated before the function call
def test(exp):
    print(exp.toSource(0))
    print(exp.realize())
    print("---")


def showDiffs(nomEx, nbDiffs, nbTests):
    if currentLanguage() == "en":
        if nbDiffs == 0:
            print(f"{nomEx} :: *** no differences over {nbTests} tests")
        else:
            print(f"{nomEx} :: *** {nbDiffs} difference{'' if nbDiffs == 0 else 's'} over {nbTests} tests")
    else:
        if nbDiffs == 0:
            print(f"{nomEx} :: *** aucune différence sur {nbTests} tests");
        else:
            print(f"{nomEx} :: *** {nbDiffs} différence{'' if nbDiffs == 0 else 's'} sur {nbTests} tests")


def checkAllEx(nomEx, exemples):
    nb = len(exemples)
    nbDiffs = 0;
    for i in range(nb):
        exp = exemples[i][0].clone()
        # console.log(exp.toSource());
        gen = exp.realize()
        expected = exemples[i][1]
        if expected is not None and gen != expected:
            print(f"{i}:{exp.toSource()}\n => {gen}\n ** {expected}", i, exp.toSource(), gen, expected)
            nbDiffs += 1
    showDiffs(nomEx, nbDiffs, nb)


# def checkAllExDep(nomEx, exemples):
#     lang = getLanguage()
#     nb = exemples.length;
#     nbDiffs = 0
#     nbTests = 0;
#     for i in range(nb):
#         if exemples[i][2] is not None:
#             console.log(lang == "en"?"**:skip example %d: %s": "**:saute exemple %d:%s", i, exemples[i][2])
#             else:
#             exp = exemples[i][0].clone();
#             dep = exp.toDependent();
#             # show(dep);
#             gen = dep.realize();
#             expected = exemples[i][1];
#             if expected is not None & & gen != expected:
#                 print("%d:%s\n %s\n => %s\n ** %s" % (i, exp.toSource(), dep.toSource(), gen, expected))
#                 nbDiffs + +;
#             nbTests + +;
#     showDiffs(nomEx, nbDiffs, nbTests)


# function checkAllExJSON(nomEx,exemples){
#     const nb=exemples.length;
#     let nbDiffs=0;
#     for (var i=0;i<nb;i++){
#         const expJS=exemples[i][0].toJSON();
#         const genJS=fromJSON(expJS).realize();
#         const expected=exemples[i][1];
#         if (expected!==null && genJS!=expected){
#             console.log("%d:%s\n => %s\n ** %s",i,ppJSON(expJS),genJS,expected)
#             nbDiffs++;
#         }
#     }
#     showDiffs(nomEx+"-JSON",nbDiffs,exemples.length);
# }


def testPreviousExamples():
    makeExamples();
    loadFr();
    checkAllEx("exemplesFr", exemplesFr);
    # checkAllExDep("exempleFrDep",exemplesFr);
    # checkAllExJSON("exemplesFr",exemplesFr);
    # checkAllEx("dependancesFr",dependancesFr);
    # console.log("----")
    # loadEn();
    # checkAllEx("exemplesEn",exemplesEn);
    # checkAllExDep("exempleEnDep",exemplesEn);
    # checkAllExJSON("exemplesEn",exemplesEn);
    # checkAllEx("dependenciesEn",dependenciesEn)
    # console.log("----")
    # # cannot use checkAllEx because it does a clone() and the language is changed...
    # const realEnFr = constituentEnFr.realize()
    # if (realEnFr == "I say hello to <b>le monde</b>. "){
    #     console.log("bilingual: OK")
    # } else {
    #     console.log("bilingual:KO",realEnFr)
    # }
    # console.log("----")
    # testWarnings()


# def show(exp):
#     print(exp.realize())

# ## some examples that were used during development
#
# def english():
#     # a few examples generates warnings shown here as comments
#     loadEn()
#     exp=S(CP(C("and"),NP(D("the"),N("apple"))),        # 13
#           VP(V("be"),A("good")))
#     print(exp.toDependent().toSource(0))
#     show(exp.toDependent())
#     # sys.exit(0)
#     exp=S(Pro("him").c("nom"),
#        VP(V("eat"),                                 # 11
#           NP(D("a"),N("apple").n("p"))
#           .add(A("red")))).add(Adv("now").a(","),0)
#     print(exp.toDependent().toSource(0))
#     show(exp.toDependent())
#     show(root(V("eat"),subj(Pro("him").c("nom"))).add(comp(Adv("now")).a(',').pos("pre")))
#     show(root(V("eat"),
#                comp(N("apple").n('p'),
#                     det(D("a"))).add(mod(A("red"))),
#                subj(Pro("him").c('nom'))).add(comp(Adv("now")).a(',').pos("pre")))
#     show(S(Pro("him").c("nom"),                      # 20
#          VP(V("eat"),
#             NP(D("a"), N("apple").tag("a", {"href":"https:#en.wikipedia.org/wiki/Apple"})))).clone())
#     show(S(CP(C("and"), NP(D("the"), N("apple"))), VP(V("be"), A("good"))))
#     show(V("reserve").t(""))  # V('reserve'):: : this bad value for option t is ignored.
#     show(N())  # N(None):: the parameter should be string, not NoneType.
#     show(DT())
#     show(DT(datetime.datetime.today()).dOpt({'rtime': True}))
#     show(DT("2021-09-01").dOpt({"rtime": "2021-08-27","hour":false,"minute":false,"second":false}))
#     show(DT().dOpt({'rtime': datetime.datetime.today()-datetime.timedelta(days=4)}))
#     show(DT(datetime.datetime.today()-datetime.timedelta(days=5)).dOpt({'rtime': True}))
#     show(DT(None).dOpt({"det": False}))
#     s = lambda: S(Pro("I").pe(1),
#                   VP(V("say").t("ps"),
#                      NP(N("hello"),
#                         PP(P("to"), NP(D("the"), N("world").n("p")))))).typ({"pas": False, "neg": True})
#     show(S(NP(D("a"), N("cat").n("p"))))
#     show(s())
#     sJson = s().toJSON()
#     import json
#     json.dump(sJson, sys.stdout, indent=3)
#     print()
#     s1 = fromJSON(s().toJSON())
#     show(s1)
#     show(S(Pro("him").c("nom"),
#          VP(V("eat"),
#             NP(D("a"),N("apple").n("p")).tag("em")
#        )).typ({"int":"tag"}))
#     show(S(Pro("him").c("nom"),
#          VP(V("eat"),
#             NP(D("a"),N("apple").n("p")).tag("em")
#        )).typ({"int":"tag","neg":True}))
#     show(S(Pro("him").c("nom"),
#          VP(V("eat").t("c"),
#             NP(D("a"),N("apple").n("p")).tag("em")
#        )).typ({"int":"tag"}))
#
# def francais():
#     loadFr()
#     exp=S(Pro("je"),
#         VP(V('manger').t("pc"),
#            NP(D('le'),
#               N('fromage')))).typ({"int":"tag"})
#     show(exp)
#     show(S(Pro("moi").pe(1),VP(V("aimer"))).typ({"pas":True}))
#     show(S(NP(D("le"), N("chat")).n("p"), VP(V("asseoir"))).typ({"refl": True}))
#     addToLexicon({"John": {"N": {"g": "m", "tab": "n35"}}})
#     addToLexicon({"Mary": {"N": {"g": "f", "tab": "n36"}}})
#
#     show(S(NP(D("le"), N("chat")),
#             VP(V("manger"),
#                NP(D("le"), N("souris")))).typ({'int': 'yon', 'neg': true})
#           )
#     show(S(Pro("lui").c('nom').pe(3).g('m').n('s'),
#             VP(V("donner").t('pc'), NP(D("un"), N("pomme")).pro(),
#                PP(P("à"), NP(D("le"), N("fille"))).pro())
#             ).typ({'neg': False, 'pas': True}))
#     show(VP(V("aller").t("pc").pe(2).n("p")).typ(1)) # VP(V('aller')):: int:1 : cette mauvaise valeur pour l'option .typ est ignorée
#     show(S(Pro("moi").c("nom").pe(3).n("p"), VP(Pro("eux").c('refl'), V("évanouir").t('pc'))).typ({"neg": True}))
#     show(S(CP(C("et"), NP(N("John")), NP(N("Mary"))), VP(V("évanouir").t('pc'))).typ({"neg": True, "refl": True}))
#     show(S(Pro("je").pe(1).n('p'),
#             VP(V("agir").t('p'),
#                AdvP(Adv("conformément"),
#                     PP(P("à"), NP(D("le"), N("loi"))))).typ({'neg': True})))
#     show(S(Pro("lui").c("nom"),
#             VP(V("parler").t("pc"),
#                PP(P("à"), NP(D("mon"), N("ami"))).pro(),
#                PP(P("de"), NP(D("mon"), N("problème"))).pro())))
#     show(S(NP(D("un"), N("garçon").g("f")), #N('garçon'):: erreur de morphologie : genre différent de celui du lexique N('garçon') :{'g': 'f', 'lexique': 'm'}
#             VP(V("travailler"),
#                PP(P("sur"), N("internet")))).typ({"neg": True}))
#     # show(V("cliquer").t("pc").pe(1))
#     show(V("repentir").t('p').pe(2).n('s'))
#     show(V("repentir").t('ip').pe(2).n('s').lier())
#     # show(PP(P("sur"),N("internet")))
#     show(S(NP(D("un"), N("garçon").g("f")),
#             # erreur de morphologie : genre différent de celui du lexique N('garçon') :{'g': 'f', 'lexique': 'm'}.
#             VP(V("travailler"),
#                PP(P("sur"), N("internet")))))
#     show(S(NP(D("le"), N("élève").g('f')),
#             VP(Pro("moi").pe(1).c('dat'), V("dire"),
#                PP(P("de"), VP(V("interroger").t('b'),
#                               NP(D("le"), N("élève").g('f')).pro(None))
#                   .typ({'neg': True})))))
#     show(VP(V("aimer").t("ip").pe(2).n("s")).typ({"refl": True}))
#     show(S(Pro("je").pe(2), VP(V("enfuir"))))
#     show(S(Pro("je").pe(2).n("p"), VP(V("laver").t("pc"))).typ({"refl": True}))
#     show(S(Pro("je").pe(2), VP(V("savoir"))).typ({"pas": True}))
#     show(S(NP(D("le"), N("chat")), VP(V("manger"))).typ({"pas": True}))
#     show(oneOf([lambda: N("amour"), lambda: N("amitié")]))
#     show(oneOf([lambda: N("amour"), lambda: N("amitié")]))
#     show(oneOf(lambda: N("amitié")))
#     show(oneOf(lambda: N("amour"), lambda: N("amitié")))
#     show(NO(4).nat())
#     show(NO(4).dOpt({"nat": True}))
#     show(D("un", "B"))  # D('un'):: langage devrait être  "en" ou  "fr" , ce sera fr.
#     c = lambda: NP(D("un"), N("chat"))
#     show(c())
#
#     s = CP(C("et"), NP(NO("1").nat(True), N("consultation")), NP(NO("2").nat(True), N("atelier")))
#     print(s.toSource())
#     show(s)
#     show(DT(None))
#     show(DT("").dOpt({"det": False}))
#     show(S(NP(D("le"),
#                N("chat").n("p"),
#                SP(Pro("que"),
#                   NP(D("le"),
#                      N("chat").g("f").n('p')),
#                   VP(V("manger").t('pc')))),
#             VP(V("être").t('p'),
#                AP(A("gris")))))
#
#
# def dependent_fr():
#     loadFr()
#     pommeS = subj(N("pomme"),det(D("le")))
#     gars = subj(N("garçon").n("p"),det(D("le")))
#     addToLexicon({"John":{"N":{"g":"m","tab":"n4"}}})
#     addToLexicon({"Mary":{"N":{"g":"f","tab":"n16"}}})
#
#     show(root(N("test")))
#     show(V("repentir").t('p').pe(1).n('s'))
#     show(root(V("manger").t("pc"),
#                   subj(N("souris"),
#                        det(D("le"))),
#                   comp(N("fromage"),
#                        det(D("le")))).typ({"int": "wad", "pas": true}))
#     show(root(V("manger").t("pc"),
#                   subj(N("souris"),
#                        det(D("le"))),
#                   comp(N("fromage"),
#                        det(D("le")))).typ({"int": "tag"}))
#     show(root(V('demander').t("pc"),
#                   comp(N('adresse'),
#                        det(D('mon'))).pro(),
#                   comp(P('à'),
#                        mod(N('parent').n("p"),
#                            det(D('mon')))).pro(),
#                   subj(Pro('je').pe(2))))
#     show(root(V("manger").t("f"),
#                subj(N("chat"),
#                     det(D("le"))).n("p"),
#                comp(N("souris"),
#                     det(D("un")))).typ({"neg":True}))
#     show(root(V('être').t("p"),
#                comp(A('gris')),
#                subj(N('souris'),
#                     det(D('le')),
#                     mod(V('manger').t("pc"),
#                         comp(Pro('que')).pos("pre"),
#                         subj(N('chat').n("p"),
#                              det(D('le')))))))
#     show(root(N('cadeau').n("p"),
#                  mod(A('beau'))))
#     show(root(N('gens').n("p"),
#                  det(D('le')),
#                  mod(A('vulgaire').pos("pre"))).cap(false))
#     show(root(N('père'),
#                  det(D('le')),
#                  mod(P('de'),
#                      mod(N('fille'),
#                          det(D('mon').pe(1))))))
#     show(root(V('manger'),
#                  comp(N('gâteau'),
#                       det(D('le'))),
#                  subj(N('enfant').n("p"),
#                       det(D('le'))).pro()))
#     show(root(V('manger'),
#                  comp(N('gâteau'),
#                       det(D('le'))).pro(),
#                  subj(N('enfant').n("p"),
#                       det(D('le')))))
#     show(root(V('manger'),
#                  comp(N('gâteau'),
#                       det(D('le'))),
#                  subj(N('enfant').n("p"),
#                       det(D('le')))).typ({"pas":True}))
#     show(root(V('venir').t("pc"),
#              comp(Adv('hier')),
#              coord(C('et'),
#                    subj(N('fruit'),
#                         det(D('le')))).add(pommeS).add(gars)))
#
# def dependent_en():
#     loadEn()
#     # show(root(V("run"),subj(N("cat"),det(D("the"))).pro()))
#     show(root(V("play").t("f"),
#                            subj(N("cat"),det(D("a"))),
#                            comp(N("piano"))).typ({"neg":true}))
#     show(root(V("sit").t("ps"),
#               subj(N("cat"),det(D("the"))),
#               comp(P("on"),mod(N("couch"),det(D("the"))))))
#     show(root(V("sit").t("ps"),
#               subj(N("cat"),det(D("the"))),
#               comp(P("on"),mod(N("couch"),det(D("the"))))).typ({"int":"tag"}))
#     show(root(V("sit").t("ps"),
#               subj(N("cat"),det(D("the"))),
#               comp(P("on"),mod(N("couch"),det(D("the"))))).typ({"int":"tag","perf":true}))
#     show(root(V("like").t("pr"),
#                subj(N("dog").n("p"),mod(A("nice"))),
#                comp(N("cat"),
#                     det(D("a"))).n("p")))
#     show(root(V('love'),
#                  comp(N('woman'),
#                       det(D('a'))).pro(),
#                  subj(Pro('I').g("m"))))
#     s = lambda: root(V("say").t("ps"),
#                      subj(Pro("I").pe(1)),
#                      comp(N("bye")),
#                      comp(P("to"),
#                           mod(N("world"),
#                               det(D("the"))))).typ({"pas": False, "neg": True})
#     show(s())
#     sJson = s().toJSON()
#     import json
#     json.dump(sJson, sys.stdout, indent=3)
#     print()
#     s1 = fromJSON(s().toJSON())
#     show(s1)
#
# def dependentTransformation():
#     s = lambda: S(Pro("I").pe(1),
#                   VP(V("say").t("ps"),
#                      NP(N("hello"),
#                         PP(P("to"), NP(D("the"), N("world").n("p")))))).typ({"pas": False, "neg": True})
#     print(s().toDependent().toSource(0))
#     show(s().toDependent())
#
# ## test a single expression (useful for launching the debugger on a given expression
# ## proper language must be chosen before calling... because the parameter is evaluated before the function call
# def test(exp):
#     print(exp.toSource(0))
#     print(exp.realize())
#
# # test_warnings()
#
# def testPrevious():
#     print(f"Previous tests of pyrealb: Version {pyrealb_version} Date: {pyrealb_datecreated}")
#     print("** English **")
#     english()
#     print("======")
#     print("** Français **")
#     francais()
#     print("======")
#     print("** Dépendances françaises **")
#     dependent_fr()
#     print("======")
#     print("** English dependencies **")
#     dependent_en()
#     print("======")
#     dependentTransformation()
#
#     # check list of list of parameters for Phrase
#     loadEn()
#     test(S(NP(D("the"),[N("cat"),A("white")],VP([V("sit"),[PP(P("on"),[NP(D("the"),N("mat"))])]]))))
#     # check position of an adjective
#     test(NP(oneOf(N("family").lier(),N("kid")),A("friendly").pos("post")))
#
#     loadFr()
#     test(NP(N("chat"),A("blanc").pos("pre")))
#     test(NP(N("chat"),A("petit")))
#     test(NP(N("chat"),A("noir")))
#
#     loadEn()
#     test(root(V("be").t("p"),
#              subj(Pro("I").n("s").pe(1)),
#                 comp(P("on"),mod(N("couch"),det(D("the"))))).typ({"int":"tag","perf":True}))
#     test(S(Pro("I").pe(1),VP(V("be"),PP(P("on"),NP(D("the"),N("couch"))))).typ({"int":"tag"}))
#
#     test(S(VP(V("go").t("b"))).typ({"neg":True}))
#     test(S(VP(V("go").t("b-to"))).typ({"neg":True}))
#     test(V("love").t("ip").pe(1).n("p"))
#     test(S(Pro("I").n("p"),VP(V("answer").t("c"))))
#
#     addToLexicon("John", {"N": {"tab": "nI", "g": "m"}})
#     addToLexicon("Mary", {"N": {"tab": "nI", "g": "f"}})
#     addToLexicon("Fred", {"N": {"tab": "nI", "g": "m"}})
#     addToLexicon("Maria-Luz", {"N": {"tab": "nI", "g": "f"}})
#     addToLexicon("firefighter", getLemma("fighter"))
#     # test(root(V("like"),comp(N("John")),subj(N("Mary"))).typ({'int': 'wod'}))
#
#     test(coord(C("but"),root(V("laugh").t('ps'),subj(N("John"))),
#                         root(V("smack").t('ps'),subj(N("Mary")),
#                              coord(C("and"),comp(N("butler"),det(D("the"))),
#                                    comp(N("maid"),det(D("the")))))))
#     loadFr()
#     test(PP(P("de"),NO(8).nat()))
#     test(V("asseoir").t("pp").n("p"))
#
#     loadFr()
#     test(S(NP(D("le"), N("chat")).n("p"),
#              VP(V("asseoir").t("pc"),
#                 PP(P("sur"),
#                    NP(D("le"), N("tapis"))))).typ({"int": "tag", "neg": True, "refl": True}))
#     test(V("asseoir").t("pc").pe(3).n("p").tag("em"))
#
#     loadEn()
#     en1 = NP(D("the"), N("cat").n("p"))
#     en2 = NP(D("a"), N("mat")).n("p")
#     loadFr()
#     test(S(en1,
#              VP(V("asseoir").t("pc").tag("em"),
#                 PP(P("sur").tag("em"),
#                    en2))).typ({"refl": true, "int": "tag"}))
#
#     test(S(Pro("ce"),V("être").t("pc")))
#
#     loadEn()
#     test(S(V("show").t("ip"),
#                      NP(D("a"),N("airline").n("p"),
#                         SP(Pro("that"),
#                            VP(V(oneOf("fly","go")))))))

if __name__ == '__main__':
    testPreviousExamples()
    # testPrevious()
    # insert here a single example for debugging perhaps commenting the line above
    # do not forget to load the appropriate language
    loadEn()
    loadFr()
