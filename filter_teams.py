import json
import sys

from Team import Team

with open("games.json", "r") as f:
    games = json.load(f)
with open("players.json", "r") as f:
    players = json.load(f)
year_indexes = {}
team_names = []
for game in games:
    if game["year"] not in year_indexes:
        year_indexes[game["year"]] = games.index(game)
for year in range(len(games)):
    if year_indexes.keys() == 0:
        # TODO: The years don't work. When years increase, the teams stay the same and things break. Fix this.
        # This is not a fix, this is broken code.
        continue
    teams = {}
    for games in games:
        if games["team_name"] not in team_names:
            team_names.append(games["team_name"])
            teams[games["team_id"]] = Team(games["team_name"], games["year"])
    for game in games():
        game.rolling_average = teams[game["team_id"]].get_rolling_avg(game)
        teams[game["team_id"]].append_game(game)
    for player in players:
        teams[player["team_id"]].append_player(player)
open("teams.json", "w").write(json.dumps([team.to_dict() for team in teams.values()]))
