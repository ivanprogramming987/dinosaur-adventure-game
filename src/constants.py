from attack import *

# variables without functions
PLAYER_LEVEL = 1
PLAYER_SPEED = 50
PLAYER_DEFENSE = 0
PLAYER_HEALTH = 100
PLAYER_LASERS = 10
PLAYER_POTIONS = 1

COMPSOGNATHUS_HEALTH = 55
COMPSOGNATHUS_DEFENSE = 10
COMPSOGNATHUS_SPEED = 75
COMPSOGNATHUS_ATTACKS = [Attack(10, 85, "Slash"), Attack(20, 80, "Tail Swipe")]

TIANYULONG_HEALTH = 40
TIANYULONG_DEFENSE = 15
TIANYULONG_SPEED = 45
TIANYULONG_ATTACKS = [Attack(15, 80, "Bite"), Attack(20, 80, "Tail Swipe"), Attack(10, 100, "Scream")]

MICRORAPTOR_HEALTH = 20
MICRORAPTOR_DEFENSE = 5
MICRORAPTOR_SPEED = 45
MICRORAPTOR_ATTACKS = [Attack(5, 100, "Scream"), Attack(10, 85, "Swoop")]

PENTACERATOPS_HEALTH = 165
PENTACERATOPS_DEFENSE = 10
PENTACERATOPS_SPEED = 45
# pentaceratops attacks in "variables with functions" section

UNKTAHEELA_HEALTH = 100
UNKTAHEELA_DEFENSE = 10
UNKTAHEELA_SPEED = 100
UNKTAHEELA_ATTACKS = [Attack(15, 95, "Bite"), Attack(20, 85, "Neck Hit"), Attack(25, 75, "Powerful Current")]

VESPERSAURUS_HEALTH = 110
VESPERSAURUS_DEFENSE = 5
VESPERSAURUS_SPEED = 80
VESPERSAURUS_ATTACKS = [Attack(20, 95, "Kick"), Attack(25, 85, "Jump Kick"), Attack(10, 100, "Claw")]

ICHTHYODECTES_HEALTH = 65
ICHTHYODECTES_DEFENSE = 5
ICHTHYODECTES_SPEED = 70
ICHTHYODECTES_ATTACKS = [Attack(5, 100, "Tail Hit"), Attack(10, 85, "Chomp"), Attack(20, 75, "Ultra Chomp")]

ANUROGNATHUS_HEALTH = 65
ANUROGNATHUS_DEFENSE = 10
ANUROGNATHUS_SPEED = 70
ANUROGNATHUS_ATTACKS = [Attack(10, 80, "Head Hit"), Attack(15, 80, "Wing Smack")]

NEMICOLOPTERUS_HEALTH = 40
NEMICOLOPTERUS_DEFENSE = 5
NEMICOLOPTERUS_SPEED = 140
# nemicolopterus attacks are in "variables with functions" section

COELOPHYSIS_HEALTH = 140
COELOPHYSIS_DEFENSE = 5
COELOPHYSIS_SPEED = 90
COELOPHYSIS_ATTACKS = [Attack(20, 90, "Claw"), Attack(25, 85, "Slash"), Attack(30, 75, "Chomp")]

CERATOSAURUS_HEALTH = 250
CERATOSAURUS_DEFENSE = 5
CERATOSAURUS_SPEED = 100
# ceratosaurus attacks are in "variables with functions" section

ANHANGUERA_HEALTH = 210
ANHANGUERA_DEFENSE = 10
ANHANGUERA_SPEED = 150
ANHANGUERA_ATTACKS = [Attack(25, 80, "Peck"), Attack(35, 70, "Power Peck"), Attack(20, 85, "Wing Smack")]

EINIOSAURUS_HEALTH = 190
EINIOSAURUS_DEFENSE = 15
EINIOSAURUS_SPEED = 100
# einiosaurus attacks are in "variables with functions" section

HOMALOCEPHALE_HEALTH = 190
HOMALOCEPHALE_DEFENSE = 10
HOMALOCEPHALE_SPEED = 120
HOMALOCEPHALE_ATTACKS = [Attack(30, 80, "Headbutt"), Attack(40, 70, "Charge"), Attack(25, 85, "Tail Swipe")]

DEINONYCHUS_HEALTH = 120
DEINONYCHUS_DEFENSE = 10
DEINONYCHUS_SPEED = 150
DEINONYCHUS_ATTACKS = [Attack(25, 90, "Claw"), Attack(30, 85, "Slash"), Attack(35, 75, "Big Bite")]

CHIALINGOSAURUS_HEALTH = 190
CHIALINGOSAURUS_DEFENSE = 10
CHIALINGOSAURUS_SPEED = 140
# chialingosaurus attacks are in "variables with functions" section

PARASAUROLOPHUS_HEALTH = 350
PARASAUROLOPHUS_DEFENSE = 5
PARASAUROLOPHUS_SPEED = 160
# parasaurolophus attacks are in "variables with functions" section

PLESIOSAURUS_HEALTH = 220
PLESIOSAURUS_DEFENSE = 15
PLESIOSAURUS_SPEED = 190
PLESIOSAURUS_ATTACKS = [Attack(30, 90, "Tail Hit"), Attack(40, 80, "Neck Hit")]

ALLOSAURUS_HEALTH = 260
ALLOSAURUS_DEFENSE = 10
ALLOSAURUS_SPEED = 175
ALLOSAURUS_ATTACKS = [Attack(35, 90, "Slash"), Attack(50, 80, "Bite")]

QUETZALCOATLUS_HEALTH = 240
QUETZALCOATLUS_DEFENSE = 10
QUETZALCOATLUS_SPEED = 200
# quetzalcoatlus attacks are in "variables with functions" section

CRYODRAKON_HEALTH = 270
CRYODRAKON_DEFENSE = 20
CRYODRAKON_SPEED = 150
# cryodrakon attacks are in "variables with functions" section

GORGOSAURUS_HEALTH = 320
GORGOSAURUS_DEFENSE = 15
GORGOSAURUS_SPEED = 190
# gorgosaurus attacks are in "variables with functions" section

VELOCIRAPTOR_HEALTH = 80
VELOCIRAPTOR_DEFENSE = 10
VELOCIRAPTOR_SPEED = 200
VELOCIRAPTOR_ATTACKS = [Attack(15, 100, "Bite"), Attack(25, 90, "Slash")]

STEGOSAURUS_HEALTH = 350
STEGOSAURUS_DEFENSE = 15
STEGOSAURUS_SPEED = 225
STEGOSAURUS_ATTACKS = [Attack(40, 90, "Kick"), Attack(50, 90, "Tail Whip")]

TRICERATOPS_HEALTH = 330
TRICERATOPS_DEFENSE = 25
TRICERATOPS_SPEED = 250
# triceratops attacks are in "variables with functions" section

# functions
def heal_15(user):
	user.health += 15
	if user.health > user.max_health:
		user.health = user.max_health
def heal_25(user):
	user.health += 25
	if user.health > user.max_health:
		user.health = user.max_health
def heal_35(user):
	user.health += 35
	if user.health > user.max_health:
		user.health = user.max_health
def heal_45(user):
	user.health += 45
	if user.health > user.max_health:
                user.health = user.max_health
def heal_60(user):
	user.health += 60
	if user.health > user.max_health:
		user.health = user.max_health
def heal_80(user):
	user.health += 80
	if user.health > user.max_health:
                user.health = user.max_health
def heal_110(user):
	user.health += 110
	if user.health > user.max_health:
                user.health = user.max_health
def heal_150(user):
	user.health += 150
	if user.health > user.max_health:
                user.health = user.max_health

def damage_self_20(user):
	user.health -= 20
def damage_self_30(user):
	user.health -= 30
def damage_self_40(user):
	user.health -= 40
def damage_self_50(user):
	user.health -= 50
def damage_self_10(user):
	user.health -= 10


# variables with functions
PLAYER_ATTACKS_LEVEL_1 = [Attack(40, 95, "Punch"),Attack(50, 85, "Kick"),Attack(0, 100, "Cure", heal_25),Attack(60, 95, "Smash", damage_self_10),Attack(50, 100, "Laser")]
PLAYER_ATTACKS_LEVEL_3 = [Attack(50, 95, "Punch"),Attack(60, 85, "Kick"),Attack(0, 100, "Cure", heal_45),Attack(75, 95, "Smash", damage_self_20),Attack(60, 100, "Laser")]
PLAYER_ATTACKS_LEVEL_5 = [Attack(65, 95, "Punch"),Attack(75, 85, "Kick"),Attack(0, 100, "Cure", heal_80),Attack(100, 95, "Smash", damage_self_30),Attack(75, 100, "Laser")]
PLAYER_ATTACKS_LEVEL_7 = [Attack(80, 95, "Punch"),Attack(90, 85, "Kick"),Attack(0, 100, "Cure", heal_110),Attack(125, 95, "Smash", damage_self_40),Attack(90, 100, "Laser")]
PLAYER_ATTACKS_LEVEL_9 = [Attack(105, 95, "Punch"),Attack(115, 85, "Kick"),Attack(0, 100, "Cure", heal_150),Attack(140, 95, "Smash", damage_self_50),Attack(115, 100, "Laser")]

PENTACERATOPS_ATTACKS = [Attack(20, 90, "Horn Hit"), Attack(30, 80, "Charge", damage_self_10), Attack(15, 90, "Cure and Hit", heal_25)]
NEMICOLOPTERUS_ATTACKS = [Attack(5, 100, "Stupid Face", heal_15), Attack(10, 90, "Wing Smack"), Attack(15, 80, "Crash")]
CERATOSAURUS_ATTACKS = [Attack(30, 90, "Roar"), Attack(40, 80, "Bite", damage_self_10), Attack(20, 90, "Blood Drain", heal_25), Attack(25, 100, "Kick")]
EINIOSAURUS_ATTACKS = [Attack(0, 100, "Drink Water", heal_45), Attack(45, 80, "Power Hit", damage_self_10), Attack(30, 90, "Horn Hit")]
CHIALINGOSAURUS_ATTACKS = [Attack(0, 90, "Heal", heal_60), Attack(30, 80, "Tail Whap"), Attack(55, 80, "Super Smack", damage_self_20)]
PARASAUROLOPHUS_ATTACKS = [Attack(35, 100, "Cure and Hit", heal_35), Attack(40, 90, "Big Headbutt"), Attack(60, 80, "Stomp", damage_self_10)]
QUETZALCOATLUS_ATTACKS = [Attack(35, 90, "Peck"), Attack(0, 90, "Heal", heal_45), Attack(45, 80, "Swoop", damage_self_10)]
CRYODRAKON_ATTACKS = [Attack(25, 90, "Peck"), Attack(0, 90, "Heal", heal_45), Attack(35, 80, "Swoop", damage_self_10)]
GORGOSAURUS_ATTACKS = [Attack(35, 90, "Bite"), Attack(0, 90, "Heal", heal_60), Attack(60, 85, "Big Bite", damage_self_20)]
TRICERATOPS_ATTACKS = [Attack(25, 85, "Healing Kick", heal_35), Attack(60, 80, "Horn Hit", damage_self_10)]

# hidden variables
COMBINATION_LOCK_CODE_ONE = (6800 / 2) - 560 + (111 * 5) # this is in code so that the puzzle isn't spoiled
COMBINATION_LOCK_HINT_ONE = "The answer is in the game somewhere else"
