from Games import Games
from Game import Game
from Team import Team
from Player import Player
from random import sample
from Score import Score

games = None
def set_games(g):
    global games
    games = g

# tools to get information about the previous games in the current season

def get_team_info(game:Game, team_name:str)->Team:
    if game.home().name() == team_name:
        return game.home()
    elif game.visitors().name() == team_name:
        return game.visitors()
    else: # should never happen...
        print(f"*** Error: game {game.game_id()}: team_name {team_name} not found.")
        print(f"It was instead: home:{game.home().name()} visitors:{game.visitors().name()}" )
        return None

# return all previous games in the season of a given team
def team_in_previous_games(game_id, team_name)->[Team]:
    teams = []
    while game_id != "null":
        team_info = get_team_info(games[game_id], team_name)
        teams.append(team_info)
        game_id = team_info.previous_game_id()
    return teams

def season_team_scores(game_id, team_name):
    return [team.period_scores["game"]
            for team in team_in_previous_games(game_id, team_name)]

def is_season_high_player(player,code,val) -> bool:
    scores = season_player_scores(player.this_game.game_id(),player.team_name,player.name())
    if len(scores) < 10 : return False # do not consider when there too few games in the season
    return val == max(score.allScores()[code] for score in scores)

def season_players(game_id,team_name,player_name) -> [Player]:
    return list(filter(lambda e: e is not None,
                       (team.get_player(player_name) for team in team_in_previous_games(game_id, team_name))))

def season_player_scores(game_id,team_name,player_name) -> [Score]:
    return [player.scores for player in season_players(game_id,team_name,player_name)]

# check for double_streak for a given player from a team
def n_double_streak(game_id,team_name,player_name) -> (int,int):
    # check if double for current game is "none" and exit immediately if is the case
    player = get_team_info(games[game_id],team_name).get_player(player_name)
    if player is None: return ()
    double = player.double()
    if double == "none": return ()
    count = 1
    for player in season_players(game_id,team_name,player_name)[1:]:
        doubleN = player.double()
        if doubleN != double: break
        count += 1
    return (double,count)

# get all double streaks of a team
def n_double_streaks(game_id,team_name)->[(str,int,int)]:
    # sort streak descending by first type of streak and then length of streak
    def sort_streak(res)-> [(str,int,int)]:
        return sorted(sorted(res, key=lambda e: e[2], reverse=True),
                      key=lambda e: {"double":2,"triple":3,"quadruple":4}[e[1]], reverse=True)
    player_names= get_team_info(games[game_id],team_name).player_names()
    res = []
    for player_name in player_names:
        dbl_streak = n_double_streak(game_id,team_name,player_name)
        if len(dbl_streak)>0:
            res.append((player_name,dbl_streak[0],dbl_streak[1]))
    return sort_streak(res)

# find length winning streak for a team
def winning_streak(game_id,team_name):
    n = 0
    for team in team_in_previous_games(game_id, team_name):
        if team.this_game.winner().name() != team_name:
            break
        n += 1
    return n

#  script made to explore the data and ensure that previous_game and next_game id
#  allowed to recreate the list of games played by a team over a season
#  this is important in order to make links between games to find "winning streaks"

def get_next(game:Game, team_name:str)->str:
    return get_team_info(game, team_name).next_game_id()

def get_previous(game:Game, team_name:str)->str:
    return get_team_info(game, team_name).previous_game_id()

def game_info(game:Game, team_name:str):
    info = get_team_info(game, team_name)
    return (f"{game.show_title():90}" 
            f" ↑:{info.previous_game_id():>5} ↓:{info.next_game_id():>5}")

#  useful for data exploration and checking but not needed for generation
def print_season(game_id:str, team_name:str, displayed:set[str]):
    # follow previous links to find first game of this season
    lastGid = gid = game_id
    while gid != "null":
        if gid not in games:
            print(f"*** {gid} not found in previous")  # should never happen...
            break
        lastGid = gid
        gid = get_previous(games[gid], team_name)
    gid = lastGid
    while gid != "null":
        if gid not in games:
            print(f"*** {gid} not found in next")  # should never happen...
            break
        print(game_info(games[gid], team_name))
        displayed.add(gid)
        gid = get_next(games[gid], team_name)
    print("---")

def print_seasons(team_name:str):
    displayed = set([])  # useful for displaying each season in a dataset
    for gid in games.keys():      # search for the first game of this team not yet displayed
        if gid not in displayed:
            game = games[gid]
            if game.home().name() == team_name:
                print("Games for", get_team_info(game, team_name).place(), team_name)
                print_season(gid, team_name, displayed)
    print("="*25)


def print_season_team_scores(game_id,team_name):
    print(team_name, game_id, games[game_id].show_title())
    print(Score.score_top_line())
    for score in  season_team_scores(game_id, team_name):
        print(score.show())


def print_player_season(game_id,team_name,player_name):
    print(team_name,player_name,games[game_id].show_title())
    print(Player.player_top_line())
    for score in season_player_scores(game_id,team_name,player_name):
        print(score.show())

def print_n_double_streaks(k=10,max=-1):
    n=0
    for s in sample(sorted(games),k=k):
        game = games[s]
        print(game.show_title())
        for team_name in  [game.home().name(),game.visitors().name()]:
            streak = n_double_streaks(s,team_name)
            if len(streak)>0:
                print(" "*6,team_name,streak)
        n += 1
        if n==max: break


if __name__ == "__main__":
    games = Games("train")
    # from stats import allTeams
    # for team in allTeams():
    #     print_seasons(team)
    # ## some tests
    print_season_team_scores("313","Hawks")
    print_player_season("947","76ers","Tony Wroten")
    gid = "313"
    print(gid,games[gid].home().name())
    double_streak= n_double_streaks(gid,games[gid].home().name())
    print(gid,double_streak)
    print(games[gid].show())
    print_n_double_streaks(k=100)

