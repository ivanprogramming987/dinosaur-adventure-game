import time
import sys

def print_s(str, t=1):
	print(str)
	time.sleep(t)

def game():
	print_s("DINOSAURS the game")
	print_s("starting...")
	print_instructions()
	print_s("\nplaying...")

def print_instructions():
        print_s("instructions:")
        print_s("when the game gives you a choice, type the number that fits your choice", 3)
        print_s("there are also certain key words that always do certain things", 3)
        print_s("key words:")
        print_s("type 'instructions' to read this again", 2)
        print_s("type 'quit' to quit the game", 2)
