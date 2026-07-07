from enemy import Enemy
from attack import Attack

class Compsognathus(Enemy): # worth 200 points when defeated
	def __init__(self, letter):
		super().__init__(55, 10, 75, [Attack(15, 75, "Slash", None), Attack(25, 50, "Tail Swipe", None)], f"Compsognathus {letter}")
