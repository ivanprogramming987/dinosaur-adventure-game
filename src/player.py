import random
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
		self.potions = PLAYER_POTIONS
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
		if attack_no == 3:
			if self.potions == 0:
				print_s("You don't have any potions")
				self.attack(target)
				return
			self.potions -= 1
			print_s(f"Potions left: {self.potions}")
		if attack_no == 5:
			if self.lasers == 0:
				print_s("You don't have any lasers")
				self.attack(target)
				return
			self.lasers -= 1
			print_s(f"Lasers left: {self.lasers}")
		atk.use(target, self)
		if target.health <= 0:
			return
		r = random.randint(0, 100)
		if self.speed > target.speed + 50:
			if r < 75:
				print_s("You were faster and attacked again!")
				self.attack(target)
		elif self.speed > target.speed + 35:
			if r < 50:
				print_s("You were faster and attacked again!")
				self.attack(target)
		elif self.speed > target.speed + 20:
			if r < 25:
				print_s("You were faster and attacked again!")
				self.attack(target)

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
		self.print_stats()

	def print_stats(self):
		print_s(f"Health: {self.health}/{self.max_health}")
		print_s(f"Speed: {self.speed}")
		print_s(f"Level: {self.level}")
		print_s(f"Lasers left: {self.lasers}")
		print_s(f"Potions left: {self.potions}")

	def __repr__(self):
		return self.name
