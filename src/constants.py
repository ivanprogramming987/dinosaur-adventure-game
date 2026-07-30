from attack import *

# variables without functions
PLAYER_LEVEL = 1
PLAYER_SPEED = 50
PLAYER_DEFENSE = 0
PLAYER_HEALTH = 100
PLAYER_LASERS = 10

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

UNKTAHEELA_HEALTH = 90
UNKTAHEELA_DEFENSE = 10
UNKTAHEELA_SPEED = 120
UNKTAHEELA_ATTACKS = [Attack(15, 95, "Bite"), Attack(20, 85, "Neck Hit"), Attack(25, 75, "Powerful Current")]

VESPERSAURUS_HEALTH = 110
VESPERSAURUS_DEFENSE = 5
VESPERSAURUS_SPEED = 75
VESPERSAURUS_ATTACKS = [Attack(20, 95, "Kick"), Attack(25, 85, "Jump Kick"), Attack(10, 100, "Claw")]

ICHTHYODECTES_HEALTH = 65
ICHTHYODECTES_DEFENSE = 5
ICHTHYODECTES_SPEED = 70
ICHTHYODECTES_ATTACKS = [Attack(5, 100, "Tail Hit"), Attack(10, 85, "Chomp"), Attack(20, 75, "Ultra Chomp")]

ANUROGNATHUS_HEALTH = 65
ANUROGNATHUS_DEFENSE = 10
ANUROGNATHUS_SPEED = 70
ANUROGNATHUS_ATTACKS = [Attack(10, 80, "Head Hit"), Attack(15, 80, "Wing Smack")]
# functions
def heal_20(user):
	user.health += 20
	if user.health > user.max_health:
		user.health = user.max_health
def heal_30(user):
	user.health += 30
	if user.health > user.max_health:
		user.health = user.max_health
def heal_40(user):
	user.health += 40
	if user.health > user.max_health:
                user.health = user.max_health
def heal_70(user):
	user.health += 70
	if user.health > user.max_health:
                user.health = user.max_health
def heal_100(user):
	user.health += 100
	if user.health > user.max_health:
                user.health = user.max_health
def heal_140(user):
	user.health += 140
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
PLAYER_ATTACKS_LEVEL_1 = [Attack(30, 95, "Punch"),Attack(50, 85, "Kick"),Attack(0, 100, "Cure", heal_20),Attack(65, 95, "Smash", damage_self_10),Attack(40, 100, "Laser")]
PLAYER_ATTACKS_LEVEL_3 = [Attack(40, 95, "Punch"),Attack(60, 85, "Kick"),Attack(0, 100, "Cure", heal_40),Attack(85, 95, "Smash", damage_self_20),Attack(50, 100, "Laser")]
PLAYER_ATTACKS_LEVEL_5 = [Attack(55, 95, "Punch"),Attack(75, 85, "Kick"),Attack(0, 100, "Cure", heal_70),Attack(110, 95, "Smash", damage_self_30),Attack(65, 100, "Laser")]
PLAYER_ATTACKS_LEVEL_7 = [Attack(70, 95, "Punch"),Attack(90, 85, "Kick"),Attack(0, 100, "Cure", heal_100),Attack(135, 95, "Smash", damage_self_40),Attack(80, 100, "Laser")]
PLAYER_ATTACKS_LEVEL_9 = [Attack(90, 95, "Punch"),Attack(115, 85, "Kick"),Attack(0, 100, "Cure", heal_140),Attack(160, 95, "Smash", damage_self_50),Attack(100, 100, "Laser")]

PENTACERATOPS_ATTACKS = [Attack(20, 90, "Horn Hit"), Attack(30, 80, "Charge", damage_self_10), Attack(10, 90, "Cure and Hit", heal_30)]
