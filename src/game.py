from battle import *
from constants import *
from enemy import *
from player import *
from main import *
from dinosaurs import *

player = Player()

def play():
	print_s("DINOSAURS the game", 1.5)
	print_s("")
	print_instructions()
	print_s("")
	junk = input("Read story? (yes to read, anything else to not) ")
	if junk == "yes":
		print_s("THE STORY:")
		print_s("The year is 2898.")
		print_s("You have unearthed a weird purple-looking rock with a green spot on it. One of your crewmates examines the rock.", 2.5)
		print_s("Their rock-identifying app that can identify every rock can't figure it out and shows a weird structure with elements that don't exist.", 3)
		print_s("The green spot looks especially unusual. It glows. Your crewmate touches it.", 2)
		print_s("The crewmate starts glowing green and then vanishes! You and your best friends Ann and James are assigned to rescue him.", 2.5)
		print_s("You touch the green spot. All of a sudden your crewmates start blurring. Your vision goes black for a few moments. Then your vision returns.", 2.5)
		print_s("But it isn't the same desert dino dig you were at.", 2)
		print_s("It looks like a blurry green jungle with enormous birds. Then you realize those colorful feathered thingys aren't birds. One walks up to you. It's huge.", 2.5)
		print_s("When your vision clears, it hits you. It's a DINOSAUR. Such a thing has never happened before (despite there being apps that can recognize any rock or anything else, really).", 3.5)
		print_s("You have to escape. Your ultra-smart app tells you that you need to find another weird purple rock with a green glowing spot.", 5)
	print_s("")
	junk = input("Type anything you want, then type enter to start: ")
	print_s("starting the game...")
	print_s("You are in a jungle. There is a big tree next to you with a hole in it.", 1.25)
	print_s("You also see a big bunch of ferns and a well trod path used by dinos often.", 1.25)
	print_s("Which way do you want to go?")
	print_s("1) Go in the tree and explore")
	print_s("2) Look inside the ferns")
	print_s("3) Walk on the path")
	i = choices(3)
	if i == 1:
		TreeOne()
	elif i == 2:
		FernsOne()
	elif i == 3:
		PathOne()

def TreeOne(f=False):
	player.lasers += 2
	print_s(f"You found 2 lasers in the tree. Your crewmate must have dropped them. Player lasers: {player.lasers}")
	if f:
		print_s("You decide to walk on the path.")
		PathOne()
	print_s("What do you want to do now?")
	print_s("1) Look inside the ferns")
	print_s("2) Walk on the path")
	i = choices(2)
	if i == 1:
		FernsOne(True)
	elif i == 2:
		PathOne()

def FernsOne(t=False):
	player.health -= 5
	print_s(f"When you look inside the ferns, a dinosaur slashes your face! Player remaining HP: {player.health}")
	if t:
		print_s("You decide to walk on the path.")
		PathOne()
	print_s("What do you want to do now?")
	print_s("1) Go in the tree and explore")
	print_s("2) Walk on the path")
	i = choices(2)
	if i == 1:
		TreeOne(True)
	elif i == 2:
		PathOne()

def PathOne():
	if player.health <= 0:
		lose()
	print_s("You come to a big clearing. A small hungry-looking dinosaur shows up. He eyes you nervously.")
	print_s("Seeing that you are taking no notice, he attacks you!")
	print_s("!!! BATTLE COMPSOGNATHUS !!!")
	compsognathus_1 = Compsognathus("A")
	battle_outcome = battle(player, [compsognathus_1])
	if battle_outcome == False:
		lose()
	else:
		score += 200
		print_s(f"You earned 200 points for defeating Compsognathus! Score: {score}")


def print_instructions():
	print_s("instructions:")
	print_s("when the game gives you a choice, type the number that fits your choice, then type enter.")
	print_s("there are also certain key words that always do certain things")
	print_s("you can only type a key word at a checkpoint")
	print_s("key words:")
	print_s("type 'instructions' to read this again")
	print_s("type 'quit' to quit the game")
	print_s("type 'continue' to continue playing")
