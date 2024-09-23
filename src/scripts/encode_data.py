import json

from src.scripts.TrainingGame import TrainingGame

with open('/Users/shay/PycharmProjects/BasketballV2/src/data/teams.json', 'r') as f:
    data = json.load(f)

training_games = []
for team in data:
    for game in team["games"]:
        players = []
        for player in team["players"]:
            if int(player["year"]) == int(game["year"]) and player["team"] == game["team"]:
                players.append(player)
        training_game = TrainingGame(players, game["rolling_average"], game["score"], game["year"])
        if not training_game.players:
            print(game["id"])
        else:
            training_games.append(training_game)
with open('/Users/shay/PycharmProjects/BasketballV2/src/data/training_data.json', 'w') as f:
    f.write(json.dumps([game.__dict__ for game in training_games]))
