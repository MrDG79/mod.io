import unittest
import async_modio

from .config import user_api_key, game_api_key, access_token
from .utils import run

class TestAsyncClient(unittest.TestCase):
    def test_oauth_access(self):
        client = async_modio.Client(auth=access_token, test=True)
        
        run(client.get_my_user())
        run(client.get_my_subs())
        run(client.get_my_events())
        run(client.get_games())
        run(client.get_my_mods())
        run(client.get_my_modfiles())
        run(client.get_my_ratings())

        run(client.close())

    def test_api_token(self):
        client = async_modio.Client(api_key=game_api_key, test=True)
        games = run(client.get_games())
        run(client.get_game(games.results[0].id))
        run(client.close())

        client = async_modio.Client(api_key=user_api_key, test=True)
        users = run(client.get_users())
        # run(client.get_user(users.results[0].id))
        run(client.close())
        
