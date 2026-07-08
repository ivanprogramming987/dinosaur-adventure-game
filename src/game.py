from battle import *
from constants import *
from enemy import *
from player import *
from dinosaurs import *
import main
import random

score = 0
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
	junk = input("Type your name, then type enter to start: ")
	player.name = junk
	print_s("starting the game...")
	print_s("You are in a jungle. There is a big tree next to you with a hole in it.", 1.25)
	print_s("You also see a big bunch of ferns and a well trod path used by dinos often.", 1.25)
	print_s("Which way do you want to go?")
	print_s("1. Go in the tree and explore")
	print_s("2. Look inside the ferns")
	print_s("3. Walk on the path")
	i = choices(3)
	if i == 1:
		TreeOne()
	elif i == 2:
		FernsOne()
	elif i == 3:
		PathOne()

def TreeOne(f=False):
	global score
	player.lasers += 2
	score += 100
	print_s(f"You found 2 lasers in the tree. Your crewmate must have dropped them. {repr(player)} lasers: {player.lasers}")
	print_s(f"You earned 100 points for finding the lasers! Score: {score}")
	if f:
		print_s("You decide to walk on the path.")
		PathOne()
	print_s("What do you want to do now?")
	print_s("1. Look inside the ferns")
	print_s("2. Walk on the path")
	i = choices(2)
	if i == 1:
		FernsOne(True)
	elif i == 2:
		PathOne()

def FernsOne(t=False):
	player.health -= 5
	print_s(f"When you look inside the ferns, a dinosaur slashes your face! {repr(player)} remaining HP: {player.health}")
	if t:
		print_s("You decide to walk on the path.")
		PathOne()
	print_s("What do you want to do now?")
	print_s("1. Go in the tree and explore")
	print_s("2. Walk on the path")
	i = choices(2)
	if i == 1:
		TreeOne(True)
	elif i == 2:
		PathOne()

def PathOne():
	global score
	if player.health <= 0:
		lose()
	print_s("You come to a big clearing. A small hungry-looking dinosaur shows up. He eyes you nervously.", 1)
	print_s("Seeing that you are taking no notice, he attacks you!", 1)
	print_s("!!! BATTLE COMPSOGNATHUS !!!")
	compsognathus_1 = Compsognathus("A")
	battle_outcome = battle(player, [compsognathus_1])
	if battle_outcome == False:
		lose()
	else:
		score += 200
		player.health += 10
		if player.health > player.max_health:
			player.health = player.max_health
		print_s(f"You earned 200 points and 10 HP for defeating Compsognathus! Score: {score}. {repr(player)} HP remaining: {player.health}")
	find_mushroom(50, 10, 10)
	print_s("The path climbs up a mountain. There is also a cave in the mountain.", 1)
	print_s("Which way do you want to go?")
	print_s("1. Climb the mountain")
	print_s("2. Go into the cave")
	print_s("3. Walk around the mountain")
	i = choices(3)
	if i == 1:
		MountainOne()
	elif i == 2:
		CaveOne()
	elif i == 3:
		DetourOne()

def MountainOne():
	global score
	find_mushroom(25, 25, 10)
	find_mushroom(75, 10, 25)
	print_s("You come to a field. You accidentally kick a small dinosaur.", 1)
	print_s("It gets angry and attacks you!", 1)
	print_s("!!! BATTLE TIANYULONG !!!")
	tianyulong_1 = Tianyulong("A")
	battle_outcome = battle(player, [tianyulong_1])
	if battle_outcome == False:
		lose()
	else:
		score += 200
		player.health += 10
		if player.health > player.max_health:
			player.health = player.max_health
		print_s(f"You earned 200 points and 10 HP for defeating Tianyulong! Score: {score}. {repr(player)} HP remaining: {player.health}")
	print_s("You walk down the mountain and find human footprints. Your crewmate must be this way.", 1)
	PathTwo()

def CaveOne():
	global score
	print_s("As you walk into the cave, a massive fluttering surrounds your head", 1)
	print_s("You automatically think 'Bats!' but then remember this is dinosaur times and there are no bats here.", 1)
	print_s("They swoop down on you. Obviously, they are hungry.", 1)
	print_s("!!! BATTLE THREE MICRORAPTOR !!!")
	microraptor_1 = Microraptor("A")
	microraptor_2 = Microraptor("B")
	microraptor_3 = Microraptor("C")
	battle_outcome = battle(player, [microraptor_1, microraptor_2, microraptor_3])
	if battle_outcome == False:
		lose()
	else:
		score += 400
		player.health += 20
		if player.health > player.max_health:
			player.health = player.max_health
		print_s(f"You earned 400 points and 20 HP for defeating three Microraptor! Score: {score}. {repr(player)} HP remaining: {player.health}")
	print_s("Luckily, after defeating the Microraptor, you are not troubled anymore.")
	player.lasers += 2
	score += 100
	print_s(f"You find 2 lasers lying on the floor! {repr(player)} lasers: {player.lasers}", 1)
	print_s(f"You earned 100 points for finding lasers! Score: {score}", 1)
	print_s(f"As you exit the cave, you see that the path continues and you see footprints.", 1)
	PathTwo()

def DetourOne():
	global score
	print_s("As you walk around the mountain, you trip and fall on a dinosaur's kill.", 1)
	print_s("The dinosaur and his friend jump out of a hole in the mountain and, thinking you are after their prey, attack you.", 1)
	compsognathus_2 = Compsognathus("A")
	compsognathus_3 = Compsognathus("B")
	print_s("!!! BATTLE TWO COMPSOGNATHUS !!!")
	battle_outcome = battle(player, [compsognathus_2, compsognathus_3])
	if battle_outcome == False:
		lose()
	else:
		score += 400
		player.health += 10
		if player.health > player.max_health:
			player.health = player.max_health
		print_s(f"You earned 400 points and 10 HP for defeating two Compsognathus! Score: {score}. {repr(player)} health: {player.health}")
	print_s("You continue along the path.")
	player.health += 20
	score += 100
	print_s("You find granola bars spilled everywhere. You eat one and you start healing from your wounds.", 1)
	print_s(f"You heal 20 damage and earn 100 points for your lucky find. Score: {score}. {repr(player)} health: {player.health}")
	print_s("You find that this detour converges onto the dino path. You also see footprints, which means your crewmate is nearby.", 1)
	PathTwo()

def PathTwo():
	player.level_up()
	print_s("walking on the path...")


def find_mushroom(probability_of_heal, heal, dmg):
	global score
	print_s("You found a mushroom!")
	print_s("Do you want to eat the mushroom?")
	print_s("1. Yes")
	print_s("2. No")
	i = choices(2)
	if i == 1:
		r = random.randint(0, 100)
		if r < probability_of_heal:
			player.health += heal
			score += 100
			if player.health > player.max_health:
				player.health = player.max_health
			print_s(f"The mushroom healed you. {repr(player)} health: {player.health}.")
			print_s(f"You earned 100 points for eating a good mushroom! Score: {score}")
		else:
			player.health -= dmg
			print_s(f"The mushroom poisoned you. {repr(player)} health: {player.health}.")
			if player.health <= 0:
				lose()
	elif i == 2:
		print_s("You decided not to eat the mushroom.")

def print_instructions():
	print_s("instructions:")
	print_s("when the game gives you a choice, type the number that fits your choice, then type enter.")
	print_s("there are also certain key words that always do certain things")
	print_s("you can only type a key word at a checkpoint")
	print_s("key words:")
	print_s("type 'instructions' to read this again")
	print_s("type 'quit' to quit the game")
	print_s("type 'continue' to continue playing")
