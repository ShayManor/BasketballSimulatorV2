import json
# This file is me freaking out because this isn't working and hard coding things I shouldn't hardcode
with open('/Users/shay/PycharmProjects/BasketballV2/src/data/training_data.json', 'r') as file:
    data = json.load(file)

for game in data:
    for player in game["players"]:
        if player["name"] == "Elliot Williams":
            player["height"] = "6-5"
            player["weight"] = "181"
        if player["name"] == "Will Cherry":
            player["height"] = "6-1"
            player["weight"] = "176"
        if player["name"] == "Patrick Christopher":
            player["height"] = "6-5"
            player["weight"] = "209"
        if player["name"] == "Jeff Adrien":
            player["height"] = "6-7"
            player["weight"] = "245"
        if player["name"] == "Jerrelle Benimon":
            player["height"] = "6-8"
            player["weight"] = "245"
        if player["height"] == '' or player["weight"] == '':
            print(player["name"])

with open('/Users/shay/PycharmProjects/BasketballV2/src/data/training_data.json', 'w') as file:
    file.write(json.dumps(data))