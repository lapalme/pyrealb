# Basketball game summarization

This demo features a rule-based data-to-text Natural Language Generation (NLG) for generating English and French *statistic-focused summaries of basketball games* using information found in the [SportSett:Basketball](https://gem-benchmark.com/data_cards/sportsett_basketball) dataset.

[More details can be found in this document](docs/SportSettSum.md)

## File organization

- `English.py` : English realizer class
- `French.py` : French realizer class
- `Fstrings.py` : Realizer using only Python string concatenation
- `Game.py` : Class for storing information about a game
- `Games.py` : Class for hiding access to the Gem dataset
- `Player.py` : Class for storing information about a player
- `Realizer.py` : Class with functions shared by English.py and French.py
- `sportsettsum.py` : summarizer (this is the main program)
- `stats.py` : computation and use of statistics about teams and players; when launched as main, it creates the data/aggregate.json file
- `Team.py` : Class for storing information about a team
- `data`/
  - `train-aggregate.json`: aggregated data about teams and players
- `docs`/
  - `Game_Class_Structure.txt` : global organisation of the main classes for information
  - `SportSett-GEM.md` : reminder of basketball terms and tricks for using the data
  - `SportSettSum.md`: paper about the rationale and organization of the whole realizer system
  

#### Contact: [Guy Lapalme](mailto:lapalme@iro.umontreal.ca)



