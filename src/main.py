import time
import sys
import game

def main():
	game.play()

def lose():
	print_s("YOU LOSE")
	print_s("You have failed to rescue your crewmate and find the purple stone.", 1)
	print_s(f"Score: {game.score}")
	print_s("GAME OVER")
	sys.exit()

def win():
	print_s("YOU WIN!!")
	print_s("Congratulations!")
	print_s(f"Score: {game.score}")
	sys.exit()

def end():
	print_s("ARE YOU SURE?")
	print_s("1. Yes")
	print_s("2. No")
	i = choices(2)
	if i == 1:
		print_s("QUITTING GAME")
		print_s("Score: {game.score}")
		sys.exit()
	elif i == 2:
		print_s("RESUMING GAME")

def print_s(str, t=0.75):
	print(str)
	time.sleep(t)

def choices(max):
	try:
		i = int(input("Please choose: "))
	except (ValueError, TypeError):
		print_s("Must type integer")
		return choices(max)
	if i < 1 or i > max:
		print_s(f"Sorry, choose a number between 1 and {max}")
		return choices(max)
	return i

if __name__ == "__main__":
	main()
