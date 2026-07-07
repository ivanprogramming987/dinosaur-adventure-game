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
			target.health -= (self.dmg - target.defense)
			if self.func != None:
				self.func(user)
			print_s(f"{self.name} activated on {repr(target)}, dealing {self.dmg} damage. {repr(target)} HP remaining: {target.health}. {repr(target)} remaining lasers: {target.lasers}")
		elif r < self.acc / 4:
			target.health -= ((self.dmg * 2) - target.defense)
			if self.func != None:
				self.func(user)
				self.func(user)
			print_s(f"{self.name} activated on {repr(target)}, and made a critical hit, dealing {self.dmg * 2} damage! {repr(target)} HP remaining: {target.health}. {repr(target)} lasers remaining: {target.lasers}")
		else:
			print_s(f"{self.name} activated on {repr(target)}, but missed. {repr(target)} HP remaining: {target.health}. {repr(target)} lasers remaining: {target.lasers}")
