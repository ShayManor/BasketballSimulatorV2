class Final_Game:
    def __init__(id, players1, players2, scores, year):
        self.id = id
        self.players1 = players1
        self.players2 = players2
        self.scores = scores
        self.year = year

    def to_dict(self):
        return {
            "id": self.id,
            "Players1": self.Players1,
            "Players2": self.Players2,
            "scores": self.scores,
            "year": self.year,
        }

    def to_jsonl(self):
        pass
