from attack import *

PLAYER_ATTACKS_LEVEL_1 = [
Attack(30, 85, "Punch", None),
Attack(50, 65, "Kick", None),
Attack(0, 100, "Cure", heal_30()),
Attack(55, 85, "Smash", damage_self_20()),
Attack(30, 100, "Laser", None) # all "Laser" attacks make you lose a laser. that is in player's code
]
PLAYER_ATTACKS_LEVEL_3 = [
Attack(40, 85, "Punch", None),
Attack(60, 65, "Kick", None),
Attack(0, 100, "Cure", heal_50()),
Attack(75, 85, "Smash", damage_self_30()),
Attack(40, 100, "Laser", None)
]
PLAYER_ATTACKS_LEVEL_5 = [
Attack(55, 85, "Punch", None),
Attack(75, 65, "Kick", None),
Attack(0, 100, "Cure", heal_80()),
Attack(100, 85, "Smash", damage_self_40()),
Attack(55, 100, "Laser", None)
]
PLAYER_ATTACKS_LEVEL_7 = [
Attack(70, 85, "Punch", None),
Attack(90, 65, "Kick", None),
Attack(0, 100, "Cure", heal_120()),
Attack(125, 85, "Smash", damage_self_50()),
Attack(70, 100, "Laser", None)
]
PLAYER_ATTACKS_LEVEL_9 = [
Attack(90, 85, "Punch", None),
Attack(115, 65, "Kick", None),
Attack(0, 100, "Cure", heal_160()),
Attack(150, 85, "Smash", damage_self_60()),
Attack(90, 100, "Laser", None)
]

PLAYER_LEVEL = 1
PLAYER_SPEED = 50
PLAYER_DEFENSE = 10
PLAYER_HEALTH = 100
PLAYER_LASERS = 10

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
