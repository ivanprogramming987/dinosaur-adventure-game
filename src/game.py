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
		print_s("The crewmate starts glowing green and then vanishes! You are assigned to rescue him.", 2)
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
	if player.health > player.max_health:
		player.health = player.max_health
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
	print_s(f"You find a laser package on the floor! {repr(player)} lasers: {player.lasers}", 1.5)
	print_s("The clearing has been cleared by an enormous sauropod. However, several other dinosaurs have made it their home.", 1.5)
	print_s("You step on some eggs. The dinosaurs think you are a predator and try to fight you off!", 1.5)
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
	if player.health > player.max_health:
		player.health = player.max_health
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
	print_s("You go to the volcano. This is a scary place. There are big boulders and small rocks everywhere.", 1.5)
	print_s("A particularly enormous boulder blocks your path.", 1)
	print_s("Where do you want to go?")
	print_s("1. Walk on the left side of the boulder")
	print_s("2. Walk on the right side of the boulder")
	i = choices(2)
	if i == 1:
		LeftSideOne(keys)
	elif i == 2:
		RightSideOne(keys)

def LeftSideOne(keys, r=False):
	print_s("Oddly, the giant boulder is one in a big line of boulders that prevent you from crossing to the right side.", 1.5)
	print_s("There seems to be just a big nothingness surrounding you except for part of a key that you find. Suddenly, you hear a GLURP! GLOIIG! GBLEEEHK!", 2)
	print_s("You wonder where the noises are coming from. But then, you see a trickle of lava slowly flowing down the volcano.", 1.5)
	print_s("THE VOLCANO IS ERUPTING!", 1)
	print_s("You have to act fast. What do you want to do?", 1)
	print_s("1. Sprint down the volcano")
	print_s("2. Jog down the volcano")
	print_s("3. Walk down the volcano")
	i = choices(3)
	if i == 1:
		SprintDownVolcano(keys, r)
	elif i == 2:
		JogDownVolcano(keys, r)
	elif i == 3:
		WalkDownVolcano(keys, r)

def SprintDownVolcano(keys, r):
	print_s("You sprint very fast to the bottom. You sprint so fast that some little stones start rolling down.", 1.5)
	print_s("The little stones push some big stones. The big stones start rolling. It's an avalanche!!!", 2)
	player.health -= 40
	print_s(f"You escape, battered and bruised by the rocks. {repr(player)} health left: {player.health}", 1.5)
	if player.health <= 0:
		main.lose()
	if r:
		CompleteVolcano(keys)
	else:
		print_s("Once the eruption is over, you decide to try the right side of the rocks.", 1)
		RightSideOne(keys, True)

def JogDownVolcano(keys, r):
	player.lasers -= 3
	if player.lasers < 0:
		player.lasers = 0
	print_s(f"You jog, followed closely by the lava. You accidentally drop some lasers. They are consumed by the lava. {repr(player)} lasers: {player.lasers}", 2)
	print_s("You escape unhurt.")
	if r:
		CompleteVolcano(keys)
	else:
		print_s("Once the eruption is over, you decide to try the right side of the rocks.", 1)
		RightSideOne(keys, True)

def WalkDownVolcano(keys, r):
	player.health -= 20
	player.lasers -= 1
	if player.lasers < 0:
		player.lasers = 0
	print_s("You decide to be slow and not cause an avalanche. There is ONE PROBLEM, however.", 1.5)
	print_s(f"The lava is faster than you! It burns your ankles. You have to pick up speed. {repr(player)} health: {player.health}", 2)
	if player.health <= 0:
		main.lose()
	print_s(f"As you run faster, you drop a laser! The lava destroys it. {repr(player)} lasers: {player.lasers}", 1.5)
	print_s("You escape, despite the swelling burns on your ankles and worse-for-wear shoes.", 1.5)
	if r:
		CompleteVolcano(keys)
	else:
		print_s("Once the eruption is over, you decide to try the right side of the rocks.", 1)
		RightSideOne(keys, True)

def RightSideOne(keys, l=False):
	print_s("You walk up the volcano and find that the giant rock is in a big line of rocks, so you cannot go to the left side.", 1.5)
	print_s("This part of the volcano has small shrubs growing on it, along with small, speedy dinosaurs.", 1.5)
	print_s("There is a lake to your right and a big meadow of shrubs just ahead.", 1)
	print_s("Which way do you want to go?")
	print_s("1. Swim in the lake")
	print_s("2. Go to the meadow of shrubs")
	i = choices(2)
	if i == 1:
		SwimTwo(keys, l)
	elif i == 2:
		MeadowOne(keys, l)

def SwimTwo(keys, l, m=False):
	print_s("You swim in the lake. There is part of a key on the bottom! You dive to get it.", 1.5)
	print_s("As you dive to it, a hungry plesiosaur swims towards you. You turn away, hoping to leave before it notices you.", 1.5)
	print_s("But then, a sharp-toothed fish comes! You are stuck between two enemies. You have to fight.", 1.5)
	print_s("!!! BATTLE ICHTHYODECTES AND UNKTAHEELA !!!")
	ichthyodectes_1 = Ichthyodectes("A")
	unktaheela_1 = Unktaheela("A")
	battle_outcome = battle(player, [ichthyodectes_1, unktaheela_1])
	battle_aftermath(battle_outcome, 500)
	print_s("You get out of the lake, soaking wet and exhausted.", 1)
	if m:
		if l:
			CompleteVolcano(keys)
		else:
			print_s("You decide to go to the left side of the rocks.", 1)
			LeftSideOne(keys, True)
	else:
		print_s("You decide to go to the meadow of shrubs.", 1)
		MeadowOne(keys, l, True)

def MeadowOne(keys, l, s=False):
	print_s("You go into the meadow. You find part of a key.", 1)
	print_s("You escape a group of meat-eating dinosaurs attacking a plant-eater.", 1.5)
	print_s("But you do NOT escape a meat-eater and pterosaur that want to eat you. A fight happens.", 1.5)
	print_s("!!! BATTLE ANUROGNATHUS AND VESPERSAURUS !!!")
	anurognathus_1 = Anurognathus("A")
	vespersaurus_1 = Vespersaurus("A")
	battle_outcome = battle(player, [anurognathus_1, vespersaurus_1])
	battle_aftermath(battle_outcome, 500)
	print_s("You walk out of the meadow.", 1)
	if s:
		if l:
			CompleteVolcano(keys)
		else:
			print_s("You decide to go to the left side of the rocks.", 1)
			LeftSideOne(keys, True)
	else:
		print_s("You decide to swim in the lake.", 1)
		SwimTwo(keys, l, True)

def CompleteVolcano(keys):
	global score
	score += 100
	player.health += 30
	if player.health > player.max_health:
		player.health = player.max_health
	print_s(f"You finished the mountain safely and earned 100 points and 30 HP!. Score: {score}. {repr(player)} health: {player.health}")
	keys[1] = True
	if keys[0] == False and keys[2] == False:
		print_s("Where do you want to go now?")
		print_s("1. Climb the mountain")
		print_s("2. Hike into the desert")
		i = choices(2)
		if i == 1:
			MountainTwo(keys)
		elif i == 2:
			DesertOne(keys)
	elif keys[0] == False and keys[2] == True:
		print_s("You decide to climb the mountain.", 1)
		MountainTwo(keys)
	elif keys[0] == True and keys[2] == False:
		print_s("You decide to hike into the desert.", 1)
		DesertOne(keys)
	else:
		print_s("You got all three keys! You unlock the mountain door.", 2)
		CaveTwo()

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
	if player.health > player.max_health:
		player.health = player.max_health
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
	checkpoint()
	print_s("You go into the cave.")
	print_s("You turn on your flashlight and look around. This place is full of stalactites and stalagmites. They are beautiful.", 2)
	print_s("There is a split in the path.")
	print_s("Which way do you want to go?")
	print_s("1. To the left")
	print_s("2. To the right")
	i = choices(2)
	if i == 1:
		LeftSideTwo()
	elif i == 2:
		RightSideTwo()

def LeftSideTwo():
	print_s("You decide to choose the left side.")
	print_s("You see cave fish and giant cave bugs. Several are about two feet long! They are catching cave fish.", 1.5)
	print_s("Suddenly, SPLASH! you fall into a big lake. Some giant cave fish are coming!", 1.5)
	print_s("They look like some fish you have already seen in the present day. They don't bother with you.", 1.5)
	print_s("Others do. They swim at you. You've seen these too.", 1)
	print_s("It's Ichthyodectes again!")
	print_s("!!! BATTLE THREE ICHTHYODECTES !!!")
	ichthyodectes_1 = Ichthyodectes("A")
	ichthyodectes_2 = Ichthyodectes("B")
	ichthyodectes_3 = Ichthyodectes("C")
	battle_outcome = battle(player, [ichthyodectes_1, ichthyodectes_2, ichthyodectes_3])
	battle_aftermath(battle_outcome, 700)
	print_s("You find a crack in the wall. It looks like it leads into a passage.", 1.5)
	print_s("What do you want to do?")
	print_s("1. Squeeze through the crack")
	print_s("2. Keep going along the path")
	i = choices(2)
	if i == 1:
		CrackOne()
	elif i == 2:
		PathFour()

def CrackOne():
	player.health += 30
	if player.health > player.max_health:
		player.health = player.max_health
	print_s("It's a tight squeeze. Finally you emerge. There is a hole in the ceiling letting light AND creatures in.", 1.5)
	print_s(f"You find a granola bar. You eat it and heal a little. {repr(player)} health left: {player.health}", 1.5)
	find_mushroom(5)
	print_s("Some pterosaurs circling above think you look tasty. They attack!", 1)
	print_s("!!! BATTLE TWO ANUROGNATHUS !!!")
	anurognathus_1 = Anurognathus("A")
	anurognathus_2 = Anurognathus("B")
	battle_outcome = battle(player, [anurognathus_1, anurognathus_2])
	battle_aftermath(battle_outcome, 450)
	EndOfCave()

def PathFour():
	print_s("You keep going. You bump into some things. They peck your head.", 1)
	print_s("!!! BATTLE FOUR NEMICOLOPTERUS !!!")
	nemicolopterus_1 = Nemicolopterus("A")
	nemicolopterus_2 = Nemicolopterus("B")
	nemicolopterus_3 = Nemicolopterus("C")
	nemicolopterus_4 = Nemicolopterus("D")
	battle_outcome = battle(player, [nemicolopterus_1, nemicolopterus_2, nemicolopterus_3, nemicolopterus_4])
	battle_aftermath(battle_outcome, 600)
	EndOfCave()

def RightSideTwo():
	print_s("You choose the right side.")
	print_s("You see a dinosaur hiding in a crack in the wall. It blunders into you.", 1.5)
	print_s("It yelps in pain and some more dinosaurs come to it. They can't see you, but they can smell you.", 1.5)
	print_s("They assume you are a predator and run away. You keep going.", 1)
	print_s("Some pterosaurs come. One nips your head. They are attacking you!", 1)
	print_s("!!! BATTLE FOUR NEMICOLOPTERUS !!!")
	nemicolopterus_1 = Nemicolopterus("A")
	nemicolopterus_2 = Nemicolopterus("B")
	nemicolopterus_3 = Nemicolopterus("C")
	nemicolopterus_4 = Nemicolopterus("D")
	battle_outcome = battle(player, [nemicolopterus_1, nemicolopterus_2, nemicolopterus_3, nemicolopterus_4])
	battle_aftermath(battle_outcome, 600)
	print_s("You walk slowly and carefully. You get to a split in the path.", 1)
	print_s("Which way do you want to go?")
	print_s("1. Turn left")
	print_s("2. Go straight")
	print_s("3. Turn right")
	i = choices(3)
	if i == 1:
		LeftChamberOne()
	elif i == 2:
		ContinueRightSide()
	elif i == 3:
		RightChamberOne()

def LeftChamberOne(r=False):
	print_s("You choose to go left.")
	print_s("This is actually just a small chamber.", 1)
	player.health -= 30
	print_s(f"You are careless and trip! You are cut in the face by a stalagmite and land on hard, bumpy ground. {repr(player)} HP left: {player.health}", 2)
	if player.health <= 0:
		main.lose()
	print_s("You leave the chamber so you don't trip again.", 1)
	if r:
		print_s("You decide to go straight.")
		ContinueRightSide()
	else:
		print_s("Where do you want to go?")
		print_s("1. Go straight")
		print_s("2. Turn right")
		i = choices(2)
		if i == 1:
			ContinueRightSide()
		elif i == 2:
			RightChamberOne(True)

def RightChamberOne(l=False):
	global score
	print_s("You choose to go right.")
	print_s("This is actually just a small chamber.", 1)
	player.lasers += 2
	score += 200
	print_s(f"You find 2 lasers! {repr(player)} lasers: {player.lasers}.")
	print_s(f"You earned 200 points! Score: {score}.")
	print_s("You investigate the rest of the chamber, but find nothing. You leave the chamber.", 1.5)
	if l:
		print_s("You decide to go straight.")
		ContinueRightSide()
	else:
		print_s("Where do you want to go?")
		print_s("1. Turn left")
		print_s("2. Go straight")
		i = choices(2)
		if i == 1:
			LeftChamberOne()
		elif i == 2:
			ContinueRightSide()

def ContinueRightSide():
	print_s("You keep walking and find that a big block has come out of the wall, allowing light and life in. There are even trees growing next to you.", 2)
	print_s("This block allows even dinosaurs to walk inside, and there are several around you.", 1.5)
	print_s("Armored dinos are the biggest. But the carnivores can't eat them. They can eat you though. One attacks you.", 1.5)
	print_s("!!! BATTLE COELOPHYSIS !!!")
	coelophysis_1 = Coelophysis("A")
	battle_outcome = battle(player, [coelophysis_1])
	battle_aftermath(battle_outcome, 500)
	print_s("Several paths join. You enter the part where they join and walk along a barren hallway.", 1.5)
	EndOfCave()

def EndOfCave():
	global score
	checkpoint()
	print_s("You come to a door. When you try to open it, it doesn't open! But then, you see it! A four-digit combination lock!", 2)
	print_s("Type the code (a number from 1 to 9999, or type 10000 for a hint)")
	combination_lock(COMBINATION_LOCK_CODE_ONE, COMBINATION_LOCK_HINT_ONE)
	player.health += 60
	if player.health > player.max_health:
		player.health = player.max_health
	print_s(f"You find an energy drink! You drink it and heal. {repr(player)} health left: {player.health}", 1.5)
	player.potions += 1
	print_s(f"You found 1 potion! {repr(player)} potions: {player.potions}", 1.5)
	score += 300
	print_s(f"You earned 300 points! Score: {score}.")
	print_s("You enter a big room. The ceiling has completely fallen. A big, ferocious dinosaur is there.", 1.5)
	print_s("The dinosaur is really hungry and has had no food for a few days, so despite you being small in comparison, it attacks.", 2)
	print_s("!!! BOSS !!!")
	print_s("!!! BATTLE CERATOSAURUS !!!")
	ceratosaurus_1 = Ceratosaurus("A")
	battle_outcome = battle(player, [ceratosaurus_1])
	battle_aftermath(battle_outcome, 1500)
	print_s("As you defeat Ceratosaurus, the front of the room breaks!", 1)
	player.level_up()
	print_s("You exit the cave and go into a jungle.", 1)
	print_s("There is a big tree with low branches that you could climb. There is also a big clearing with a hill in the middle.", 2)
	print_s("Which way do you want to go?")
	print_s("1. Climb the tree")
	print_s("2. Climb the hill")
	print_s("3. Walk around the hill")
	i = choices(3)
	if i == 1:
		TreeTwo()
	elif i == 2:
		HillOne()
	elif i == 3:
		DetourTwo()

def TreeTwo():
	print_s("You decide to climb the tree. Odd, toothed birds are flying around you, eating bugs.", 1.5)
	print_s("You get to the top. You can see jungle all around you, broken only by a grassy hill.", 1.5)
	print_s("You can see the edge of the jungle and a desert just outside it. It is a wonderful sight.", 1.5)
	player.lasers += 2
	print_s(f"You find 2 lasers! {repr(player)} lasers: {player.lasers}", 1)
	print_s("You climb down. A pterosaur starts circling above you, screeching, and pecking you.", 1.5)
	print_s("You try to avoid it. But you can't. It's pulling your hair out!", 1)
	print_s("!!! BATTLE ANHANGUERA !!!")
	anhanguera_1 = Anhanguera("A")
	battle_outcome = battle(player, [anhanguera_1])
	battle_aftermath(battle_outcome, 600)
	print_s("You finish climbing down the tree.")
	JungleOne()

def HillOne():
	print_s("You decide to climb the hill. You see squashed fruits and broken glass bottles everywhere!", 1.5)
	player.potions += 1
	print_s(f"One glass bottle seems intact. It's a potion! {repr(player)} potions: {player.potions}", 1.5)
	print_s("You reach the top of the hill. You see a dinosaur sitting on eggs.", 1)
	print_s("You walk by the nest. Another dinosaur gets really scared and thinks you are an egg theif!", 1.5)
	print_s("It attacks you.")
	print_s("!!! BATTLE EINIOSAURUS !!!")
	einiosaurus_1 = Einiosaurus("A")
	battle_outcome = battle(player, [einiosaurus_1])
	battle_aftermath(battle_outcome, 600)
	print_s("You walk down the hill. You see something yummy.", 1)
	find_mushroom(10)
	JungleOne()

def DetourTwo():
	print_s("You take the route around the hill.")
	print_s("You see some dinosaurs butting heads. One looks like it has lost.", 1)
	print_s("You walk by. The dinosaur who lost seems to be really angry. It goes on a rampage and takes out it's rage on you!", 2)
	print_s("!!! BATTLE HOMALOCEPHALE !!!")
	homalocephale_1 = Homalocephale("A")
	battle_outcome = battle(player, [homalocephale_1])
	battle_aftermath(battle_outcome, 600)
	print_s("You see a fruiting tree. You eat a fruit. It's weird tasting, but enjoyable.", 1.5)
	find_fruit(-8, 13)
	find_fruit(-10, 15)
	JungleOne()

def JungleOne():
	checkpoint()
	print_s("You decide to go into the jungle.")
	find_fruit(-8, 10)
	print_s("It is dark. There are ferns everywhere. You keep tripping on roots and logs.", 1.5)
	print_s("You become aware of something softly walking behind you. You climb a tree, afraid it will notice you.", 1.5)
	print_s("You've seen that thing. That's the dinosaur that has your crewmate.", 1)
	print_s("You climb down the tree and chase it. But it's too fast. It escapes.", 1)
	player.lasers += 1
	print_s(f"You then see that your crewmate has dropped a laser! {repr(player)} lasers: {player.lasers}")
	print_s("You keep going and find food on a tree!", 1)
	find_mushroom(10)
	find_fruit(-10, 15)
	print_s("You run into some small things flying in the air. They are territorial and try to peck you out.", 1.5)
	print_s("!!! BATTLE FIVE NEMICOLOPTERUS !!!")
	nemicolopterus_1 = Nemicolopterus("A")
	nemicolopterus_2 = Nemicolopterus("B")
	nemicolopterus_3 = Nemicolopterus("C")
	nemicolopterus_4 = Nemicolopterus("D")
	nemicolopterus_5 = Nemicolopterus("E")
	battle_outcome = battle(player, [nemicolopterus_1, nemicolopterus_2, nemicolopterus_3, nemicolopterus_4, nemicolopterus_5])
	battle_aftermath(battle_outcome, 750)
	print_s("You then come to where the trees are a little more sparse. It's more open, and you can see a desert ahead of you.", 2)
	print_s("There are less ferns. But one big clump catches your eye. It is next to a big tree with very low branches.", 1.5)
	print_s("Which way do you want to go?")
	print_s("1. Climb the tree")
	print_s("2. Look in the ferns")
	print_s("3. Walk into the desert")
	i = choices(3)
	if i == 1:
		TreeThree()
	elif i == 2:
		FernsTwo()
	elif i == 3:
		DesertTwo()

def TreeThree(f=False):
	print_s("You decide to climb the tree.")
	player.health -= 30
	print_s(f"You climb the tree, but something pushes you off! {repr(player)} health left: {player.health}", 1.5)
	if player.health <= 0:
		main.lose()
	if f:
		DesertTwo()
	else:
		print_s("Where do you want to go?")
		print_s("1. Look in the ferns")
		print_s("2. Walk into the desert")
		i = choices(2)
		if i == 1:
			FernsTwo(True)
		elif i == 2:
			DesertTwo()
def FernsTwo(t=False):
	print_s("You decide to look in the ferns.")
	player.potions += 1
	print_s(f"You find a potion in the ferns! {repr(player)} potions: {player.potions}", 1)
	if t:
		DesertTwo()
	else:
		print_s("Where do you want to go?")
		print_s("1. Climb the tree")
		print_s("2. Walk into the desert")
		i = choices(2)
		if i == 1:
			TreeThree(True)
		elif i == 2:
			DesertTwo()

def DesertTwo():
	checkpoint()
	print_s("You decide to walk into the desert.")
	print_s("You see some hills. You look in them. They're nests!", 1)
	print_s("Some hunters are here. They see the eggs. Yum! One takes an egg. Ew! It's rotten.", 1.5)
	print_s("They see you. They're really hungry from living in the desert where there isn't much food, so they attack you!", 1.5)
	print_s("!!! BATTLE TWO VESPERSAURUS !!!")
	vespersaurus_1 = Vespersaurus("A")
	vespersaurus_2 = Vespersaurus("B")
	battle_outcome = battle(player, [vespersaurus_1, vespersaurus_2])
	battle_aftermath(battle_outcome, 600)
	print_s("You keep walking. You see a big footprint. In it is a measuring tape. Your crewmate is this way!", 1.5)
	player.health += 60
	if player.health > player.max_health:
		player.health = player.max_health
	print_s(f"You also find a granola bar in the footprint. You eat it and heal some. {repr(player)} health left: {player.health}", 2)
	print_s("You go in the direction of the footprint. Some more carnivores are here.", 1.5)
	print_s("Luckily, they spot some food and attack it. They don't bother with you or even see you.", 1.5)
	find_mushroom(10)
	print_s("There is a canyon. There are also two ways to go into the canyon. The canyon is wide enough that in order to keep up with the big dinosaur, you won't be able to go around the canyon.", 2.5)
	print_s("Which path do you want to go down?")
	print_s("1. Go down the steep slope")
	print_s("2. Go down the shallow slope")
	i = choices(2)
	if i == 1:
		SlopeOne()
	elif i == 2:
		SlopeTwo()

def SlopeOne():
	global score
	print_s("You decide to go down the steep slope.")
	player.health -= 50
	print_s(f"It's really steep and hard to climb. You slip and slide down the slope. {repr(player)} health left: {player.health}", 2)
	if player.health <= 0:
		main.lose()
	player.potions += 1
	score += 200
	print_s(f"You find 1 potion! {repr(player)} potions: {player.potions}.", 1.5)
	print_s(f"You earned 200 points! Score: {score}.", 1)
	print_s("There is a pond with creepy frogs in it. You leave the creepy frogs alone.", 1.5)
	print_s("You find a big dinosaur footprint. It isn't the right kind of footprint. The dinosaur that has your crewmate did not make this footprint.", 2)
	print_s("The two ways to get into the canyon merge. You have made it to the bottom.", 1.5)
	print_s("Which way do you want to go to climb out of the canyon?")
	print_s("1. Climb up the west side")
	print_s("2. Climb up the east side")
	i = choices(2)
	if i == 1:
		ClimbOne()
	elif i == 2:
		ClimbTwo()

def SlopeTwo():
	global score
	print_s("You decide to go down the shallow slope.")
	print_s("It's quite easy to walk down this shallow slope. You find footprints indicating the dinosaur with your crewmate has gone down this way.", 2)
	print_s("But the slight grade means dinosaurs could be here. They are.", 1.5)
	player.health -= 50
	print_s(f"Some start chasing you. You try to run away, but slip and fall. {repr(player)} health left: {player.health}", 1.5)
	if player.health <= 0:
		main.lose()
	player.lasers += 1
	score += 200
	print_s(f"You find 1 laser! {repr(player)} lasers: {player.lasers}.", 1.5)
	print_s(f"You earned 200 points! Score: {score}.", 1)
	print_s("You reach the bottom of the canyon!")
	print_s("How do you want to get out?")
	print_s("1. Climb up the west side")
	print_s("2. Climb up the east side")
	i = choices(2)
	if i == 1:
		ClimbOne()
	elif i == 2:
		ClimbTwo()

def ClimbOne():
	checkpoint()
	print_s("You decide to climb up the west side.")
	print_s("This is a hard, precipitous climb. You climb and climb until your muscles feel like they are going to burst.", 2)
	print_s("But you still aren't at the top yet. Finally you make it to a part where you can rest. You collapse, exhausted.", 2)
	print_s("However, this collapse disturbs something. It comes out of its hole in the canyon wall.", 1.5)
	print_s("When you turn around, you realize this is actually two dinosaurs, not one.", 1.5)
	print_s("!!! BATTLE COELOPHYSIS AND DEINONYCHUS !!!")
	coelophysis_1 = Coelophysis("A")
	deinonychus_1 = Deinonychus("A")
	battle_outcome = battle(player, [coelophysis_1, deinonychus_1])
	battle_aftermath(battle_outcome, 900)
	print_s("You keep climbing and eventually get out of the canyon!", 1)
	print_s("You decide to follow a path that turns right here.", 1)
	PathSix()

def ClimbTwo():
	checkpoint()
	print_s("You decide to climb up the east side.")
	print_s("This climb is quite ridiculously hard.", 1)
	print_s("You keep feeling like you just can't climb up that one more ledge. But you always climb it, only to find yet another ledge that you have to pull yourself up on to.", 2.5)
	print_s("You climb to a quite spacious ledge with small shrubs growing on it.", 1.5)
	print_s("Suddenly a territorial dinosaur comes. It tries to wack you off with its spiked tail. It misses.", 1.5)
	print_s("But it keeps trying to fight you off. You can't even find any way to climb out without it whipping you with its tail.", 2)
	print_s("!!! BATTLE CHIALINGOSAURUS !!!")
	chialingosaurus_1 = Chialingosaurus("A")
	battle_outcome = battle(player, [chialingosaurus_1])
	battle_aftermath(battle_outcome, 600)
	print_s("You climb out of the canyon. You see a path and decide to follow it.", 1.5)
	PathSix()

def PathSix():
	player.level_up()
	print_s("to be continued...")

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

def combination_lock(code, hint):
	i = choices(10000)
	if i == code:
		print_s("You unlocked the lock!")
		return
	elif i == 10000:
		print_s(hint)
		combination_lock(code)
	else:
		print_s("You did not unlock the lock.")
		combination_lock(code)

def battle_aftermath(battle_outcome, points):
	global score
	if battle_outcome == False:
		main.lose()
	else:
		score += points
		player.potions += 1
		print_s(f"You earned 1 potion! {repr(player)} potions: {player.potions}")
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
	print_s('there is no "save" function in this game. it WILL NOT reload ANYTHING if you quit.')

def checkpoint():
	print_s("CHECKPOINT! type instructions, quit, stats, or continue (anything else will default to 'continue')")
	i = input("Please choose: ")
	if i == "instructions":
		print_instructions()
	elif i == "quit":
		main.end()
	elif i == "stats":
		player.print_stats()
