import json
import sys
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from player import Player


class player_scraper():
    def __init__(self):
        # number of years back to go
        self.num_years = 20

        self.chrome_options = Options()
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.final_players = []
        self.final_players_dict = []

    def scrape_players(self):
        # Get the data for each year
        #         f"https://www.nba.com/stats/players/bio?Season=2023-2024&SeasonType=Regular%20Season&dir=D")
        for year_index in range(self.num_years):
            self.driver.get(
                f"https://www.nba.com/stats/players/bio?Season={2023 - year_index}-{str(2024 - year_index)[2:]}&SeasonType=Regular%20Season")
            # print(len(self.driver.find_elements(By.XPATH, self.menu_path)))
            # self.driver.find_elements(By.XPATH, self.all_path)[0].click()
            # Get the data table
            self.select_all()
            wait = WebDriverWait(self.driver, 10)
            table_body = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Crom_body__UYOcU")))
            rows = table_body.find_elements(By.TAG_NAME, "tr")
            players = []
            index = 0
            for row in rows:
                index += 1
                reduced_player_data = []
                cols = row.find_elements(By.TAG_NAME, "td")
                for col in cols:
                    reduced_player_data.append(col.text)
                players.append(Player(rows.index(row), reduced_player_data, 2024 - year_index))
                print(players)
            self.final_players.append(players)
            # finalizes data
            for player in players:
                self.final_players_dict.append(player.to_dict())

    def finalize_data(self):
        # print(json.dumps(self.final_players_dict))
        open("players.json", "w").write(json.dumps(self.final_players_dict))

    def select_all(self):
        all_selector = self.driver.find_elements(By.XPATH, "//option[@value='-1']")
        selector_test = False
        for selector in all_selector:
            if selector.text == "All":
                selector.click()
                selector_test = True
                break
        if not selector_test and len(all_selector) > 0:
            print("ERROR")
            print(len(all_selector))


player_scraper().scrape_players()
