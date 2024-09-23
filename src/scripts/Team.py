import json


class Team:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.games = []
        self.players = []
        self.rolling_avg = 0

    def append_player(self, player):
        self.players.append(player)

    def append_game(self, game):
        self.games.append(game)

    def set_rolling_avg(self):
        avg_sum = sum([int(game["score"]) for game in self.games[-5:]])
        window = 5
        for i in range(len(self.games)):
            game = self.games[i]
            if window == 1:
                game["rolling_average"] = game["score"]
                return
            avg_sum += int(game["score"])
            avg_sum -= int(self.games[i+window-1]["score"])
            if len(self.games) - i <= window:
                game["rolling_average"] = avg_sum / (len(self.games)-i)
            else:
                game["rolling_average"] = avg_sum / (window)
            if len(self.games) - i <= window:
                window -= 1

    def get_rolling_average(self):
        rolling_games = []
        self.games = self.games[::-1]
        for game in self.games:
            if len(rolling_games) < 5:
                rolling_games.append(int(game["score"]))
            if self.games.index(game) >= 5:
                rolling_games.append(int(game["score"]))
                rolling_games.pop(0)
            game["rolling_average"] = sum(rolling_games) / min(5, self.games.index(game) + 1)
            if len(rolling_games) != 5:
                print("ERROR")
                print(len(rolling_games))


    def to_dict(self):
        return {
            "name": self.name,
            "year": self.year,
            "games": self.games,
            "players": self.players,
        }