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
