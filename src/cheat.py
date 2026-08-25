import game

def main():
	print("CHEATING... (this is for test purposes)")
	game.player.name = "Cheater"
	for i in range(4):
		print("CHEATING...")
		game.player.level_up()
	print("FINISHED CHEATING...")
	game.PathSix()

if __name__ == "__main__":
	main()
