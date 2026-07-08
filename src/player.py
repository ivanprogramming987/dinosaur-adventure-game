from constants import *
from main import print_s
from main import choices

class Player:
	def __init__(self):
		self.level = PLAYER_LEVEL
		self.attacks = PLAYER_ATTACKS_LEVEL_1
		self.defense = PLAYER_DEFENSE
		self.speed = PLAYER_SPEED
		self.health = PLAYER_HEALTH
		self.max_health = PLAYER_HEALTH
		self.lasers = PLAYER_LASERS
		self.name = "Player"

	def attack(self, target):
		print_s("Pick an attack:")
		print_s(f"1. {self.attacks[0].name}")
		print_s(f"2. {self.attacks[1].name}")
		print_s(f"3. {self.attacks[2].name}")
		print_s(f"4. {self.attacks[3].name}")
		print_s(f"5. {self.attacks[4].name}")
		attack_no = choices(5)
		atk = self.attacks[attack_no - 1]
		if attack_no == 5:
			if self.lasers == 0:
				print_s("You don't have any lasers")
				return
			self.lasers -= 1
			print_s(f"Lasers left: {self.lasers}")
		atk.use(target, self)
		if self.speed > target.speed * 2:
			atk.use(target, self)

	def level_up(self):
		self.level += 1
		print_s("LEVEL UP!")
		print_s(f"you are at level {self.level}!")
		self.max_health += 50
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
			self.speed += 25
		self.health = self.max_health

	def __repr__(self):
		return self.name
