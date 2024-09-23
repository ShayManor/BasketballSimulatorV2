from src.scripts.filter_teams import filter_teams
from src.scripts.nba_game_scraper import GameScraper
from src.scripts.nba_player_scraper import player_scraper


games = GameScraper()
games.scrape_games()
players = player_scraper()
players.scrape_players()
f = filter_teams()
f.finalize_data()
