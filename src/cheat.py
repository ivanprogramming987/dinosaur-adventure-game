import game

def main():
	try:
		print("CHEATING... (this is for test purposes)")
		game.player.name = "Cheater"
		for i in range(7):
			print("CHEATING...")
			game.player.level_up()
		print("FINISHED CHEATING...")
		game.player.potions = 3
		game.HideInCave()
	except (KeyboardInterrupt):
		print("Keyboard interrupt detected.")
		print("QUITTING GAME")

if __name__ == "__main__":
	main()
