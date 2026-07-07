import random

class Enemy:
	def __init__(self, health, defense, speed, attacks, name, lasers=None):
		self.health = health
		self.defense = defense
		self.speed = speed
		self.attacks = attacks
		self.name = name
		self.lasers = lasers

	def attack(self, target):
		attack_no = next_attack()
		atk = self.attacks[attack_no]
		atk.use(target, self)
		if self.speed >= target.speed * 2:
			atk.use(target, self)

	def next_attack(self):
		r = random.randint(0, len(self.attacks) - 1)
		return self.attacks[r]

	def __repr__(self):
		return f"Enemy {self.name}"
