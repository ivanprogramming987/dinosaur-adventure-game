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
	print_s("Player stats:")
	player.print_stats()
	print_s("")
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
	print_s(f"You earned 100 points! Score: {score}")
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
	checkpoint()
	if player.health <= 0:
		main.lose()
	print_s("You come to a big clearing. A small hungry-looking dinosaur shows up. He eyes you nervously.", 1)
	print_s("Seeing that you are taking no notice, he attacks you!", 1)
	print_s("!!! BATTLE COMPSOGNATHUS !!!")
	compsognathus_1 = Compsognathus("A")
	battle_outcome = battle(player, [compsognathus_1])
	battle_aftermath(battle_outcome, 200)
	find_mushroom(5)
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
	find_mushroom(5)
	print_s("You come to a field. You accidentally kick a small dinosaur peacefully grazing on plants.", 1.5)
	print_s("It gets angry and attacks you!", 1)
	print_s("!!! BATTLE TIANYULONG !!!")
	tianyulong_1 = Tianyulong("A")
	battle_outcome = battle(player, [tianyulong_1])
	battle_aftermath(battle_outcome, 200)
	print_s("You walk down the mountain and find human footprints. Your crewmate must be this way.", 2)
	PathTwo()

def CaveOne():
	global score
	print_s("As you walk into the cave, a massive fluttering surrounds your head.", 1.5)
	print_s("You automatically think 'Bats!' but then remember this is dinosaur times and there are no bats here.", 2)
	print_s("They swoop down on you. Obviously, they are hungry.", 1)
	print_s("!!! BATTLE THREE MICRORAPTOR !!!")
	microraptor_1 = Microraptor("A")
	microraptor_2 = Microraptor("B")
	microraptor_3 = Microraptor("C")
	battle_outcome = battle(player, [microraptor_1, microraptor_2, microraptor_3])
	battle_aftermath(battle_outcome, 300)
	print_s("Luckily, after defeating the Microraptor, you are not troubled anymore.", 1)
	player.lasers += 2
	score += 100
	print_s(f"You find 2 lasers lying on the floor! {repr(player)} lasers: {player.lasers}", 1)
	print_s(f"You earned 100 points! Score: {score}", 1)
	print_s(f"As you exit the cave, you see that the path continues and you see footprints.", 2)
	PathTwo()

def DetourOne():
	global score
	print_s("As you walk around the mountain, you trip and fall on a dinosaur's kill.", 1)
	print_s("The dinosaur and his friend jump out of a hole in the mountain and, thinking you are after their prey, attack you.", 2)
	compsognathus_1 = Compsognathus("A")
	compsognathus_2 = Compsognathus("B")
	print_s("!!! BATTLE TWO COMPSOGNATHUS !!!")
	battle_outcome = battle(player, [compsognathus_1, compsognathus_2])
	battle_aftermath(battle_outcome, 400)
	print_s("You continue along the path.")
	player.health += 20
	score += 100
	print_s("You find granola bars spilled everywhere. You eat one and you start healing from your wounds.", 1)
	print_s(f"You heal 20 damage and earn 100 points! Score: {score}. {repr(player)} health: {player.health}")
	print_s("You find that this detour converges onto the dino path. You also see footprints, which means your crewmate is nearby.", 2)
	PathTwo()

def PathTwo():
	checkpoint()
	player.level_up()
	print_s("You follow your crewmate's footprints, but suddenly they vanish, replaced by a trail of huge dinosaur footprints.", 2)
	print_s("You follow the footprints, but another dinosaur shows up. A big dinosaur is chasing it.", 2)
	print_s("Luckily, the big dinosaur ignores you.", 1)
	find_mushroom(5)
	print_s("The path leads into a jungle and you follow it.", 1)
	print_s("You see dinosaurs flying through trees. They swoop down on you.", 1.5)
	print_s("Oh no! More Microraptor.")
	print_s("!!! BATTLE FOUR MICRORAPTOR !!!")
	microraptor_1 = Microraptor("A")
	microraptor_2 = Microraptor("B")
	microraptor_3 = Microraptor("C")
	microraptor_4 = Microraptor("D")
	battle_outcome = battle(player, [microraptor_1, microraptor_2, microraptor_3, microraptor_4])
	battle_aftermath(battle_outcome, 400)
	print_s("You see a huge dinosaur coming towards you. You climb a tree and luckily, it does not notice you.", 2)
	print_s("But then, you suddenly look closer. It's carrying someone.", 1.5)
	print_s("IT'S YOUR CREWMATE!!!", 1.5)
	find_mushroom(5)
	print_s("You climb down and start walking. You slip on some leaves.", 1.5)
	print_s("Oh no! A large, crabby herbivore shows up. It seems angry about you squashing its leaves.", 2)
	print_s("It lowers its head, showing five sharp horns.", 1)
	print_s("This dinosaur will be very difficult to fight.", 1)
	print_s("!!! BOSS !!!", 1)
	print_s("!!! BATTLE PENTACERATOPS !!!", 1)
	pentaceratops = Pentaceratops("A")
	battle_outcome = battle(player, [pentaceratops])
	battle_aftermath(battle_outcome, 1000)
	player.health += 80
	print_s(f"You find an energy drink. You drink it and heal some damage. {repr(player)} HP: {player.health}", 1.5)
	print_s("The path ends. You see a huge mountain, a volcano, and a desert.", 1.5)
	print_s("The mountain has a locked door on it. But, the door has three locks. You must find three keys to unlock it.", 2)
	print_s("Which way do you want to go? Each way has one key.")
	print_s("1. Climb the mountain")
	print_s("2. Go to the volcano !!! HARD !!!")
	print_s("3. Hike through the desert")
	keys = [False, False, False]
	i = choices(3)
	if i == 1:
		MountainTwo(keys)
	elif i == 2:
		VolcanoOne(keys)
	elif i == 3:
		DesertOne(keys)

def MountainTwo(keys):
	checkpoint()
	print_s("You are climbing up the mountain. You see a tree. To your delight, it has tasty fruit!", 1.5)
	find_fruit(-5, 8)
	print_s("You see a pond with a box in it. You also see a pit with something shiny in it.", 1.5)
	print_s("There is also a part of the jungle that seems to have been cleared by a large dinosaur.", 1.5)
	print_s("Which way do you want to go?")
	print_s("1. Swim to the box")
	print_s("2. Crawl into the pit")
	print_s("3. Look in the clearing")
	paths = [False, False, False]
	i = choices(3)
	if i == 1:
		SwimOne(paths, keys)
	elif i == 2:
		PitOne(paths, keys)
	elif i == 3:
		ClearingOne(paths, keys)

def SwimOne(paths, keys):
	global score
	print_s("You swim to the box and open it. There is part of a key inside!", 1)
	print_s("As you swim back, an odd long-necked thing swims towards you.", 1)
	print_s("It opens its mouth and rushes at you! You dodge the bite.", 1)
	print_s("But it is still trying to eat you.", 1)
	print_s("!!! BATTLE UNKTAHEELA !!!")
	unktaheela_1 = Unktaheela("A")
	battle_outcome = battle(player, [unktaheela_1])
	battle_aftermath(battle_outcome, 300)
	find_fruit(-8, 10)
	paths[0] = True
	if paths[1] == False and paths[2] == False:
		print_s("What do you want to do now?")
		print_s("1. Go into the pit")
		print_s("2. Walk to the clearing")
		i = choices(2)
		if i == 1:
			PitOne(paths, keys)
		elif i == 2:
			ClearingOne(paths, keys)
	elif paths[1] == False and paths[2] == True:
		print_s("You decide to go into the pit.", 1)
		PitOne(paths, keys)
	elif paths[1] == True and paths[2] == False:
		print_s("You decide to walk to the clearing.", 1)
		ClearingOne(paths, keys)
	else:
		CompleteMountain(keys)

def PitOne(paths, keys):
	print_s("You are going into the pit, when you find a stash of fruit and mushrooms!", 1.5)
	find_fruit(-10, 10)
	find_mushroom(10)
	print_s("You find the glinting object. It is part of the key and some glue to glue the key pieces.", 1.5)
	print_s("But there are a few dinosaurs snooping around. They are attacking a plant-eater.", 1.5)
	player.health -= 10
	print_s(f"You leave before they notice you. A dinosaur hiding in the sand bites your face! {repr(player)} health left: {player.health}", 2)
	if player.health <= 0:
		main.lose()
	print_s("You decide to leave in case that happens again.", 1)
	paths[1] = True
	if paths[0] == False and paths[2] == False:
		print_s("What do you want to do now?")
		print_s("1. Swim to the box")
		print_s("2. Walk to the clearing")
		i = choices(2)
		if i == 1:
			SwimOne(paths, keys)
		elif i == 2:
			ClearingOne(paths, keys)
	elif paths[0] == False and paths[2] == True:
		print_s("You decide to swim to the box.")
		SwimOne(paths, keys)
	elif paths[0] == True and paths[2] == False:
		print_s("You decide to go into the clearing.")
		ClearingOne(paths, keys)
	else:
		CompleteMountain(keys)

def ClearingOne(paths, keys):
	player.lasers += 1
	print_s(f"You find a laser package on the floor! {repr(player)} lasers: {player.lasers}", 1)
	print_s("The clearing has been cleared by an enormous sauropod. However, several other dinosaurs have made it their home.", 1.5)
	print_s("You step on some eggs. The dinosaurs think you are a predator and try to fight you off. There is also a real predator fighting you.", 2)
	tianyulong_1 = Tianyulong("A")
	tianyulong_2 = Tianyulong("B")
	print_s("!!! BATTLE TWO TIANYULONG !!!")
	battle_outcome = battle(player, [tianyulong_1, tianyulong_2])
	battle_aftermath(battle_outcome, 500)
	print_s("You find part of the key!", 1)
	paths[2] = True
	if paths[0] == False and paths[1] == False:
		print_s("What do you want to do now?")
		print_s("1. Swim to the box")
		print_s("2. Go into the pit")
		i = choices(2)
		if i == 1:
			SwimOne(paths, keys)
		elif i == 2:
			PitOne(paths, keys)
	elif paths[0] == False and paths[1] == True:
		print_s("You decide to swim to the box.")
		SwimOne(paths, keys)
	elif paths[0] == True and paths[1] == False:
		print_s("You decide to go into the pit.")
		PitOne(paths, keys)
	else:
		CompleteMountain(keys)

def CompleteMountain(keys):
	global score
	score += 100
	player.health += 30
	print_s(f"You finished the mountain safely and earned 100 points and 30 HP!. Score: {score}. {repr(player)} health: {player.health}")
	keys[0] = True
	if keys[1] == False and keys[2] == False:
		print_s("Where do you want to go now?")
		print_s("1. Walk to the volcano !!! HARD !!!")
		print_s("2. Hike into the desert")
		i = choices(2)
		if i == 1:
			VolcanoOne(keys)
		elif i == 2:
			DesertOne(keys)
	elif keys[1] == False and keys[2] == True:
		player.level_up()
		print_s("You decide to walk to the volcano.", 1)
		VolcanoOne(keys)
	elif keys[1] == True and keys[2] == False:
		print_s("You decide to hike into the desert.", 1)
		DesertOne(keys)
	else:
		print_s("You got all three keys! You unlock the mountain door.", 2)
		CaveTwo()

def VolcanoOne(keys):
	checkpoint()
	print_s("walking to the volcano...")

def CompleteVolcano(keys):
	print_s("You finished the volcano safely.")

def DesertOne(keys):
	checkpoint()
	print_s("You walk into the desert. It is a difficult hike.", 1)
	print_s("There are two big cacti with holes in them. There is also a block of sandstone ahead. You shake the sandstone block. It's hollow, and there is something in it.", 3)
	print_s("What do you want to do now?")
	print_s("1. Go into the first cactus")
	print_s("2. Go into the second cactus")
	print_s("3. Try to break the sandstone")
	print_s("4. Keep hiking into the desert")
	paths = [False, False]
	i = choices(4)
	if i == 1:
		CactusOne(paths, keys)
	elif i == 2:
		CactusTwo(paths, keys)
	elif i == 3:
		BreakSandstone(paths, keys)
	elif i == 4:
		PathThree(paths, keys)

def CactusOne(paths, keys):
	r = random.randint(-2, 2)
	if r < 0:
		player.lasers += r
		print_s(f"You go into the cactus and lose {r * -1} lasers. {repr(player)} lasers: {player.lasers}")
	elif r == 0:
		print_s("You go into the cactus. Nothing happens.")
	else:
		player.lasers += r
		print_s(f"You go into the cactus and find {r} lasers! {repr(player)} lasers: {player.lasers}")
		print_s(f"You earned 100 points! Score: {score}")
	n_choices = 1
	print_s("Where do you want to go?")
	print_s("1. Go into the second cactus")
	if paths[0] == False:
		print_s("2. Try to break the sandstone")
		n_choices = 2
	if paths[1] == False and paths[0] == False:
		print_s("3. Keep hiking into the desert")
		n_choices = 3
	if paths[1] == False and paths[0] == True:
		print_s("2. Keep hiking into the desert")
		n_choices = 2
	i = choices(n_choices)
	if i == 1:
		CactusTwo(paths, keys)
	elif i == 2:
		if paths[0] == True:
			PathThree(paths, keys)
		else:
			BreakSandstone(paths, keys)
	elif i == 3:
		PathThree(paths, keys)

def CactusTwo(paths, keys):
	print_s("You find a mushroom and a fruit that some dinosaur dropped.", 1)
	find_fruit(-6, 7)
	find_mushroom(5)
	n_choices = 1
	print_s("Where do you want to go?")
	print_s("1. Go into the first cactus")
	if paths[0] == False:
		print_s("2. Try to break the sandstone")
		n_choices = 2
	if paths[1] == False and paths[0] == False:
		print_s("3. Keep hiking into the desert")
		n_choices = 3
	if paths[1] == False and paths[0] == True:
		print_s("2. Keep hiking into the desert")
		n_choices = 2
	i = choices(n_choices)
	if i == 1:
		CactusOne(paths, keys)
	elif i == 2:
		if paths[0] == True:
			PathThree(paths, keys)
		else:
			BreakSandstone(paths, keys)
	elif i == 3:
		PathThree(paths, keys)

def BreakSandstone(paths, keys):
	print_s("You break the sandstone. Part of a key is inside along with some glue to stick the key together.", 1.5)
	paths[0] = True
	if paths[1] == True:
		CompleteDesert(keys)
	else:
		print_s("Where do you want to go?")
		print_s("1. Go into the first cactus")
		print_s("2. Go into the second cactus")
		print_s("3. Keep hiking into the desert")
		i = choices(3)
		if i == 1:
			CactusOne(paths, keys)
		elif i == 2:
			CactusTwo(paths, keys)
		elif i == 3:
			PathThree(paths, keys)

def PathThree(paths, keys):
	print_s("You keep hiking. You see a dinosaur. Food is scarce, so when it sees you, it attacks without hesitation.", 1.5)
	print_s("!!! BATTLE VESPERSAURUS !!!")
	vespersaurus_1 = Vespersaurus("A")
	battle_outcome = battle(player, [vespersaurus_1])
	battle_aftermath(battle_outcome, 300)
	print_s("You keep going. There is a big rock with writing on it. It says:", 1.5)
	print_s("")
	print_s("oa ej iiu 3395 eeh u", 2)
	print_s("")
	print_s("You find part of the key on a rock!", 1)
	print_s("You hike back to the two cacti and sandstone block.", 1)
	paths[1] = True
	if paths[0] == True:
		CompleteDesert(keys)
	else:
		print_s("Where do you want to go?")
		print_s("1. Go into the first cactus")
		print_s("2. Go into the second cactus")
		print_s("3. Break the sandstone block")
		i = choices(3)
		if i == 1:
			CactusOne(paths, keys)
		elif i == 2:
			CactusTwo(paths, keys)
		elif i == 3:
			BreakSandstone(paths, keys)

def CompleteDesert(keys):
	global score
        score += 100
        player.health += 30
        print_s(f"You finished the desert safely and earned 100 points and 30 HP!. Score: {score}. {repr(player)} health: {player.health}")
	keys[2] = True
	if keys[0] == False and keys[1] == False:
		print_s("Where do you want to go now?")
		print_s("1. Climb the mountain")
		print_s("2. Walk into the volcano !!! HARD !!!")
		i = choices(2)
		if i == 1:
			MountainTwo(keys)
		elif i == 2:
			VolcanoOne(keys)
	elif keys[0] == True and keys[1] == False:
		player.level_up()
		print_s("You decide to walk to the volcano.", 1)
		VolcanoOne(keys)
	elif keys[0] == False and keys[1] == True:
		print_s("You decide to climb the mountain.", 1)
		MountainTwo(keys)
	else:
		print_s("You got all three keys! You unlock the mountain door.", 2)
		CaveTwo()

def CaveTwo():
	print_s("going into the cave...")

def find_mushroom(n):
	global score
	print_s("You found a mushroom!")
	print_s("Do you want to eat the mushroom?")
	print_s("1. Yes")
	print_s("2. No")
	i = choices(2)
	if i == 1:
		r = random.randint(0, 100)
		if r < 75:
			player.health += n
			score += 100
			if player.health > player.max_health:
				player.health = player.max_health
			print_s(f"The mushroom healed you. {repr(player)} health: {player.health}.")
			print_s(f"You earned 100 points! Score: {score}")
		else:
			player.health -= n
			print_s(f"The mushroom poisoned you. {repr(player)} health: {player.health}.")
			if player.health <= 0:
				main.lose()
	elif i == 2:
		print_s("You decided not to eat the mushroom.")

def find_fruit(min, max):
	global score
	print_s("You found a fruit!")
	print_s("Do you want to eat the fruit?")
	print_s("1. Yes")
	print_s("2. No")
	i = choices(2)
	if i == 1:
		r = random.randint(min, max)
		if r > 0:
			player.health += r
			score += 100
			if player.health > player.max_health:
				player.health = player.max_health
			print_s(f"The fruit healed you. {repr(player)} health: {player.health}.")
			print_s(f"You earned 100 points! Score: {score}")
		elif r == 0:
			print_s("The fruit had no effect whatsoever.")
		else:
			player.health += r
			print_s(f"The fruit poisoned you. {repr(player)} health: {player.health}.")
			if player.health <= 0:
				main.lose()
	elif i == 2:
		print_s("You decided not to eat the fruit.")

def battle_aftermath(battle_outcome, points):
	global score
	if battle_outcome == False:
		main.lose()
	else:
		score += points
		print_s(f"You earned {points} points! Score: {score}")

def print_instructions():
	print_s("instructions:")
	print_s("when the game gives you a choice, type the number that fits your choice, then type enter.")
	print_s("there are also certain key words that always do certain things")
	print_s("you can only type a key word at a checkpoint")
	print_s("key words:")
	print_s("type 'instructions' to read this again")
	print_s("type 'quit' to quit the game")
	print_s("type 'continue' to continue playing")
	print_s("type 'stats' to see your stats")
	print_s("")
	print_s("if you need to quit immediately, type Ctrl+C. (it will give you an error message but don't worry about that.)")

def checkpoint():
	print_s("CHECKPOINT! type instructions, quit, stats, or continue (any other word will default to 'continue')")
	i = input("Please choose: ")
	if i == "instructions":
		print_instructions()
	elif i == "quit":
		main.end()
	elif i == "stats":
		player.print_stats()
