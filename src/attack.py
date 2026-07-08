from main import print_s
import random

class Attack:
	def __init__(self, dmg, acc, name, func):
		self.dmg = dmg
		self.acc = acc
		self.name = name
		self.func = func

	def use(self, target, user):
		r = random.randint(0, 100)
		if r < self.acc:
			if self.dmg != 0:
				target.health -= (self.dmg - target.defense)
			if self.func != None:
				self.func(user)
			print_s(f"{self.name} activated on {repr(target)}, dealing {self.dmg - target.defense} damage. {repr(target)} HP remaining: {target.health}.")
		elif r < self.acc / 4:
			if self.dmg != 0:
				target.health -= ((self.dmg * 2) - target.defense)
			if self.func != None:
				self.func(user)
				self.func(user)
			print_s(f"{self.name} activated on {repr(target)}, and made a critical hit, dealing {(self.dmg * 2) - target.defense} damage! {repr(target)} HP remaining: {target.health}.")
		else:
			print_s(f"{self.name} activated on {repr(target)}, but missed. {repr(target)} HP remaining: {target.health}.")
