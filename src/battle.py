from main import print_s
from main import choices

def battle(player, enemies):
	while True:
		if player.health <= 0:
			return False

		print_s("Pick an enemy:")
		for e in range(len(enemies)):
			print_s(f"{e+1}. {repr(enemies[e])}")
		i = choices(len(enemies))

		player.attack(enemies[i-1])
		if enemies[i-1].health <= 0:
			print(f"You defeated {repr(enemies[i-1])}")
			enemies.pop(i-1)
			if len(enemies) == 0:
				print_s(f"{repr(player)} Wins!")
				return True
		for enemy in enemies:
			enemy.attack(player)
