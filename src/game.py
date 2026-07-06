import time
import sys

def print_s(str, t=0.75):
	print(str)
	time.sleep(t)

def play():
	print_s("DINOSAURS the game", 1.5)
	print_s("")
	print_instructions()
	print_s("")
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
	print_s("starting the game...")


def print_instructions():
	print_s("instructions:")
	print_s("when the game gives you a choice, type the number that fits your choice")
	print_s("there are also certain key words that always do certain things")
	print_s("you cannot type a key word in the middle of a battle")
	print_s("key words:")
	print_s("type 'instructions' to read this again")
	print_s("type 'quit' to quit the game")
