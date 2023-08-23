# Basketball statistics used in the [SportSett GEM dataset](https://gem-benchmark.com/data_cards/sportsett_basketball)

The Data Fields are briefly described in the Dataset Overview section, but the meaning of the numerical scores is not described.

Not being a basketball expert, I wrote this document as an *aide-memoire* of the abbreviations used in the `line_score` fields for a team and `box_score` fields  for each player in the SportSett Gem dataset. Each game being a JSON structure.

**CAUTION**: for *unknown reasons*, values (e.g. numbers and `null`) are represented as strings, but booleans are often represented as booleans but not always... 

Information taken from [Wikipedia](https://en.wikipedia.org/wiki/Basketball_statistics).

French terms given here underlines in parentheses, taken from the [Olympic Summer Sports Glossary (London 2012)](https://web.archive.org/web/20140226152312/http://www.lexique-jo.org/2012/disciplines1.cfm?rub=BASK&the=&lang=)

Tables at [basket-ball-reference.com](https://www.basketball-reference.com/boxscores/201411010PHI.html) give also interesting information.

## `line_score`

Information about the  `game`, first and second half (`H1`,`H2`), each quarter (`Q1`,`Q2`,`Q3`,`Q4`) and overtime (`OT`) which is often all 0. 

**CAUTION**: currently the values for `H1` and `H2` are the *string concatenation* of respectively `Q1` and `Q2` and of `Q3` and `Q4`, so they should not be relied upon for computation.

Information  in the record `rec`about the `game` of the  `home` or `vis`  team with the following access path. 

    rec["teams"]["home"]["line_score"]["game"]

| Field name                    | Full name                         | Description                                                  |
| ----------------------------- | --------------------------------- | ------------------------------------------------------------ |
| `FGA`<br/>`FGM`<br/>`FG_PCT`  | attempted<br/>made<br/>percentage | **F**ield **G**oal worth two points (<u>tir de champ; tir extérieur</u>)<br/>*these counts also include FG3s* |
| `FG3A`<br>`FG3M`<br>`FG3_PCT` | attempted<br>made<br>percentage   | **F**ield **G**oal worth **3** points (<u>tir à trois points</u>)<br/>*As they are already counted in FG, for points there are worth 1 point* |
| `FTA`<br/>`FTM`<br/>`FT_PCT`  | attempted<br/>made<br/>percentage | unopposed attempt to score points by shooting from behind the **F**ree-**T**hrow line (<u>lancer franc</u>) |
| `DREB`<br/>`OREB`<br/>`TREB`  | defensive<br>offensive<br>total   | **REB**ound : awarded to a player who retrieves the ball after a missed field goal or free throw (<u>rebond</u>) |
| `BLK`                         | block                             | occurs when a defensive player legally deflects a field goal attempt from an offensive player to prevent a score (<u>contre</u>) |
| `AST`                         | assist                            | attributed to a player who passes the ball to a teammate in a way that leads directly to a score by field goal (<u>passe décisive</u>) |
| `STL`                         | steal                             | when a defensive player legally causes a turnover by their positive, aggressive action (<u>interception</u>) |
| `TOV`                         | turn-over                         | occurs when a team loses possession of the ball to the opposing team before a player takes a shot at their team's basket. (<u>perte de ballon</u>) |
| `PF`                          | personal foul                     | a breach of the rules that concerns illegal personal contact with an opponent (<u>faute</u>) |
| `PTS`                         | points                            | score in a game (<u>points</u>)                              |
| `MIN`                         | minutes                           | total number of minutes played by all players, usually 60 for a quarter (5 players each 12 minutes) (<u>minutes</u>) |



## `box_score`

List of records for Information about each player of the `home` or `vis` team.

Information  in the record `rec` about for the first player of the `home` team is obtained with the following access path. 

    rec["teams"]["home"]["box_score"][0]

| Field name                    | Full name                         | Description                                                  |
| ----------------------------- | --------------------------------- | ------------------------------------------------------------ |
| `first_name`                  | First name                        |                                                              |
| `last_name`                   | Family name                       |                                                              |
| `name`                        | Full name                         |                                                              |
| `starter`                     | starter?                          | `true` or `false` if present on the field at the start of the game |
| `MIN`                         | minutes                           | number of minutes on the field (*minutes*)                   |
| `FGA`<br/>`FGM`<br/>`FG_PCT`  | attempted<br/>made<br/>percentage | **F**ield **G**oal worth two points (<u>tir de champ; tir extérieur</u>)<br/>*these counts also include FG3s* |
| `FG3A`<br>`FG3M`<br>`FG3_PCT` | attempted<br>made<br>percentage   | **F**ield **G**oal worth **3** points (<u>tir à trois points</u>)<br/>*As they are already counted in FG, for points there are worth 1 point* |
| `FTA`<br/>`FTM`<br/>`FT_PCT`  | attempted<br/>made<br/>percentage | unopposed attempt to score points by shooting from behind the **F**ree-**T**hrow line  (<u>lancer franc</u>) |
| `DREB`<br/>`OREB`<br/>`TREB`  | defensive<br>offensive<br>total   | **REB**ound : awarded to a player who retrieves the ball after a missed field goal or free throw (<u>rebond</u>) |
| `AST`                         | assist                            | attributed to a player who passes the ball to a teammate in a way that leads directly to a score by field goal (<u>passe décisive</u>) |
| `STL`                         | steal                             | when a defensive player legally causes a turnover by their positive, aggressive action (<u>interception</u>) |
| `BLK`                         | block                             | occurs when a defensive player legally deflects a field goal attempt from an offensive player to prevent a score (<u>contre</u>) |
| `TOV`                         | turn-over                         | occurs when a team loses possession of the ball to the opposing team before a player takes a shot at their team's basket (<u>perte de ballon</u>). |
| `PF`                          | personal foul                     | a breach of the rules that concerns illegal personal contact with an opponent (<u>faute</u>) |
| `PTS`                         | points                            | used to keep track of the score in a game (<u>points</u>)    |
| `+/-`                         | plus-minus                        | change in the score when the player is either on or off the court |
| `DOUBLE`                      | kind of double                    | `double` if the player make double digits in a game in any two of the `PTS`, `TREB`, `AST`, `STL` and BLK statistics  `triple` if double digits in three statistics; `none` otherwise (most of the time...) (<u>double</u>) |

## Data file on GEM 

### Reading the training data file in Python 

```python
import datasets
dataset_name = 'GEM/sportsett_basketball'
datasets.load_dataset(dataset_name,split="train")
```

### Structure of each record

```python
{
  "sportsett_id": int,
  "gem_id": str, # name of the data file
  "game": {
      "day": int,
      "month": str,
      "year": int,
      "dayname": str,
      "season": int,
      "stadium": str,
      "capacity": int,
      "attendance": int,
      "city": str,
      "state": str,
      "game_id": int
    },
  "teams": {
      "home": {
          "name": str,
          "place": str,
          "conference": str,
          "division": str,
          "wins": int,
          "losses": int,
          "conference_standing": int,
          "game_number": int,
          "previous_game_id": int,
          "next_game_id": int,
          "line_score": { see above }
          "box_score" : { see above }
          "next_game" : {
            "day": int,
            "month": str,
            "year": int,
            "dayname": str,
            "city": str,
            "stadium": str,
            "opponent_name": str,
            "opponent_place": str,
            "is_home": "True" or "False" # usually bool are indicated as such
          }
       "vis": { same as "home"}
      }
    "references" : [str], # tokenized references
    # the following fields are undocumented
    "references": [str], # original references 
    "target": str,       # seems identical to the first element of references
    "linearized_input": str # looks like the original data with XML-like open tags only    
  }
}
```



## Exploring the data with `jq`

[jq](https://jqlang.github.io/jq/) is very useful for exploring large jsonl files. Its syntax looks a bit *esoteric* at the start, but it is very fast and very convenient. 

Here is a jq expression to show the scores of  Kendrick Perkins, both at home and as visitor,  when he played more than 5 minutes. Each list of scores is displayed on a single line.

```
jq -c '.teams|.home,.vis|.box_score|.[]| select(.name =="Kendrick Perkins" and (.MIN |tonumber)>0)' train.jsonl
```

Conversion tonumber is important because in this specific json file, all numbers are kept as strings...

## Contact

[Guy Lapalme](mailto:lapalme@iro.umontreal,.ca)
