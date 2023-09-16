# Basketball game summarization

This demo features a rule-based data-to-text Natural Language Generation (NLG) for generating English and French *statistic-focused summaries of basketball games* using information found in the [SportSett:Basketball](https://gem-benchmark.com/data_cards/sportsett_basketball) dataset.

[More details can be found in this document](docs/SportSettSum.md)

## File organization

- `BasketballSummarizer.py` : abstract class for a basketball summarizer
- `English.py` : English realizer class
- `French.py` : French realizer class
- `FStrings.py` : Realizer using only Python string concatenation
- `Game.py` : Class for storing information about a game
- `game_stats.py` : functions for finding interesting facts between teams in a given game
- `Games.py` : Class for hiding access to the Gem dataset
- `global_stats.py` : computation and use of statistics about teams and players computed over the train dataset; 
  when launched as main, it creates the `data/aggregate.json` file
- `LexicalChoices.py` : abstract class for a realizer
- `Player.py` : Class for storing information about a player
- `Realizer.py` : Class with functions shared by English.py and French.py
- `Score.py` : Class for keeping numeric scores (for both Team line-scores and Play box-scores) 
- `seasons_stats.py` : functions for querying information in past game of the current season 
- `sportsettsum.py` : summarizer (this is the main program)
- `Team.py` : Class for storing information about a team
- `data`/
  - `nba-cities-names.json` : names of the NBA teams with the corresponding cities as nouns in the format 
    appropriate to be added to the basic lexicon of each realizer. This is especially useful for French for proper 
    number agreement and for realizing adequate elision.
  - `Seasons-train.txt` : listing of the all games for a given team in each season in the *train* split
  - `train-aggregate.json`: aggregated data about teams and players
- `docs`/
  - `Game_Class_Structure.txt` : global organisation of the main classes for information
  - `SportSett-GEM.md` : reminder of basketball terms and tricks for using the data
  - `SportSettSum.md`: paper about the rationale and organization of the whole realizer system

- `output`/
  - `test`, `train` and `validation`: directories with a sample of generated summaries from the given corpus. These 
    directories are created by running `sportsettsum.py` as main.


**Contact**: [Guy Lapalme](mailto:lapalme@iro.umontreal.ca)



