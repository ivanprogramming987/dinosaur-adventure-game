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
COMPSOGNATHUS_ATTACKS = [Attack(10, 85, "Slash", None), Attack(20, 60, "Tail Swipe", None)]

TIANYULONG_HEALTH = 40
TIANYULONG_DEFENSE = 15
TIANYULONG_SPEED = 45
TIANYULONG_ATTACKS = [Attack(15, 80, "Bite", None), Attack(20, 60, "Tail Swipe", None), Attack(10, 100, "Scream", None)]

MICRORAPTOR_HEALTH = 20
MICRORAPTOR_DEFENSE = 5
MICRORAPTOR_SPEED = 85
MICRORAPTOR_ATTACKS = [Attack(5, 100, "Scream", None), Attack(10, 85, "Swoop", None)]

PENTACERATOPS_HEALTH = 165
PENTACERATOPS_DEFENSE = 10
PENTACERATOPS_SPEED = 55

# functions
def heal_30(user):
	user.health += 30
	if user.health > user.max_health:
		user.health = user.max_health
def heal_50(user):
	user.health += 50
	if user.health > user.max_health:
                user.health = user.max_health
def heal_80(user):
	user.health += 80
	if user.health > user.max_health:
                user.health = user.max_health
def heal_120(user):
	user.health += 120
	if user.health > user.max_health:
                user.health = user.max_health
def heal_160(user):
	user.health += 160
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
def damage_self_60(user):
	user.health -= 60


# variables with functions
PLAYER_ATTACKS_LEVEL_1 = [Attack(30, 95, "Punch", None),Attack(50, 85, "Kick", None),Attack(0, 100, "Cure", heal_30),Attack(55, 95, "Smash", damage_self_20),Attack(30, 100, "Laser", None)]
PLAYER_ATTACKS_LEVEL_3 = [Attack(40, 95, "Punch", None),Attack(60, 85, "Kick", None),Attack(0, 100, "Cure", heal_50),Attack(75, 95, "Smash", damage_self_30),Attack(40, 100, "Laser", None)]
PLAYER_ATTACKS_LEVEL_5 = [Attack(55, 95, "Punch", None),Attack(75, 85, "Kick", None),Attack(0, 100, "Cure", heal_80),Attack(100, 95, "Smash", damage_self_40),Attack(55, 100, "Laser", None)]
PLAYER_ATTACKS_LEVEL_7 = [Attack(70, 95, "Punch", None),Attack(90, 85, "Kick", None),Attack(0, 100, "Cure", heal_120),Attack(125, 95, "Smash", damage_self_50),Attack(70, 100, "Laser", None)]
PLAYER_ATTACKS_LEVEL_9 = [Attack(90, 95, "Punch", None),Attack(115, 85, "Kick", None),Attack(0, 100, "Cure", heal_160),Attack(150, 95, "Smash", damage_self_60),Attack(90, 100, "Laser", None)]

PENTACERATOPS_ATTACKS = [Attack(25, 90, "Horn Hit", None), Attack(45, 75, "Charge", damage_self_20), Attack(5, 90, "Cure and Hit", heal_30)]
