
class Player:
    def __init__(self, id, bio_stats, year):
        self.id = id
        self.name = bio_stats[0]
        self.team = bio_stats[1]
        self.age = bio_stats[2]
        self.height = bio_stats[3]
        self.weight = bio_stats[4]
        self.college = bio_stats[5]
        self.country = bio_stats[6]
        self.draft_year = bio_stats[7]
        self.draft_round = bio_stats[8]
        self.draft_number = bio_stats[9]
        self.gp = bio_stats[10]
        self.pts = bio_stats[11]
        self.reb = bio_stats[12]
        self.ast = bio_stats[13]
        self.netrtg = bio_stats[14]
        self.oreb = bio_stats[15]
        self.dreb = bio_stats[16]
        self.usg = bio_stats[17]
        self.ts = bio_stats[18]
        self.astp = bio_stats[19]
        self.year = year


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            # "team": self.team,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            # "college": self.college,
            # "country": self.country,
            # "draft_year": self.draft_year,
            # "draft_round": self.draft_round,
            "draft_number": self.draft_number,
            "gp": self.gp,
            "pts": self.pts,
            "reb": self.reb,
            "ast": self.ast,
            "netrtg": self.netrtg,
            "oreb": self.oreb,
            "dreb": self.dreb,
            "usg": self.usg,
            "ts": self.ts,
            "astp": self.astp,
            "year": self.year,
        }

