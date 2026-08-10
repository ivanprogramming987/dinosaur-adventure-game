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
		if player.health <= 0:
			print_s(f"{repr(player)} killed himself/herself by damaging himself/herself!")
			return False

		if enemies[i-1].health <= 0:
			print_s(f"You defeated {repr(enemies[i-1])}!")
			enemies.pop(i-1)
			if len(enemies) == 0:
				print_s(f"{repr(player)} wins!")
				return True

		for e in range(len(enemies)):
			enemy = enemies[e]
			enemy.attack(player)
			if enemy.health <= 0:
				print_s(f"{repr(enemy)} killed itself by damaging itself!")
				enemies.pop(e)
				if len(enemies) == 0:
					print_s(f"{repr(player)} wins!")
					return True
