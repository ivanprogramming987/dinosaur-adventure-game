import game

def main():
	print("CHEATING... (this is for test purposes)")
	game.player.name = "Cheater"
	for i in range(2):
		print("CHEATING...")
		game.player.level_up()
	game.player.health = 100
	print("FINISHED CHEATING...")
	game.EndOfCave()

if __name__ == "__main__":
	main()
