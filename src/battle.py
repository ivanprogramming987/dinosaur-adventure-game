from main import print_s
from main import choices

def battle(player, enemies):
	while True:
		if player.health <= 0:
			print_s(f"Enemy(s) Win!")
			return False

		print_s("Pick an enemy:")
		print_s(f"1. {repr(enemies[0])}")
		if len(enemies) > 1:
			print_s(f"2. {repr(enemies[1])}")
		if len(enemies) > 2:
			print_s(f"3. {repr(enemies[2])}")
		if len(enemies) > 3:
			print_s(f"4. {repr(enemies[3])}")
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
