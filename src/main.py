import time
import sys
import game

def main():
	try:
		game.play()
	except (KeyboardInterrupt):
		print("Keyboard interrupt (Ctrl+C or Cmd+C) detected.")
		print("QUITTING GAME")

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
	print_s("The dinosaurs in this game were all real. Learn all about them!")
	print_s("They were:")
	print_s("Compsognathus")
	print_s("Tianyulong")
	print_s("Microraptor")
	print_s("Unktaheela (a plesiosaur)")
	print_s("Vespersaurus")
	print_s("Icthyodectes (a fish)")
	print_s("Anurognathus (a pterosaur)")
	print_s("Nemicolopterus (a pterosaur)")
	print_s("Coelophysis")
	print_s("Anhanguera (a pterosaur)")
	print_s("Einiosaurus")
	print_s("Homalocephale")
	print_s("Deinonychus")
	print_s("Chialingosaurus")
	print_s("Plesiosaurus (a plesiosaur)")
	print_s("Allosaurus")
	print_s("Gorgosaurus")
	print_s("Velociraptor")
	print_s("Stegosaurus")
	print_s("Triceratops")
	print_s("Pachycephalosaurus")
	print_s("Ankylosaurus")
	print_s("")
	print_s("And the bosses were:")
	print_s("Pentaceratops")
	print_s("Ceratosaurus")
	print_s("Parasaurolophus")
	print_s("Quetzalcoatlus (a pterosaur)")
	print_s("Cryodrakon (a pterosaur)")
	print_s("Elasmosaurus (a plesiosaur)")
	print_s("Argentinosaurus")
	print_s("Tyrannosaurus Rex")
	sys.exit()

def end():
	print_s("ARE YOU SURE YOU WANT TO QUIT?")
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
