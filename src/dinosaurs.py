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

class Coelophysis(Enemy):
	def __init__(self, letter):
		super().__init__(COELOPHYSIS_HEALTH, COELOPHYSIS_DEFENSE, COELOPHYSIS_SPEED, COELOPHYSIS_ATTACKS, f"Coelophysis {letter}")

class Ceratosaurus(Enemy):
	def __init__(self, letter):
		super().__init__(CERATOSAURUS_HEALTH, CERATOSAURUS_DEFENSE, CERATOSAURUS_SPEED, CERATOSAURUS_ATTACKS, f"Ceratosaurus {letter}")

	def __repr__(self):
		return f"Boss {self.name}"

class Anhanguera(Enemy):
	def __init__(self, letter):
		super().__init__(ANHANGUERA_HEALTH, ANHANGUERA_DEFENSE, ANHANGUERA_SPEED, ANHANGUERA_ATTACKS, f"Anhanguera {letter}")

class Einiosaurus(Enemy):
	def __init__(self, letter):
		super().__init__(EINIOSAURUS_HEALTH, EINIOSAURUS_DEFENSE, EINIOSAURUS_SPEED, EINIOSAURUS_ATTACKS, f"Einiosaurus {letter}")

class Homalocephale(Enemy):
	def __init__(self, letter):
		super().__init__(HOMALOCEPHALE_HEALTH, HOMALOCEPHALE_DEFENSE, HOMALOCEPHALE_SPEED, HOMALOCEPHALE_ATTACKS, f"Homalocephale {letter}")

class Deinonychus(Enemy):
	def __init__(self, letter):
		super().__init__(DEINONYCHUS_HEALTH, DEINONYCHUS_DEFENSE, DEINONYCHUS_SPEED, DEINONYCHUS_ATTACKS, f"Deinonychus {letter}")

class Chialingosaurus(Enemy):
	def __init__(self, letter):
		super().__init__(CHIALINGOSAURUS_HEALTH, CHIALINGOSAURUS_DEFENSE, CHIALINGOSAURUS_SPEED, CHIALINGOSAURUS_ATTACKS, f"Chialingosaurus {letter}")

class Parasaurolophus(Enemy):
	def __init__(self, letter):
		super().__init__(PARASAUROLOPHUS_HEALTH, PARASAUROLOPHUS_DEFENSE, PARASAUROLOPHUS_SPEED, PARASAUROLOPHUS_ATTACKS, f"Parasaurolophus {letter}")

	def __repr__(self):
		return f"Boss {self.name}"

class Plesiosaurus(Enemy):
	def __init__(self, letter):
		super().__init__(PLESIOSAURUS_HEALTH, PLESIOSAURUS_DEFENSE, PLESIOSAURUS_SPEED, PLESIOSAURUS_ATTACKS, f"Plesiosaurus {letter}")

class Allosaurus(Enemy):
	def __init__(self, letter):
		super().__init__(ALLOSAURUS_HEALTH, ALLOSAURUS_DEFENSE, ALLOSAURUS_SPEED, ALLOSAURUS_ATTACKS, f"Allosaurus {letter}")

class Quetzalcoatlus(Enemy):
	def __init__(self, letter):
		super().__init__(QUETZALCOATLUS_HEALTH, QUETZALCOATLUS_DEFENSE, QUETZALCOATLUS_SPEED, QUETZALCOATLUS_ATTACKS, f"Quetzalcoatlus {letter}")

	def __repr__(self):
		return f"Boss {self.name}"

class Cryodrakon(Enemy):
	def __init__(self, letter):
		super().__init__(CRYODRAKON_HEALTH, CRYODRAKON_DEFENSE, CRYODRAKON_SPEED, CRYODRAKON_ATTACKS, f"Cryodrakon {letter}")

	def __repr__(self):
		return f"Boss {self.name}"
