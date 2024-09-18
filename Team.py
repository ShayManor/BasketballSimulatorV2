class Team:
    def __init__(self, name, year):
        self.id = id
        self.name = name
        self.year = year
        self.games = []
        self.players = []
        self.rolling_avg = 0

    def append_player(self, player):
        self.players.append(player)

    def append_game(self, game):
        self.games.append(game)

    def get_rolling_avg(self, game):
        index = self.games.index(game)
        if len(self.games) -index < 5:
            return sum([game.score for game in self.games[index:]]) / (len(self.games)-index)
        else:
            return sum([game.score for game in self.games[index - 5:index]]) / 5

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "year": self.year,
            "games": [game.to_dict() for game in self.games],
            "players": [player.to_dict() for player in self.players],
        }