import json
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from player import Player

menu_path = "//*[@id='__next']/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div"
all_path = "//*[@id='__next']/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select/option[1]"
# number of years back to go
num_years = 24

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

final_players = []
# Get the data for each year
for year_index in range(num_years):
    driver.get(
        f"https://www.nba.com/stats/players/bio?Season={2023 - year_index}-{str(2024 - year_index)[2:]}&SeasonType=Regular%20Season&dir=D&sort=NET_RATING")

    driver.find_elements(By.XPATH, menu_path)[0].click()
    driver.find_elements(By.XPATH, all_path)[0].click()
    # Get the data table
    wait = WebDriverWait(driver, 10)
    table_body = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Crom_body__UYOcU")))
    rows = table_body.find_elements(By.TAG_NAME, "tr")
    players = []
    for row in rows:
        reduced_player_data = []
        cols = row.find_elements(By.TAG_NAME, "td")
        for col in cols:
            reduced_player_data.append(col.text)
        players.append(Player(rows.index(row), reduced_player_data, 2024 - year_index))
    final_players.append(players)
final_players_dict = []
# finalizes data
for player in players:
    final_players_dict.append(player.to_dict())
print(json.dumps(final_players_dict))
open("players.json", "w").write(json.dumps(final_players_dict))
