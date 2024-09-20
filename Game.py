class Game:
    def __init__(self, game_id, team, opponent, date, score, year):
        self.game_id = game_id
        self.team = team
        self.opponent = opponent
        self.date = date
        self.score = score
        self.year = year
        self.rolling_average = 0
    
    def to_dict(self):
        d = {
            "id": self.game_id,
            "team": self.team,
            "opponent": self.opponent,
            "score": self.score,
            "date": self.date,
            "year": self.year,
        }
        if self.rolling_average != 0:
            d["rolling_average"] = self.rolling_average
        return d
    