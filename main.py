from filter_teams import filter_teams
from nba_game_scraper import GameScraper
from nba_player_scraper import player_scraper


games = GameScraper()
games.scrape_games()
players = player_scraper()
players.scrape_players()
f = filter_teams()
f.finalize_data()
