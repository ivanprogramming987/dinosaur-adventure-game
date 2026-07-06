import unittest
from player import *
from constants import *

class TestPlayer(unittest.TestCase):
	def test_player_init(self):
		player = Player()
