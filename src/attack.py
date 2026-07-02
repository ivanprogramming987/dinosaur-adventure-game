from player import *
from enemy import *
from game import print_s
import random

class Attack:
	def __init__(self, dmg, acc, name):
		self.dmg = dmg
		self.acc = acc
		self.name = name

	def use(self, target):
		r = random.randint(0, 100)
		if r < acc:
			target.health -= (dmg - target.defense)
			print_s(f"{self.name} activated on {target.repr()}, dealing {dmg} damage. Target HP remaining: {target.health}")
		else:
			print_s(f"{self.name} activated on {target.repr()}, but missed. Target HP remaining: {target.health}")
