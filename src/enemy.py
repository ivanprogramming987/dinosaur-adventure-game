import random
from main import print_s

class Enemy:
	def __init__(self, health, defense, speed, attacks, name):
		self.health = health
		self.defense = defense
		self.speed = speed
		self.attacks = attacks
		self.name = name
		self.max_health = health

	def attack(self, target):
		atk = self.next_attack()
		atk.use(target, self)
		r = random.randint(0, 100)
		if self.speed > target.speed + 50:
			if r < 75:
				print_s(f"{repr(self)} was faster and attacked again!")
				self.attack(target)
		elif self.speed > target.speed + 35:
			if r < 50:
				print_s(f"{repr(self)} was faster and attacked again!")
				self.attack(target)
		elif self.speed > target.speed + 20:
			if r < 25:
				print_s(f"{repr(self)} was faster and attacked again!")
				self.attack(target)

	def next_attack(self):
		r = random.randint(0, len(self.attacks) - 1)
		return self.attacks[r]

	def __repr__(self):
		return f"Enemy {self.name}"
