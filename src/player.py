from constants import *
from game import print_s

class Player:
	def __init__():
		self.level = PLAYER_LEVEL
		self.attacks = PLAYER_ATTACKS
		self.defense = PLAYER_DEFENSE
		self.speed = PLAYER_SPEED

	def attack(self, target):
		attack_no = print_attacks()
                if attack_no > 5 or attack_no < 1:
                        print("Sorry, choose a number between 1 and 5")
			attack(target)
			return
		atk = self.attacks[attack_no - 1]
		atk.use(target)
		if self.speed > target.speed * 2:
			atk.use(target)

	def print_attacks(self):
		print_s("Pick an attack:")
		print_s(f"1. {self.attacks[0].name}")
		print_s(f"2. {self.attacks[1].name}")
		print_s(f"3. {self.attacks[2].name}")
		print_s(f"4. {self.attacks[3].name}")
		print_s(f"5. {self.attacks[4].name}")
		atk = int(input("choose one: "))
		return atk

	def __repr__(self):
		return "Player"
