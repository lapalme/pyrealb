# Summarizing Basketball Games

[Guy Lapalme](mailto:lapalme@iro.umontreal.ca), Université de Montréal, July 2023

This paper describes ***SportSettSum***, a rule-based data-to-text Natural Language Generation (NLG) for generating English and French *statistic-focused summaries of basketball games* using information found in the [SportSett:Basketball](https://gem-benchmark.com/data_cards/sportsett_basketball) dataset (Thomson *et al*.,2020). This dataset combines scores and performance measures about the teams and the players of thousands of NBA games with human-authored summaries about these games. This dataset is a *clean-up* and redesign of the Rotowire (Wiseman et al. 2017) dataset which had been used to develop Seq2Seq models for generating paragraph-sized texts.  

*SportSett:Basketball* has been used in experiments about the evaluation of factual accuracy in automatically generated texts (Thomson *et al.*, 2023) and in an [Accuracy Evaluation shared task](https://aclanthology.org/2021.inlg-1.23.pdf), but we could not find any documented use of this dataset by an NLG (neural or not) system to produce complete summaries. This seems surprising given the recent surge of interest in NLG based on GPT-*n* systems, probably because most of these struggle not to *hallucinate* when given verifiable data. This means that NLG evaluation based on BLEU or other automatic metrics cannot be relied upon anymore and is thus much more time consuming and probably more complicated than developing the systems themselves.

Our goal here is not to develop an industrial system or to *beat* any GPT look-alike, but to display a use case  the [pyrealb bilingual text realizer](https://github.com/lapalme/pyrealb) for creating French and English documents from statistical data. The system is developed in Python and its source code is available in this GitHub directory. The human-authored summaries in *SportSett:Basketball* were used as an English corpus for developing appropriate phrasings.  

*Warning*: we are not a basketball expert, nor even a fan.  At the start of this project, we had to develop a [personal lexicon of the main terms](SportSett-GEM.md) such as field *goals*, *turnovers*, *rebounds*, *steals*, *blocks*, etc. by searching the internet. We had never read a basketball game summary before.  So seasoned basketball fans will surely find quite naive our analysis of the games and players. This warning applies even more to French for which we do not even have any reference summary.

But this is not the main point of this exercise whose takeaway lesson is the process of going from data to the text by roughly following the steps of the *now classical* architecture proposed by Reiter (2007): 

- **Signal analysis**: analyzing input data looking for patterns
- **Data interpretation**:  identifying domain-specific messages from patterns and causal relations between messages
- **Document planning**: deciding which messages to mention and rhetorical structure in the generated text.
- **Realization**: creating the actual text

# 1 - Description of the input data

Before describing the system, we  give an overview of the input data, the specifics of which can be found in the source code. 

The [SportSett:Basketball](https://gem-benchmark.com/data_cards/sportsett_basketball) dataset (Thomson *et al*.,2020) is a relational database about NBA games between 2014 and 2018 which allows very detailed queries. But in our experiments, we restricted ourselves to the *JSON* version available in [GEMv2](https://aclanthology.org/2022.emnlp-demos.27/) as a *[Hugging Face dataset](https://gem-benchmark.com/data_cards/sportsett_basketball)* with three splits:

| Split      |   NBA seasons    | Games |
| ---------- | :--------------: | ----: |
| Train      | 2014, 2015, 2016 |  3690 |
| Validation |       2017       |  1230 |
| Test       |       2018       |  1230 |

Each game is described by global information such as the date, the stadium and the city where the game was played. Each team (*home* and *visitors*) is described by its name, its city, its current conference standing and quite detailed information about the scores: 

- *line-scores* of the teams  for each quarter, half and complete game; 
- *box-scores* for each player

Finally, there is a link to the next game of each team.  There are also one or two human-written summaries per game.

The detailed statistics give information about the number of points, of attempted and made field goals, of blocks, of assists, etc. The following table gives the box-scores for the Philadelphia 76ers in their game against the Miami Heat on November 1, 2014, the first game of the *Train* dataset which we use as running example in this paper. The head of tables follow the same conventions as the used for the [official scores](https://www.basketball-reference.com/boxscores/201411010PHI.html). 

| Game |  FGM |  FGA | FG3M | FG3A |  FTM |  FTA | OREB | TREB |  AST |  STL |  BLK |  TOV | PF   | PTS  |
| :--: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---- | ---- |
|  Q1  |   13 |   21 |    3 |    8 |    1 |    2 |    2 |   10 |   10 |    2 |    5 |    6 |      | 30   |
|  Q2  |    8 |   15 |    0 |    2 |    8 |   12 |    1 |   11 |    7 |    1 |    1 |    4 |      | 24   |
|  Q3  |   10 |   16 |    4 |    8 |    5 |    6 |    1 |   10 |    9 |    2 |    2 |    6 |      | 29   |
|  Q4  |    4 |   15 |    0 |    5 |    5 |    6 |    0 |    6 |    2 |    4 |    2 |    8 |      | 13   |
| game |   35 |   67 |    7 |   23 |   19 |   26 |    4 |   37 |   28 |    9 |   10 |   24 | 21   | 96   |

The following shows the data for the 4  (out of the 12) Philadephia players scoring the most points in this game.

| PLAYER          | STRT  |  MIN |  FGM |  FGA | FG3M | FG3A |  FTM |  FTA | OREB | TREB |  AST |  STL |  BLK |  TOV |   PF |  PTS |  +/- |
| :-------------- | :---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Tony Wroten     | True  |   33 |    6 |   11 |    1 |    4 |    8 |   11 |    0 |    3 |   10 |    1 |    1 |    4 |    1 |   21 |  -11 |
| Brandon Davies  | False |   23 |    7 |    9 |    1 |    2 |    3 |    4 |    0 |    3 |    0 |    3 |    0 |    3 |    3 |   18 |   -1 |
| Hollis Thompson | True  |   32 |    4 |    8 |    2 |    5 |    0 |    0 |    0 |    1 |    2 |    0 |    3 |    2 |    2 |   10 |  -17 |
| Henry Sims      | True  |   27 |    4 |    9 |    0 |    0 |    1 |    2 |    1 |    4 |    2 |    0 |    1 |    0 |    1 |    9 |  -10 |

The human written summary associated with this game (237 words) is the following in which we have underlined contextual information that cannot be found from a statistical analysis of the provided data (96 words, about 40%).  Note the typo in *Tornoto*, indicating that this summary was surely written by  a human !

> The Miami Heat (20) defeated the Philadelphia 76ers (0 - 3) 114 - 96 on Saturday. Chris Bosh scored a game - high 30 points to go with eight rebounds in 33 minutes. <u>Josh McRoberts made his Heat debut after missing the entire preseason recovering from toe surgery.</u> McRoberts came off the bench and played 11 minutes. <u>Shawne Williams was once again the starter at power forward in McRoberts' stead.</u> Williams finished with 15 points and three three - pointers in 29 minutes. Mario Chalmers scored 18 points in 25 minutes off the bench. <u>Luc Richard Mbah a Moute replaced Chris Johnson in the starting lineup for the Sixers on Saturday. Hollis Thompson shifted down to the starting shooting guard job to make room for Mbah a Moute.</u> Mbah a Moute finished with nine points and seven rebounds in 19 minutes. K.J. McDaniels, <u>who suffered a minor hip flexor injury in Friday's game, was available and</u> played 21 minutes off the bench, finishing with eight points and three blocks. <u>Michael Carter-Williams is expected to be out until Nov. 13, but Tony Wroten continues to put up impressive numbers in Carter-Williams' absence.</u> Wroten finished with a double - double of 21 points and 10 assists in 33 minutes. The Heat will complete a back - to - back set at home Sunday against the <u>Tornoto</u> Raptors. The Sixers' next game is at home Monday against the Houston Rockets.

### 1.1 - *Mundane* but important details

Data is often *tricky* even in well-organized directories such as the GEMv2. In this case, the data is always represented as a string, including integers, booleans and even `null` even though JSON can/should store these data types as such. We determined that the whole file would then about 15% smaller. So care must be taken when making computation, sorting or testing. We also discovered that the derived data for half-time of the games from the values of quarters had been computed by string concatenation of string values instead of the addition of the numeric values, curtesy of the overloading of the plus sign in  JavaScript or Python. 

Although the data is available as a [Hugging Face dataset](https://huggingface.co/docs/datasets/index), currently we do not use any of the interesting properties for accessing efficiently columnar data, we load the whole dataset once and process it like an array (`list` in Python) of JSON structures.

We have `def`ined Python classes (`Games`, `Game`, `Team`,  `Player` and  `Score`) with methods to access the JSON fields with more informative names than abbreviations and three letter keys. These functions convert the string values when required. Should we eventually want to use the database instead of the JSON as data source, we could (hopefully!) keep the same interface.  Some fields appearing in the JSON are not *exported*, because they seemed redundant (e.g., many details about the next game which can be accessed directly by fetching the game information in the database) or computable from other fields (e.g., the percentage of success that can be computed by dividing the number of *made* over the number of *attempted*).

After all these caveats, we can now start transforming the data into text. As illustrated above, and confirmed by reading other summaries, they mostly follow the usual pyramidal structure of newspaper articles. First, describe the global result before giving information about each team and then about the players that have an *high* scores. Finally, there is an indication of when and where will be played the next game for each team. 

Of course, it cannot be expected to mention contextual information about the health condition of the players or some contract agreements as such information does not appear in the input data and we will not *hallucinate* them.

#### Examples of output

For the *impatient*, here is one English summary produced by ***SportSettSum*** from the data described in the above example:

> The Heat, leader in their conference, overcame the 76ers 114-96 on Saturday at the Wells Fargo Center in Philadelphia. 
>
> The Heat led in all four quarters. 
>
> Chris Bosh who was a starter had an efficient performance scoring 30 points with four assists. Tony Wroten who was in the starting line-up scored a game high with 21 points  (6-11 FG, 1-4 3Pt, 8-11 FT) while adding ten assists and performed a double-double. 
>
> The Heat showed 49 percent from the field and 20-29 free throws.  Mario Chalmers who started this game had 20 points with 6-for-9 FG.  Luol Deng recorded 15 points with seven points.  Shawne Williams added 15 points with 5-for-9 FG and four assists.  Dwyane Wade ended up with nine points with ten assists. 
>
> The 76ers showed 52 percent from the field and 19-26 free throws and committed 24 turnovers.  Brandon Davies who was a starter finished with 18 points  (7-9 FG, 1-2 3Pt, 3-4 FT)  Luc Mbah a Moute contributed an efficient nine points with seven rebounds and three assists.  Malcolm Thomas scored eight points in 19 minutes  (4-4 FG, 0-0 3Pt, 0-0 FT)  Alexey Shved posted six points with six assists. 
>
> For their next game, the Heat will receive the Toronto Raptors on Sunday. For their next game, the 76ers will be at home against the Houston Rockets on Monday. 

***SportSettSum*** can also generate a French summary such as the following. Because of the randomization between the phrasing choices, the French version is not a literal translation of the English, but it conveys the same information. Both realizers work from the same original data and use the same algorithm for selecting the information to convey.

> Les Heat, meneurs dans leur conférence, ont dominé les 76ers 114-96 samedi au stade Wells Fargo Center à Philadelphia. 
> 
>Les Heat ont mené dans les quatre quarts. 
> 
>Chris Bosh qui figurait dans l'alignement de départ a réalisé une performance excellente comptant 30 points  (9-17 L, 2-5 L3, 10-11 LF) tout en ajoutant quatre passes décisives. Tony Wroten qui débutait la partie a mené, comptant 21 points  (6-11 L, 1-4 L3, 8-11 LF) et dix passes décisives et a terminé avec un double-double. 
> 
>Les Heat ont compté 49 pour cent de tirs réussis et 20-sur-29 lancers francs.  Mario Chalmers qui figurait dans l'alignement de départ a terminé avec 20 points avec 6-sur-9 L.  Luol Deng a eu 15 points avec 7-sur-11 L.  Shawne Williams a marqué 15 points avec 5-sur-9 L et quatre passes décisives.  Dwyane Wade a ajouté neuf points  (4-18 L, 0-1 L3, 1-3 LF) et dix passes décisives. 
> 
>Les 76ers ont compté 52 pour cent de tirs réussis et 19-sur-26 lancers francs et ont subi 24 pertes de ballon.  Brandon Davies qui était un partant a contribué un efficace 18 points  (7-9 L, 1-2 L3, 3-4 LF)  Luc Mbah a Moute a enregistré neuf points  (4-10 L, 0-2 L3, 1-2 LF) tout en ajoutant trois passes décisives.  Malcolm Thomas a fini avec huit points en 19 minutes  (4-4 L, 0-0 L3, 0-0 LF)  Alexey Shved a terminé avec six points avec six passes décisives. 
> 
>Pour leur prochaine partie, les Heat accueilleront les Raptors de Toronto dimanche. Pour leur prochaine partie, les 76ers seront à domicile contre les Rockets d'Houston lundi. 

## 2 - Architecture of the generation process

We now describe the steps going from the input data to the final text following the steps identified by Reiter. 

## 2.1 - Signal analysis

This first step looks for patterns in the data that will appear in the summary.  Human summaries start by naming the winner and loser teams with their scores. Then the best players' performances are given. Finally, information is given about the next games for both teams.

The game results and the information about the next game can be found directly in the JSON, as is the performance of the players who, in each team, scored the most points. But determining which player should be mentioned next with what appropriate information needs more work. It would be useless, and boring, to list the performances of each player, given that this information is available in the table which could be displayed or available on request. 

## 2.2 - Data interpretation

In order to focus on the most significant aspects, we decided to preprocess the training corpus to aggregate the performances of each player in all games in which he played more than one minute, ignoring the team. The summary will mention a player if he has an *high* number of field goals, three-pointers, rebounds or assists. Currently *high* is defined as being in the first quintile (best 20%) of all his scores.

Similarly, for each team,  points for all games in which it was part are aggregated. This information is used for choosing the aspects worth mentioning when talking about a team using the same criterion. 

As the statistics are only computed on the training corpus (season 2014-2016), they are not available for a few good *rookies* (e.g. Bogdan Bogdanović who arrived in 2018) when the summarizer is run on the validation or the test corpora which cover the 2017 and 2018 seasons. The realizer will still mention them if they are the best scorer in a given game. 

## 2.3 - Document planning

The pseudo-code for the summarizing a `game` is the following (paragraphs numbers will be used later for reference):

```
1. Give the winner and loser scores with location and date information about the game
2. Check for interesting turning points
3. Give information about the best players of both teams
4. For each  team in [winner,loser]
		4.1 Show global team performance
		4.2 For each player of the team (in decreasing order of points scored)  
					if player has any high score
						give information about this player
5. give information about the next games for the winner and the loser
```



## 2.4 - Realization

The symbolic and rule-based realizer ***SportSettSum*** is implemented by means of  Python 3 classes using the package `pyrealb`. Three classes were defined: one for the English realizer, another for the French realizer and another one using only Python string concatenation for comparison purposes. These three realizer classes share the same external signature. The summarizer calls realizers' classes methods that correspond to the steps of the document planning defined above.

Before describing the organization of the realizer classes, we recall the essentials of `pyrealb`. 

### 2.4.1 - Introduction to `pyrealb` 

[`pyrealb`](https://github.com/lapalme/pyrealb) is a Python port of [jsRealB](https://arxiv.org/pdf/2012.15425.pdf) which was strongly influenced by SimpleNLG (Gatt & Reiter, 2009) in which realization is achieved by programming language instructions that create data structures corresponding to the elements of the sentence to be realized. Once the data structure is built, it is traversed to produce a string.

Like SimpleNLG, `pyrealb` has the following components:

- morphological rules to determine the appropriate word forms, such as plurals and conjugations;
- a lexicon defining the word category, gender, number, declension and conjugation rule number and other features needed to produce the final token;
- syntactic rules to properly order words in a sentence, perform agreement between constituents and carry out other interactions.

`pyrealb` has these components for both French and English with other *goodies*, such as the spelling out of numbers and the wording of temporal expressions that are especially useful in data to text applications. 

`pyrealb` accepts either a *Constituent* or a *Dependent* notation for building sentences. For ***SportSettSum***, we use the *Constituent* notation. The data structure is built by class constuctor calls whose names are similar to the symbols typically used for constituent syntax trees:

- **Terminal**: `N` (noun), `V` (verb), `A` (adjective), `D` (determiner), `Pro` (pronoun), Adv (adverb), `P` (preposition), `C` (conjunction), `NO` (number), `DT` (date), `Q` (quoted/canned text). A terminal is created with a single parameter, most often a string, its lemma.
- **Phrase** for combining its parameters, i.e. terminals and other phrases: `S` (Sentence), `SP` (Subjective Phrase), `NP` (Noun Phrase), `VP` (Verb Phrase), `AP` (Adjective Phrase), `CP` (Coordinate Phrase), `PP` (Prepositional Phrase), `AdvP` (Adverbial Phrase).

Features are added to these structures using the dot notation to modify their properties. For terminals, their person, number, gender can be specified. For phrases, the sentence may be negated or set to a passive mode; a noun phrase can be pronominalized. Punctuation signs and HTML tags can also be added.

The main advantage of using a Python-based notation is the fact that programming constructs can be used to incrementally build a structure before being realized. The following example illustrates some of these capabilities in a small program to create parts of structures. 

```python
quality = oneOf(A("strong"),A("skilled"),A("talented"))
player  = NP(D("the"),N("player"),quality)
score   = VP(V(oneOf("score","win")))
score.add(NP(NO(25),N("point")))
```

The `oneOf` function, returning one of its arguments chosen at random, allows for varying between synonyms or similar formulations. The `add` method is used to incrementally build the structure that can then be realized as a string using the `realize` method.   For example, the result of the evaluation of 

```python
S(player,score).t("ps").realize()
```

can be  `The talented player scored 25 points.` Note that the past tense is applied to the whole structure before realization. Other types of modifications can also be done on the original structure. The following example shows a case of negative passive sentence at the future tense. `25 points will not be won by the strong player.`

```python
S(player,score).t("f").typ({"neg":True, "pas":True}).realize()
```

Functions can also be defined for creating recurrent patterns such as the following which, given a `Team` instance, will generate a structure that will be realized as either `the Heat` or `the Miami Heat` if the second parameter is `True`. 

```python
  def team_np(self, team, with_place=False):
      return NP(D("the"),
                Q(team.place()) if with_place else None,
                Q(team.name())).n("p")
```

### 2.4.2 - Realizer class organization

The following shows the methods of the English realizer that are used  by the summarizer. The class `Realizer` is a superclass that defines functions shared by both English and French realizer functions. 

```python
class English(Realizer):
    def __init__(self,tense="ps"):
      ...
    best_player_VPs = [...]
    player_VPs = [...]
		def show_winner(self,winner, loser, g_date, g_stadium, g_city) -> str:
      ...
    def show_turning_points(self,winner,loser,overtime,loser_lead_in_first_half,   
                                 loser_lead_in_second_half,always_lead) -> str:
      ...
    def show_team_perf(self,team) -> str: 
      ...
    def show_player_perf(self,team_name, player, vp, show_starter) -> str:
      ...
    def show_next_game(self,date,team_1,is_home,team_2) -> str:
      ...
```

The class variables `best_player_VPs` and `player_VPs` are two arrays of functions returning various verb phrases for the best scorer (e.g., `lead the way posting` or `finished with`) or for indicating the score of a player (e.g., `recorded` or `contributed`).  The summarizer calls one of these functions to vary the ways the performance of each player is indicated.

### 2.4.3 - Summarization functions

The methods returning a string are called by the following `summarize` function having as arguments an instance of a realizer and the information about a given game. It is a direct mapping of the [document planning](#document-planning) as shown by the numbered comments.  This function is *language and realizer independent*. The strings returned by the realizer functions are concatenated into *paragraphs* themselves *joined* by two end-of-lines to build a vanilla formatting. A more sophisticated presentation (e.g., in HTML) could be built, but this is independent of the sentence realization process. If needed `pyrealb` could realize sentences with embedded HTML tags.

```python
    def summarize(realizer, game) -> str:
    # determine winner and loser
    home = game.home()
    visitors = game.visitors()
    if home.line_scores("game").points() > visitors.line_scores("game").points():
        winner, loser = home, visitors
    else:
        winner, loser = visitors, home
    paras = []
    # 1 - give the winner and loser scores with location and date information about the game
    paras.append(realizer.show_winner(winner, loser, game.date(),
                                      game.stadium(), game.city()))
    winner_scores = winner.players_scores()
    loser_scores = loser.players_scores()
    # 2 - check for interesting turning points in the game
    t_points = realizer.show_turning_points(*turning_points(winner, loser))
    if len(t_points) > 0:
        paras.append(t_points)
    # 3 - give information about the best players of both teams
    vps = sample(realizer.best_player_VPs, k=len(realizer.best_player_VPs))
    paras.append(
        realizer.show_player_perf(winner_scores[0],
                                  vps[0], winner_scores[0].starter()) +
        realizer.show_player_perf(loser_scores[0],
                                  vps[1], loser_scores[0].starter())
    )
    # 4 - show interesting statistics for each team and their players
    vps = sample(realizer.player_VPs, k=len(realizer.player_VPs))
    iVP = 0
    for team in [winner, loser]:
        # 4.1 - show global team performance
        team_para = [realizer.show_team_perf(team)]
        # 4.2 - show player performance of the team (in decreasing order of points made)
        first = True  # indicate starter only for the first player
        for player in team.players_scores()[1:]:
            if first:
                starter = player.starter()
                first = False
            if player_has_statistics(player.name()) \
                    and player_has_interesting_statistics(player):
                # show interesting statistics about a given player in a given game
                team_para.append(realizer.show_player_perf(player,
                                                           vps[iVP % len(vps)], starter))
                iVP += 1
            starter = False
        paras.append(" ".join(team_para))
    # 5 - give information about the next games for the winner and the loser if available
    next_games = ""
    next_game_info = next_game(winner)
    if next_game_info is not None:
        next_games += realizer.show_next_game(*next_game_info)
    next_game_info = next_game(loser)
    if next_game_info is not None:
        next_games += realizer.show_next_game(*next_game_info)
    if len(next_games)>0:
        paras.append(next_games)
    return "\n\n".join(paras)
```

We describe the function for conveying the performance of a player. As arguments, it gets a player instance, the verb phrase function to use and whether or not the fact that this player is a starter should be mentioned or not. These choices have already been made by the `summarize` function. 

The sentence starts by giving the name of the player, then if needed, the fact that he is in the starting alignment, followed by *high enough* details about how many minutes he played and how many fields goals, three-pointers, rebounds and assists he achieved. The *height* is determined by the fact that the value is in the first quintile (top 20%) determined by the [Data Interpretation](#data-interpretation) step. Finally, the fact that the player achieved a *double* is shown.  These elements are gathered in an array used by `CP` to build a coordinated phrase which adds the appropriate commas and conjunction depending on the number of facts chosen. This can result in a sentence such as

```
Luc Mbah a Moute ended up with nine points with seven rebounds and three assists.
```

As a further variation, some player information can also be given in a shorter and more telegraphic form such as `(7-11 FG, 1-3 3Pt, 0-1 FT)`

```python
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
```

As the other functions of the realizers follow roughly the same pattern, they are not discussed in this paper. The reader should see the global pattern and can consult the [source code](https://github.com/lapalme/pyrealb/tree/main/demos/basketball) for details.

## 3 - Conclusion

This document has described how `pyrealb` was used for generating French and English basketball summaries from for numerical data. We leave it to the reader to judge the quality of the output. Our goal was to give a complete example of data to text NLG aplication. It is similar in design to the [Weather `pyrealb` demo](../../weather/README.md) which generates French and English weather reports from numerical information. 

## References

- Albert Gatt and Ehud Reiter, 2009. *SimpleNLG: A realisation engine for practical applications*. In Proceedings of the 12th European Workshop on Natural Language Generation (ENLG 2009), pages 90–93, Athens, Greece, March 2009. Association for Computational Linguistics.
- Ehud Reiter. 2007. [An Architecture for Data-to-Text Systems](https://aclanthology.org/W07-2315). In *Proceedings of the Eleventh European Workshop on Natural Language Generation (ENLG 07)*, pages 97–104, Saarbrücken, Germany. DFKI GmbH. *This paper won the [INLG 2022 - Test of Time Award.](https://inlgmeeting.github.io/index.html)*
- Craig Thomson, Ehud Reiter, Barkavi Sundararajan, 2023, [*Evaluating factual accuracy in complex data-to-text*](https://www.sciencedirect.com/science/article/pii/S0885230823000013)), Computer Speech & Language, Volume 80.
- Craig Thomson, Ehud Reiter, and Somayajulu Sripada. 2020. [SportSett:Basketball - A robust and maintainable data-set for Natural Language Generation](https://aclanthology.org/2020.intellang-1.4). In *Proceedings of the Workshop on Intelligent Information Processing and Natural Language Generation*, pages 32–40, Santiago de Compostela, Spain. Association for Computational Linguistics.
- Sam Wiseman, Stuart Shieber, and Alexander Rush. 2017. [Challenges in Data-to-Document Generation](https://aclanthology.org/D17-1239). In *Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing*, pages 2253–2263, Copenhagen, Denmark. Association for Computational Linguistics.