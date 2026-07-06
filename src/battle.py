from game import print_s

def battle(player, enemies):
	while True:
		if player.health <= 0:
			print_s(f"Enemy(s) Win!")
			return False
		enemies_lose = True
		for enemy in enemies:
			if not enemy.health <= 0:
				enemies_lose = False
		if enemies_lose:
			print_s(f"Player Wins!")
			return True

		target = print_enemies()
		player.attack(target)
		for enemy in enemies:
			if enemy.health > 0:
				enemy.attack(player, enemy.next_attack())

def print_enemies():
	print_s("Pick an enemy:")
	print_s(f"1) {repr(enemies[0])}")
	if len(enemies) > 1:
		print_s(f"2) {repr(enemies[1])}")
	if len(enemies) > 2:
		print_s(f"3) {repr(enemies[2])}")
	if len(enemies) > 3:
		print_s(f"4) {repr(enemies[3])}")
	target = int(input("Choose one: "))
	if target < 1 or target > len(enemies):
		print("Sorry, choose one")
		return print_enemies()
