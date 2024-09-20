import json
import sys
from typing import Dict

from Team import Team


class filter_teams:

    def __init__(self):
        self.SWITCHED_TEAMS = {"SEA": "OKC", "NOH": "NOP", "NJN": "BKN", "VAN": "MEM", "NOK": "NOP"}
        with open("games.json", "r") as f:
            self.games = json.load(f)
        with open("players.json", "r") as f:
            self.players = json.load(f)
        self.year_indexes = {}
        self.team_names = []
        self.teams = {}


    def filter_teams_years(self):
        for game in self.games:
            if game["year"] not in self.year_indexes:
                self.year_indexes[game["year"]] = self.games.index(game)
        # for year in range(len(games)):
        #     if year_indexes.keys() == 0:
        #         # TODO: The years don't work. When years increase, the teams stay the same and things break. Fix this.
        #         # This is not a fix, this is broken code.
        #         continue

    def filter_games(self):
        for game in self.games:
            name = game["team"]
            if name in self.SWITCHED_TEAMS:
                name = self.SWITCHED_TEAMS[name]
            if name not in self.team_names:
                self.team_names.append(name)
                self.teams[name] = Team(name, game["year"])
        for game in self.games:
            name = game["team"]
            self.teams[name].append_game(game)
        for player in self.players:
            if player["draft_number"] == "Undrafted":
                player["draft_number"] = -1
            self.teams[player["team"]].append_player(player)
        teams_dict = []
        for team in self.teams:
            self.teams[team].get_rolling_average()
            teams_dict.append(self.teams[team].to_dict())
        return json.dumps(teams_dict)

    def finalize_data(self):
        self.filter_teams_years()
        open("teams.json", "w").write(self.filter_games())


f = filter_teams()
f.finalize_data()
for i in range(20):
    print(str(f.teams["ATL"].games[i]["rolling_average"]) + "   " + str(f.teams["ATL"].games[i]["score"]))

# ATL_games = f.teams["ATL"].games.get()
