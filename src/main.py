import time
import sys
from game import *

score = 0

def main():
	play()

def lose():
	print_s("YOU LOSE")
	print_s(f"Score: {score}")
	sys.exit()

def win():
	print_s("YOU WIN!!")
	print_s("Congratulations!")
	print_s(f"Score: {score}")
	sys.exit()

def print_s(str, t=0.75):
	print(str)
	time.sleep(t)

def choices(max):
	i = int(input("Please choose: "))
	if i < 1 or i > max:
		print_s("Sorry, choose one")
		return choices(max)
	return i

if __name__ == "__main__":
	main()
