class Enemy:
	def __init__(self, health, defense, speed, attacks, name):
		self.health = health
		self.defense = defense
		self.speed = speed
		self.attacks = attacks
		self.name = name

	def attack(self, target, attack_no):
		atk = self.attacks[attack_no]
		atk.use(target)
		if self.speed >= target.speed * 2:
			atk.use(target)

	def __repr__(self):
		return f"Enemy {self.name}"
