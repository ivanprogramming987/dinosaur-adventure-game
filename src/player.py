from constants import *
from game import print_s

class Player:
	def __init__():
		self.level = PLAYER_LEVEL
		self.attacks = PLAYER_ATTACKS_LEVEL_1
		self.defense = PLAYER_DEFENSE
		self.speed = PLAYER_SPEED
		self.health = PLAYER_HEALTH
		self.max_health = PLAYER_HEALTH
		self.lasers = PLAYER_LASERS

	def attack(self, target):
		attack_no = print_attacks()
		atk = self.attacks[attack_no - 1]
		if attack_no == 5:
			self.lasers -= 1
			if self.lasers == 0:
				print_s("You don't have any lasers")
				return
		atk.use(target, self)
		if self.speed > target.speed * 2:
			atk.use(target, self)

	def print_attacks(self):
		print_s("Pick an attack:")
		print_s(f"1. {self.attacks[0].name}")
		print_s(f"2. {self.attacks[1].name}")
		print_s(f"3. {self.attacks[2].name}")
		print_s(f"4. {self.attacks[3].name}")
		print_s(f"5. {self.attacks[4].name}")
		atk = int(input("choose one: "))
		if atk > 5 or atk < 1:
			print_s("Sorry, choose a number between 1 and 5")
			return print_attacks()

	def level_up(self):
		self.level += 1
		print_s("LEVEL UP!")
		print_s(f"you are at level {self.level}")
		self.max_health += 50
		self.defense += 10
		self.speed += 25
		if self.level == 3:
			self.attacks = PLAYER_ATTACKS_LEVEL_3
		elif self.level == 5:
			self.attacks = PLAYER_ATTACKS_LEVEL_5
		elif self.level == 7:
			self.attacks = PLAYER_ATTACKS_LEVEL_7
		elif self.level == 9:
			self.attacks = PLAYER_ATTACKS_LEVEL_9
		elif self.level == 10:
			self.max_health += 50
			self.defense += 10
			self.speed += 25
		self.health = self.max_health

	def __repr__(self):
		return "Player"
