import json

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Game import Game


class GameScraper:
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.num_years = 20

    def scrape_games(self):
        games = []
        for i in range(self.num_years):
            print(i)
            self.driver.get(
                f"https://www.nba.com/stats/teams/boxscores?SeasonType=Regular+Season&Season={2023 - i}-{str(2024 - i)[2:]}")
            self.select_all()
            wait = WebDriverWait(self.driver, 10)
            table_body = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Crom_body__UYOcU")))
            rows = table_body.find_elements(By.TAG_NAME, "tr")
            index = 0
            for row in rows:
                index += 1
                games_info = []
                cols = row.find_elements(By.TAG_NAME, "td")
                for col in cols:
                    games_info.append(col.text)
                games.append(Game(index, games_info[0], games_info[1][-3:], games_info[2], games_info[5], 2024 - i))
            games_dict = []
            for game in games:
                games_dict.append(game.to_dict())
                print(game.to_dict())
            with open("games.json", "w") as f:
                f.write(json.dumps(games_dict))

    def select_all(self):
        all_selector = self.driver.find_elements(By.XPATH, "//option[@value='-1']")
        selector_test = False
        for i in range(5):
            for selector in all_selector:
                if selector.text == "All":
                    selector.click()
                    selector_test = True
                    break
            if not selector_test and len(all_selector) > 0:
                print("ERROR")
                print(len(all_selector))
