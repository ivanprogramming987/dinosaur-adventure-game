from main import print_s
import random

class Attack:
	def __init__(self, dmg, acc, name, func=None):
		self.dmg = dmg
		self.acc = acc
		self.name = name
		self.func = func

	def use(self, target, user):
		original_user_health = user.health
		r = random.randint(0, 100)
		if r < 10:
			if self.dmg != 0:
				target.health -= ((self.dmg * 2) - target.defense)
			if self.func != None:
				self.func(user)
				self.func(user)
			print_s(f"{self.name} activated on {repr(target)}, and made a critical hit, dealing {(self.dmg * 2) - target.defense if self.dmg > 0 else 0} damage! {repr(target)} HP remaining: {target.health}.")
		elif r < self.acc:
			if self.dmg != 0:
				target.health -= (self.dmg - target.defense)
			if self.func != None:
				self.func(user)
			print_s(f"{self.name} activated on {repr(target)}, dealing {self.dmg - target.defense if self.dmg > 0 else 0} damage. {repr(target)} HP remaining: {target.health}.")
		else:
			print_s(f"{self.name} activated on {repr(target)}, but missed. {repr(target)} HP remaining: {target.health}.")

		if user.health > original_user_health:
			print_s(f"{repr(user)} healed {user.health - original_user_health} damage! {repr(user)} HP remaining: {user.health}")
		elif user.health < original_user_health:
			print_s(f"{repr(user)} did {original_user_health - user.health} damage to himself/herself/itself! {repr(user)} HP remaining: {user.health}")
