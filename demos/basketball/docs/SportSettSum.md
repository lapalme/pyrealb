# Summarizing Basketball Games

[Guy Lapalme](mailto:lapalme@iro.umontreal.ca), Université de Montréal, September 2023

This paper describes ***SportSettSum***, a rule-based data-to-text Natural Language Generation (NLG) for generating English and French *statistic-focused summaries of basketball games* using information found in the [SportSett:Basketball](https://gem-benchmark.com/data_cards/sportsett_basketball) dataset (Thomson *et al*.,2020). This dataset combines scores and performance measures about the teams and the players of thousands of NBA games with human-authored summaries about these games. This dataset is a *clean-up* and redesign of the Rotowire (Wiseman et al. 2017) dataset which had been used to develop Seq2Seq models for generating paragraph-sized texts.  

*SportSett:Basketball* has been used in experiments about the evaluation of factual accuracy in automatically generated texts (Thomson *et al.*, 2023) and in an [Accuracy Evaluation shared task](https://aclanthology.org/2021.inlg-1.23.pdf), but we could not find any documented use of this dataset by an NLG (neural or not) system to produce complete summaries. This seems surprising given the recent surge of interest in NLG based on GPT-*n* systems, probably because most of these struggle not to *hallucinate* when given verifiable data. This means that NLG evaluation based on BLEU or other automatic metrics cannot be relied upon anymore and is thus much more time consuming and probably more complicated than developing the systems themselves.

Our goal here is not to develop an industrial system or to *beat* any GPT look-alike, but to display a use case  of the [pyrealb bilingual text realizer](https://github.com/lapalme/pyrealb) for creating French and English documents from statistical data. The system is developed in Python and its source code is available in this GitHub directory. The human-authored summaries in *SportSett:Basketball* were used as an English corpus for developing appropriate phrasings.  

*Warning*: we are not a basketball expert, not even a fan.  At the start of this project, we had to develop a [personal lexicon of the main terms](SportSett-GEM.md) such as field *goals*, *turnovers*, *rebounds*, *steals*, *blocks*, etc. by searching the internet. We had never read a basketball game summary before.  So seasoned basketball fans will surely find quite naive our analysis of the games and players. This warning applies even more to French for which we do not even have any reference summary. We read some texts on the French [Basket USA](https://www.basketusa.com/news/) web site to find some inspiration, although the site is more about new about the teams than game summaries.

But this is not the main point of this exercise whose takeaway lesson is the process of going from data to the text by roughly following the steps of the *now classical* architecture proposed by Reiter (2007): 

- **Signal analysis**: analyzing input data looking for patterns
- **Data interpretation**:  identifying domain-specific messages from patterns and causal relations between messages
- **Document planning**: deciding which messages to mention and rhetorical structure in the generated text.
- **Realization**: creating the actual text

## Description of the input data

Before describing the system, we  give an overview of the input data, the specifics of which can be found in the source code. 

The [SportSett:Basketball](https://gem-benchmark.com/data_cards/sportsett_basketball) dataset (Thomson *et al*.,2020) is a relational database about NBA games between 2014 and 2018 which allows very detailed queries. In our experiments, we restricted ourselves to the *JSON* version available in [GEMv2](https://aclanthology.org/2022.emnlp-demos.27/) as a *[Hugging Face dataset](https://gem-benchmark.com/data_cards/sportsett_basketball)* with three splits:

| Split      |   NBA seasons    | Games |
| ---------- | :--------------: | ----: |
| Train      | 2014, 2015, 2016 |  3690 |
| Validation |       2017       |  1230 |
| Test       |       2018       |  1230 |

Each game is described by global information such as the date, the stadium and the city where the game was played. Each team (*home* and *visitors*) is described by its name, its city, its current conference standing and quite detailed information about the scores: 

- *line-scores* of the teams  for each quarter, half and complete game; 
- *box-scores* for each player

Finally, there is a link to the following game of each team.  There are also one or two human-written summaries per game.

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

The human written summary associated with this game (237 words) is the following in which we have underlined contextual information that cannot be found from a statistical analysis of the provided data (96 words, about 40%).  Note the typo in *Tornoto*, suggesting that this summary was surely written by  a human!

> The Miami Heat (20) defeated the Philadelphia 76ers (0 - 3) 114 - 96 on Saturday. Chris Bosh scored a game - high 30 points to go with eight rebounds in 33 minutes. <u>Josh McRoberts made his Heat debut after missing the entire preseason recovering from toe surgery.</u> McRoberts came off the bench and played 11 minutes. <u>Shawne Williams was once again the starter at power forward in McRoberts' stead.</u> Williams finished with 15 points and three three - pointers in 29 minutes. Mario Chalmers scored 18 points in 25 minutes off the bench. <u>Luc Richard Mbah a Moute replaced Chris Johnson in the starting lineup for the Sixers on Saturday. Hollis Thompson shifted down to the starting shooting guard job to make room for Mbah a Moute.</u> Mbah a Moute finished with nine points and seven rebounds in 19 minutes. K.J. McDaniels, <u>who suffered a minor hip flexor injury in Friday's game, was available and</u> played 21 minutes off the bench, finishing with eight points and three blocks. <u>Michael Carter-Williams is expected to be out until Nov. 13, but Tony Wroten continues to put up impressive numbers in Carter-Williams' absence.</u> Wroten finished with a double - double of 21 points and 10 assists in 33 minutes. The Heat will complete a back - to - back set at home Sunday against the <u>Tornoto</u> Raptors. The Sixers' next game is at home Monday against the Houston Rockets.

### *Mundane* but important details

Data is often *tricky* even in well-organized directories such as the GEMv2. In this case, all the data is  represented as strings, including integers, Booleans and even `null` even though JSON can/should store these data types as such. We determined that the JSON file would be 10% smaller if appropriate types would have been used. So care must be taken when making computation, sorting or testing. We also discovered that the derived data for half-time of the games from the values of quarters had been computed by string concatenation of string values instead of the addition of the numeric values, curtesy of the overloading of the plus sign in  JavaScript or Python. There were also errors in the values of the total minutes of play which were always shown as "4" instead of 240 for a regular game (5 players that are on the field for four quarters of 12 minutes).

Over the course of this project, we read samples of summaries to get an idea of the phrasings and choices of information to convey. But we also noticed that over the years, the style of the summaries seemed to change probably because the authors or the editors decided to focus on different aspects of the games even though the global text plan remained similar.  In 2014, as shown in the previous example, there were quite a lot of *outside* player information such as injuries, contract or personal problems, etc. In 2018, most game summaries included highlights of significant team performance quarter by quarter.  We would expect that an automatic text generator might be able to learn how to adapt to this change of style.  But it must be remembered that the way the SportSett corpus has been split is by years: earlier years are for training and later years are for validation and test. This splitting reflects the fact that, in production, a text generator will generate new text based on what the system has learned previously.  Unfortunately in this case, as the texts in the test split can relatively different from the ones in the training and validation splits, it might be hard for any learning system to create new texts similar to the ones in the test and thus get good scores...

Although the data is available as a [Hugging Face dataset](https://huggingface.co/docs/datasets/index), currently we do not use any of the interesting properties for accessing efficiently columnar data, we load the whole dataset once and process it like an array (`list` in Python) of JSON structures. The numeric values are converted to `int`s and corrected when the data set is loaded.

We have `def`ined Python classes (`Games`, `Game`, `Team`,  `Player` and  `Score`) with methods to access the JSON fields with more informative names than abbreviations and three letter keys. Should we eventually want to use the database instead of the JSON as data source, we could (hopefully!) keep the same interface.  Some fields appearing in the JSON are not *exported*, because they seemed redundant (e.g., many details about the next game which can be accessed directly by fetching the game information in the data) or computable from other fields (e.g., the percentage of success that can be computed by dividing the number of *made* over the number of *attempted*).

After all these caveats, we can now start transforming the data into text. As illustrated above, and confirmed by reading other summaries, the texts mostly follow the usual pyramidal structure of newspaper articles. First, they describe the global result before giving information about each team and then about the players that have a *high* scores. Mentions are often added when the a team or player performance in this game is much better than the season average or if a team is in a *long winning streak*. Finally, there is an indication of when and where will be played the next game for each team. 

Of course, it cannot be expected to mention contextual information about the health condition of the players or some contract agreements as such information does not appear in the input data. They will not be *hallucinated* by our system.

#### Examples of output

For the *impatient*, here is one English summary produced by ***SportSettSum*** from the data described in the above example:

> The Heat  (2-0) , leader in their conference, dominated the 76ers  (0-3) 114-96 in
> Philadelphia at the Wells Fargo Center on Saturday.
>
> The Heat led in all four quarters. During the first quarter, the 76ers obtained better
> goals percentage a difference of 14%. The 76ers overcame the Heat for rebounds by 8 in the
> first half. In the third quarter, the 76ers got better free throws percentage a difference
> of 21%. The Heat dominated the 76ers for points 27 to 13 over the fourth quarter. During
> the game, the Heat obtained better three-pointers percentage an advantage of 20%.
>
> Chris Bosh who started this game led the way off the bench scoring 30 points with four
> assists. Tony Wroten who was in the starting line-up had an efficient performance scoring
> 21 points  (6-11 FG, 1-4 3Pt, 8-11 FT) and ten assists and performed a double-double.
>
> The Heat showed 49 percent from the field and 20-29 free throws.  Mario Chalmers who was a
> starter added 20 points.  Luol Deng had 15 points with 7-for-11 FG.  Shawne Williams
> scored 15 points with 5-of-9 FG and four assists.  Dwyane Wade had nine points with ten
> assists.
>
> The 76ers showed 52 percent from the field and 19-26 free throws and committed 24
> turnovers.  Brandon Davies who started this game added 18 points with 7-of-9 FG.  Luc Mbah
> a Moute added nine points with seven rebounds and three assists.  Malcolm Thomas finished
> with eight points in 19 minutes with nine rebounds grabbed.  Alexey Shved scored six
> points with six assists.
>
> For their next game, the Heat will receive the Toronto Raptors on Sunday. On deck for the
> 76ers will be a home match versus Houston.

***SportSettSum*** can also generate a French summary such as the following. Because of the randomization between the phrasing choices, the French version is not a literal translation of the English, but it conveys the same information. Both realizers work from the same original data and use the same algorithm for selecting the information to convey.

> Le Heat  (2-0) , meneurs dans leur conférence, a surpassé les 76ers  (0-3) 114-96 samedi à
> Philadelphia au stade Wells Fargo Center.
>
> Le Heat a mené pendant les quatre quarts. Durant le premier quart, les 76ers ont obtenu les
> meilleurs tirs en pourcentage, un avantage de 14%. Les 76ers ont vaincu le Heat pour les
> rebonds par 8 durant la première demie. Durant le troisième quart, les 76ers ont réussi
> les meilleurs lancers francs en pourcentage, 83% par rapport à 62%. Le Heat a dominé les
> 76ers pour les points 27 à 13 pendant le quatrième quart. Durant la partie, le Heat a
> réussi les meilleurs tirs à 3 points en pourcentage, 50% par rapport à 30%.
>
> Chris Bosh qui était un partant a fini avec 30 points avec quatre passes décisives. Tony
> Wroten qui était un partant a mené son équipe marquant 21 points  (6-11 L, 1-4 L3, 8-11
> LF) tout en ajoutant dix passes décisives et a terminé avec un double-double.
>
> Le Heat a compté 49 pour cent de tirs réussis et 20 lancers francs sur 29.  Mario Chalmers
> qui était un partant a ajouté 20 points avec 6-sur-9 L.  Luol Deng a enregistré 15 points.
> Shawne Williams a marqué 15 points  (5-9 L, 3-5 L3, 2-2 LF) et quatre passes décisives.
> Dwyane Wade a contribué un efficace neuf points avec dix passes décisives.
>
> Les 76ers ont compté 52 pour cent de tirs réussis et 19 lancers francs sur 26 et ont subi
> 24 pertes de ballon.  Brandon Davies qui était un partant a ajouté 18 points.  Luc Mbah a
> Moute a terminé avec neuf points avec sept rebonds récupérés et trois passes décisives.
> Malcolm Thomas a terminé avec huit points en 19 minutes avec neuf rebonds récupérés.
> Alexey Shved a contribué un efficace six points avec six passes décisives.
>
> Le prochain match du Heat sera à domicile contre les Raptors de Toronto dimanche. À venir
> pour les 76ers, un match à domicile contre Houston.

 [Sample of generated summaries with the corresponding data and reference summaries](../output)

## Architecture of the generation process

We now describe the steps going from the input data to the final text following the steps identified by Reiter. 

### Signal analysis

This first step looks for patterns in the data to convey in the summary.  Human summaries start by naming the winner and loser teams with their scores, followed by the team performance over each quarter. The best players' performances are then given. Finally, information is given about the next games for both teams.

The game results and the information about the next game can be found directly in the JSON, as is the performance of the players who, in each team, scored the most points. The *line-scores*  describe the results for each quarter. But determining which player should be mentioned next with what appropriate information needs more work. It would be useless, and boring, to list the performances of each player, given that this information is available in the table which could be displayed or made available on request. There are also mentions of interesting season's performances.

### Data interpretation

#### *Intra-game* data

To determine the turning points and the relative performance of each team over a game, we compare the line-scores of each team and determine the largest differences over certain thresholds provided there are enough occurrences to be meaningful. The largest differences are considered more important and a single score is kept for each period (quarter, half or game). These performances are then sorted by period to appear in chronological order.

#### *Inter-game* data

In order to focus on the most significant aspects of players performance, we decided to preprocess the training corpus to aggregate the scores of each player in all games in which he played more than one minute, ignoring the team. The summary will mention a player if he has a *high* number of field goals, three-pointers, rebounds or assists. Currently *high* is defined as being in the first quintile (best 20%) of all his scores.

Similarly, for each team,  points for all games in which it took part are aggregated. This information is used for choosing the aspects worth mentioning when talking about a team using the same criterion. 

As the statistics are only computed on the training corpus (season 2014-2016), they are not available for a few good *rookies* (e.g. Bogdan Bogdanović who arrived in 2018) when the summarizer is run on the validation or the test corpora which cover the 2017 and 2018 seasons. The realizer will still mention them if they are the best scorer in a given game. 

As each game of a team is linked to the previous game of the same within a season, we defined functions to compute statistics such as average performance or the number of consecutive victories (winning streaks) within a season. 

Given the fact, that the training and validation corpora span the years 2014-2017, it would be concievable to compute multi-year statistics and use these when generating summaries for the 2018 games (test corpus). But currently, we only take into account the previous games of the current season

### Document planning

The pseudo-code for the summarizing a `game` is the following (paragraphs numbers will be used later for reference):

```
1. Give the winner and loser scores with location and date information about the game 
   and mention winning streak if it long enough
2. Check for turning points and interesting facts
3. Give information about the best players of both teams
4. For each  team in [winner,loser]
		4.1 Show global team performance
		4.2 For each player of the team (in decreasing order of points scored)  
					if player has any high score
						give information about this player
5. give information about the next games for the winner and the loser
```

### Realization

The realization step uses a symbolic and rule-based  approach  implemented by means of  Python 3 classes using the package `pyrealb` for NLG.  The realizer will be described [below](#realizer-organization), but we first recall the essentials of `pyrealb`. 

## The `pyrealb` bilingual realizer package

[`pyrealb`](https://github.com/lapalme/pyrealb) is a Python port of [jsRealB](https://arxiv.org/pdf/2012.15425.pdf) which was strongly influenced by SimpleNLG (Gatt & Reiter, 2009) in which realization is achieved by programming language instructions that create data structures corresponding to the elements of the sentence to be realized. Once the data structure is built, it is traversed to produce a string.

Like SimpleNLG, `pyrealb` has the following components:

- *morphological rules* to determine the appropriate word forms, such as plurals and conjugations;
- a *lexicon* defining the word category, gender, number, declension and conjugation rule number and other features needed to produce the final token;
- *syntactic rules* to properly order words in a sentence, perform agreement between constituents and carry out other interactions.

`pyrealb` has these components for both French and English with other *goodies*, such as the spelling out of numbers and the wording of temporal expressions that are especially useful in data to text applications. 

`pyrealb` accepts either a *Constituent* or a *Dependent* notation for building sentences. For ***SportSettSum***, we use the *Constituent* notation. The data structure is built by class constuctor calls whose names are similar to the symbols typically used for constituent syntax trees:

- **Terminal**: `N` (noun), `V` (verb), `A` (adjective), `D` (determiner), `Pro` (pronoun), Adv (adverb), `P` (preposition), `C` (conjunction), `NO` (number), `DT` (date), `Q` (quoted/canned text). A terminal is created with a single parameter, most often a string, its lemma.
- **Phrase** for combining its parameters, i.e. terminals and other phrases: `S` (Sentence), `SP` (Subordinate Phrase), `NP` (Noun Phrase), `VP` (Verb Phrase), `AP` (Adjective Phrase), `CP` (Coordinate Phrase), `PP` (Prepositional Phrase), `AdvP` (Adverbial Phrase).

Features are added to these structures using the dot notation to modify their properties. For terminals, their person, number, gender can be specified. For phrases, the sentence may be negated or set to a passive mode; a noun phrase can be pronominalized. Punctuation signs and HTML tags can also be added.

The main advantage of using a Python-based notation is the fact that programming constructs can be used to incrementally build a structure before being realized. The following example illustrates some of these capabilities in a small program to create parts of structures. 

```python
quality = oneOf(A("strong"),A("skilled"),A("talented")) # choose a quality
player  = NP(D("the"),N("player"),quality)   # combine player and quality
score   = VP(V(oneOf("score","win")))        # select a verb
score.add(NP(NO(25),N("point")))             # add object to the verb
```

The `oneOf` function, returning one of its arguments chosen at random, allows for varying between synonyms or similar formulations. The `add` method is used to incrementally build the structure that can then be realized as a string using the `realize` method.   For example, one result of the evaluation of 

```python
S(player,score).t("ps").realize()
```

can be  *The talented player scored 25 points.* Note that the past tense is applied to the whole structure before realization. Other types of modifications can also be done on the original structure. The following example shows a case of negative passive sentence at the future tense. *25 points will not be won by the strong player.*

```python
S(player,score).t("f").typ({"neg":True, "pas":True}).realize()
```

Functions can also be defined for creating recurrent patterns such as the following which, given a `Team` instance, will generate a structure that will be realized as either *the Heat* or *the Miami Heat* if the second parameter is `True`. 

```python
def team_np(self, team, with_place=False):
    return NP(D("the"),
              N(team.place()) if with_place else None,
              N(team.name())).n("p")
```

## Realizer organization

The following shows the methods that our *basketball realizer* implements, they correspond to the steps identified in [document planning](#document-planning). Checking that a realizer implements these methods is performed by means of the [abc - Abstract Base Classes](https://docs.python.org/3/library/abc.html) Python package (shown here without the `@abc.abstractmethod` annotations. 

```python
import abc
class BasketballSummarizer(abc.ABC):
    def show_winner(self, winner, loser, g_date, g_stadium, g_city,
                    winning_streak_length) -> str: pass    
    def show_turning_points(self, winner, loser, overtime, 
                            loser_lead_in_first_half,
                            loser_lead_in_second_half, always_lead) -> str: pass
    def show_team_perf(self, team) -> str:pass
    def show_team_facts(self, winner, loser, interesting) -> str: pass
    def show_player_perf(self, team_name, player, vp_func, show_starter) -> str: pass
    def show_next_game(self, date, team_1, is_home, team_2) -> str: pass
```

All these methods return strings to be called by the following `summarize` function with two parameters: the first, `realizer` is an instance of a subclass of `BasketSummarizer`  implementing these six methods; the second parameter `game` gives access to the data about this game . 

The code of `summarize` is a  *language and realizer independent* direct mapping of the [document planning](#document-planning) as shown by the numbered comments.  The strings returned by the realizer functions are concatenated into *paragraphs* themselves *joined* by two end-of-lines as a vanilla formatting. A more sophisticated presentation (e.g., in HTML) could be built, but this is independent of the sentence realization process. If needed `pyrealb` could also realize sentences with embedded HTML tags.

```python
def summarize(realizer, game) -> str:
    # determine winner and loser
    home = game.home()
    visitors = game.visitors()
    if game.winner() == home:
        winner, loser = home, visitors
    else:
        winner, loser = visitors, home

    paras = []
    # 1 - give the winner and loser scores with location and date of the game
    winning_streak_length = winning_streak(game.game_id(), winner.name())
    paras.append(realizer.show_winner(winner, loser, game.date(),
                                      game.stadium(), game.city(),
                                      winning_streak_length))
    losing_streak_length = losing_streak(game.game_id(), winner.name())
    if losing_streak_length > 3:
        paras.append(realizer.team_losing_streak_vp(loser, losing_streak_length))

    # 2 - check for turning points and interesting facts during the game
    game_para = []
    t_points = realizer.show_turning_points(*turning_points(winner, loser))
    if len(t_points) > 0:
        game_para.append(t_points)
    interesting = interesting_stats(winner.period_scores, loser.period_scores)
    int_facts = realizer.show_team_facts(winner, loser, interesting)
    game_para.extend(int_facts)
    if len(game_para) > 0:
        paras.append("".join(game_para))

    # 3 - give information about the best players of both teams
    winner_players = winner.players_sorted()
    loser_players = loser.players_sorted()
    paras.append(
        realizer.show_player_perf(winner_players[0],
                                  realizer.best_player_VP,
                                  winner_players[0].starter()) +
        realizer.show_player_perf(loser_players[0],
                                  realizer.best_player_VP,
                                  loser_players[0].starter())
    )

    # 4 - show interesting statistics for each team and their players
    for team in [winner, loser]:
        # 4.1 - show global team performance
        team_para = [realizer.show_team_perf(team)]
        # 4.2 - show player performance of the team in decreasing order of points
        # statistics for the best player have given above, so we start at index 1
        players = team.players_sorted()
        if player_has_statistics(players[1].name()) \
                and player_has_interesting_statistics(players[1]):
            # indicate starter only for the second-best player
            team_para.append(
                realizer.show_player_perf(players[1],
                                      realizer.player_VP, players[1].starter()))
        for player in players[2:]:
            if player_has_statistics(player.name()) \
                    and player_has_interesting_statistics(player):
                team_para.append(
                    realizer.show_player_perf(player, realizer.player_VP, False))
        paras.append(" ".join(team_para))

    # 5 - give information about the next games for the winner and the loser
    next_games = ""
    next_game_info = next_game(winner)
    if next_game_info is not None:
        next_games += realizer.show_next_game(*next_game_info)
    next_game_info = next_game(loser)
    if next_game_info is not None:
        next_games += realizer.show_next_game(*next_game_info)
    if len(next_games) > 0:
        paras.append(next_games)
    return "\n\n".join("\n".join(wrap(para, width=paragraph_width)) for para in paras)
```

### `BasketballSummarizer` implementations

Two subclasses implement the `BasketballSummarizer` interface:

- `FStrings`: an English realizer using only Python string concatenations (often *f-strings* hence the name of the class) that can be seen as a baseline. It will not be further described here but you can look at its  [source code](../FStrings.py).

- `Realizer` : a language independent `pyrealb` `Constituent` *sentence organizer* calling methods of two subclasses `English` and `French` to build `Constituent` structures that are then realized into strings. These subclasses must implement the methods that defined in the  [`LexicalChoices` abstract class](../LexicalChoices.py) . The global organization for the `pyrealb` realizers is thus as follows:

  ```python
  class Realizer(BasketballSummarizer):
    ...
  class English(Realizer,LexicalChoices):
    ...
  class French(Realizer,LexicalChoices):
    ...
  ```

`Realizer`  defines the sentence organization using high level `Phrase`s (e.g. sentences, subordinates, coordinates, etc) while the `Terminal`s and lower level `Phrase`s (e.g. `NP`, `VP`, etc.) are defined either in the subclasses `English` and `French`.

Here a are two examples of functions in the  [English](../English.py) class: the first to realize *who started this game* or *who was in the starting line-up* for the first function, the verb tense is determined in the calling function (see line 8 of the `show_player_perf` below ; the second for realizing *a season high*.

```python
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
```

The function with the same name in the  [French](../French.py)  class realizes *débutait la partie* or *figurait dans l'alignement de départ*. The second function realizes *un record pour la saison*.

```python
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
        NP(D("mon"),A("bon").f("co"),N("score"))
    )
    return np.add(
        oneOf(
            PP(P("pour"),NP(D("le"), N("saison"))),
            PP(P("jusque"),Adv("ici"))
        )
    )
```

So we see that there is a clear separation between the word choice and the organization within a sentence which is the job of the  [Realizer](../Realizer.py)  class. This clear separation ensures that the sentence organization is the same between both English and French sentences. 

As an example of a method in `Realizer`, we describe how the performance of a player is realized. It has three parameters:

- a player instance giving access to the data about this player
- a verb phrase function to choose an appropriate verb depending on whether this player was the best in this game or not.  These choices have already been made by the `summarize` function (lines 23, 26, 41 and 47). 
- The last parameter indicates if this player a was on the field at the start of the game. 

Calls are made to subclass functions to return `Constituent` structures as required by the `LexicalChoices` abstract class, such as the functions: `starter_player()` (line 7) or `season_high()` (line 11) whose code was given above.

```python
def show_player_perf(self, player,vp_func,show_starter) -> str:
    # player [starter] vp [points] [details]
    # show global information
    name = player.name()
    vp_st = None
    if show_starter:
        vp_st = self.starter_player()
    vp = vp_func().t(self.t())
    np_pts = self.nb(player.scores.points(), "point")
    if is_season_high_player(player, "PTS", player.scores.points()):
        np_pts.add(self.season_high())
    vp.add(np_pts)
    s = S(Q(name), vp_st, vp)
    minutes = player.scores.minutes()
    if is_high("players", name, "MIN", minutes):
        s.add(self.nb_minutes_played(minutes))
    # show details in either long form or only as a list of numbers
    details = []
    details.append(oneOf(
        lambda: self.show_points(player),
        lambda: self.show_points_details(player)
    ))
    double = player.double()
    if double != "none":
        details.append(self.doubles(double))
    return s.add(self.conjunction(details)).realize()
```

The sentence starts by giving the name of the player (line 4), then if needed, the fact that he is in the starting alignment (line 6), followed by *high enough* details about how many minutes he played and how many fields goals, three-pointers, rebounds and assists he achieved (line 10). The *height* is determined by the fact that the value is in the first quintile (top 20%) determined by the [Data Interpretation](#data-interpretation) step. Finally, the fact that the player achieved a *double* is shown (line 23).  These elements are gathered in an array used by `conjunction` to build a coordinated phrase which adds the appropriate commas and conjunction depending on the number of facts chosen. This can result in an English sentence such as

```
Luc Mbah a Moute ended up with nine points with seven rebounds and three assists.
```

or in a French sentence such as

```
Luc Mbah a terminé avec neuf points avec sept rebonds et trois passes décisives.
```

As a further variation, some player information can also be given in a shorter and more telegraphic form such as `(7-11 FG, 1-3 3Pt, 0-1 FT)`. As the other functions of the realizers follow roughly the same pattern, they are not discussed in this paper. The reader should see the global pattern and can consult the full [source code](https://github.com/lapalme/pyrealb/tree/main/demos/basketball) for details.

## Conclusion

This document has described how `pyrealb` was used for generating French and English basketball summaries from numerical data. We leave it to the reader to judge the quality of the output.  [Other examples of data with the output of our three realizers with the reference summary can be seen here](../output). Our goal was to give a complete example of data-to-text NLG application. It is similar in design to the [Weather `pyrealb` demo](../../weather/README.md) which generates French and English weather reports from numerical information. 

## Acknowledgment

We want to thank Craig Thomson and Fabrizio Gotti for their insights and suggestions about a previous version of this document.

## References

- Albert Gatt and Ehud Reiter, 2009. *SimpleNLG: A realisation engine for practical applications*. In Proceedings of the 12th European Workshop on Natural Language Generation (ENLG 2009), pages 90–93, Athens, Greece, March 2009. Association for Computational Linguistics.
- Ehud Reiter. 2007. [An Architecture for Data-to-Text Systems](https://aclanthology.org/W07-2315). In *Proceedings of the Eleventh European Workshop on Natural Language Generation (ENLG 07)*, pages 97–104, Saarbrücken, Germany. DFKI GmbH. *This paper won the [INLG 2022 - Test of Time Award.](https://inlgmeeting.github.io/index.html)*
- Craig Thomson, Ehud Reiter, Barkavi Sundararajan, 2023, [*Evaluating factual accuracy in complex data-to-text*](https://www.sciencedirect.com/science/article/pii/S0885230823000013)), Computer Speech & Language, Volume 80.
- Craig Thomson, Ehud Reiter, and Somayajulu Sripada. 2020. [SportSett:Basketball - A robust and maintainable data-set for Natural Language Generation](https://aclanthology.org/2020.intellang-1.4). In *Proceedings of the Workshop on Intelligent Information Processing and Natural Language Generation*, pages 32–40, Santiago de Compostela, Spain. Association for Computational Linguistics.
- Sam Wiseman, Stuart Shieber, and Alexander Rush. 2017. [Challenges in Data-to-Document Generation](https://aclanthology.org/D17-1239). In *Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing*, pages 2253–2263, Copenhagen, Denmark. Association for Computational Linguistics.