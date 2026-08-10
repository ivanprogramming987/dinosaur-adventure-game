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
		print_s("1. Punch (does a low amount of damage with high accuracy)")
		print_s("2. Kick (does a higher amount of damage with lower accuracy)")
		print_s(f"3. Cure -- potions left: {self.potions} (heals a certain amount of damage. cannot use unless you have potions)")
		print_s("4. Smash (does a very high amount of damage, but you damage yourself)")
		print_s(f"5. Laser -- lasers left: {self.lasers} (does the same amount of damage as Kick, but with 100% accuracy. cannot use unless you have potions)")
		attack_no = choices(5)
		atk = self.attacks[attack_no - 1]
		if attack_no == 3:
			if self.potions == 0:
				print_s("You don't have any potions")
				self.attack(target)
				return
			self.potions -= 1
		if attack_no == 5:
			if self.lasers == 0:
				print_s("You don't have any lasers")
				self.attack(target)
				return
			self.lasers -= 1
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
