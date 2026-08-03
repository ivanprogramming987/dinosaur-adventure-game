from enemy import Enemy
from attack import Attack
from constants import *

class Compsognathus(Enemy):
	def __init__(self, letter):
		super().__init__(COMPSOGNATHUS_HEALTH, COMPSOGNATHUS_DEFENSE, COMPSOGNATHUS_SPEED, COMPSOGNATHUS_ATTACKS, f"Compsognathus {letter}")

class Tianyulong(Enemy):
	def __init__(self, letter):
		super().__init__(TIANYULONG_HEALTH, TIANYULONG_DEFENSE, TIANYULONG_SPEED, TIANYULONG_ATTACKS, f"Tianyulong {letter}")

class Microraptor(Enemy):
	def __init__(self, letter):
		super().__init__(MICRORAPTOR_HEALTH, MICRORAPTOR_DEFENSE, MICRORAPTOR_SPEED, MICRORAPTOR_ATTACKS, f"Microraptor {letter}")

class Pentaceratops(Enemy):
	def __init__(self, letter):
		super().__init__(PENTACERATOPS_HEALTH, PENTACERATOPS_DEFENSE, PENTACERATOPS_SPEED, PENTACERATOPS_ATTACKS, f"Pentaceratops {letter}")
		self.max_health = PENTACERATOPS_HEALTH

	def __repr__(self):
		return f"Boss {self.name}"

class Unktaheela(Enemy):
	def __init__(self, letter):
		super().__init__(UNKTAHEELA_HEALTH, UNKTAHEELA_DEFENSE, UNKTAHEELA_SPEED, UNKTAHEELA_ATTACKS, f"Unktaheela {letter}")

class Vespersaurus(Enemy):
	def __init__(self, letter):
		super().__init__(VESPERSAURUS_HEALTH, VESPERSAURUS_DEFENSE, VESPERSAURUS_SPEED, VESPERSAURUS_ATTACKS, f"Vespersaurus {letter}")

class Ichthyodectes(Enemy):
	def __init__(self, letter):
		super().__init__(ICHTHYODECTES_HEALTH, ICHTHYODECTES_DEFENSE, ICHTHYODECTES_SPEED, ICHTHYODECTES_ATTACKS, f"Ichthyodectes {letter}")

class Anurognathus(Enemy):
	def __init__(self, letter):
		super().__init__(ANUROGNATHUS_HEALTH, ANUROGNATHUS_DEFENSE, ANUROGNATHUS_SPEED, ANUROGNATHUS_ATTACKS, f"Anurognathus {letter}")

class Nemicolopterus(Enemy):
	def __init__(self, letter):
		super().__init__(NEMICOLOPTERUS_HEALTH, NEMICOLOPTERUS_DEFENSE, NEMICOLOPTERUS_SPEED, NEMICOLOPTERUS_ATTACKS, f"Nemicolopterus {letter}")
