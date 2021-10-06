import os
import random


random.seed()



# Creates the player's cards 
basicPress = {
    "name": "Press Attack (Basic)", 
    "type": "Press", 
    "condition": 8, 
    "SPDrain": 0, 
    "hitDamage": 4
}
strikeHead = {
    "name": "Strike Head", 
    "type": "Press", 
    "condition": 12, 
    "SPDrain": 10, 
    "hitDamage": 8
}

smashDefenses = {
    "name": "Smash Defenses", 
    "type": "Press", 
    "condition": 12, 
    "SPDrain": 12, 
    "hitDamage": 14
}


sneakAttack = {
    "name": "Sneak Attack", 
    "type": "Press", 
    "condition": 12, 
    "SPDrain": 8, 
    "hitDamage": 8
}

basicAttack = {
    "name": "Basic Attack", 
    "type": "Attack", 
    "condition": 8, 
    "SPDrain": 0, 
    "hitDamage": 2
}

basicDefend = {
    "name": "Basic Defend", 
    "type": "Defend", 
    "condition": 8, 
    "SPDrain": 0, 
    "defendDamage": 2
}
block = {
    "name": "Block", 
    "type": "Defend", 
    "condition": 12, 
    "SPDrain": 10, 
    "defendDamage": 8
}

basicEvade = {
    "name": "Basic Evade", 
    "type": "Evade", 
    "condition": 8, 
    "SPDrain": 1, 
    "defendDamage": 4
}


fighterDeck = [strikeHead, block, smashDefenses, basicPress, basicAttack, basicDefend, basicEvade]
rogueDeck = [strikeHead, block, sneakAttack, basicPress, basicAttack, basicDefend, basicEvade]

# Stat blocks for Characters
player = {
    "name": "Player",
    "class": "Fighter",
    "hp": 50,
    "sp": 25,
    "agi": 1,
    "str": 3,
    "defendTemp": 0,
    "deck": fighterDeck
}

enemy = {
    "name": "Enemy",
    "class": "Rogue",
    "hp": 50,
    "sp": 25,
    "agi": 3,
    "str": 1,
    "defendTemp": 0,
    "deck": rogueDeck
}




# Placed in definition for future expansion
"""
def calculateTurnOrder(charAttack):
    if charAttack.attackType == "Press":
        return 2
    if charAttack.attackType == "Attack":
        return 0
    if charAttack.attackType == "Defend":
        return 1
    if charAttack.attackType == "Evade":
        return 2
"""

# Future: Will only display options player can still do with current SP
def choosePlayerAction():
    attackChoice = None
    while attackChoice == None:
        counter = 1
        for x in player["deck"]:
            print(counter, end = ":  " + x["name"])
            print("")
            counter += 1
        attackInput = player["deck"][int(input("Which action would you like to take?"))-1]
        print(attackInput)
        if attackInput == None:
            print("Invalid input. Please select one of the available moves.")
        #elif attackInput is out of range
        #elif attackInput it blank/not a number
        elif attackInput["SPDrain"] >= player["sp"]:
            print("You do not have the Stamina to perform that action. Please select a different move.")
        else:
            attackChoice = attackInput
    return attackChoice


def resolveAction(actor, action, otherCharacter):
    totalDamage = 0
    if ((action["type"] == "Press") or (action["type"] == "Evade")):
        hit = isAHit(actor["agi"], action["condition"])
    else:
        hit = isAHit(actor["agi"], action["condition"])
    if hit == True:
        if ((action["type"] == "Press") or (action["type"] == "Attack")):
            print("It is a hit!")
            totalDamage = (actor["str"] + action["hitDamage"] - otherCharacter["defendTemp"])
            if totalDamage > 0:
                otherCharacter["hp"] -= totalDamage
            print("Damage dealt =  ", end = str(totalDamage))
            print("")
        elif action["type"] == "Defend":
            print(f'{actor["name"]} defended successfully.')
            actor["defendTemp"] = action["defendDamage"]
            print(f'{actor["name"]} is defended from {actor["defendTemp"]} damage')
        elif action["type"] == "Evade":    
            print(f'{actor["name"]} evaded successfully.')
            actor["defendTemp"] = action["defendDamage"] + actor["agi"]
            print(f'{actor["name"]} is evading from {actor["defendTemp"]} damage')
    else:
        print("The action missed!")


def chooseCards(deck):
    return deck[1]


def chooseEnemyAction():
    attackChoice = None
    while attackChoice == None:
        option = random.randint(1, len(enemy["deck"]))
        if enemy["deck"][(option-1)]["SPDrain"] <= enemy["sp"]:
            attackChoice = enemy["deck"][(option-1)]
    return attackChoice


def checkGameOver():
    if (player["hp"] > 0 and enemy["hp"] > 0):
        return False
    else:
        return True

def isAHit(mod, hitCondition):
    if mod == None:
        mod = 0
    rolld20 = random.randint(1, 20) + mod
    if rolld20 >= hitCondition:
        return True
    else:
        return False

# Clears the screen
os.system('cls||clear')
while (player["hp"] > 0 and enemy["hp"] > 0):
    # Clears the screen
    os.system('cls||clear')
    # Displays current Health and SP amounts
    player["sp"] += 3
    enemy["sp"] += 3
    print(f'{player["name"]} has {player["hp"]} health and {player["sp"]} stamina remaining.')
    print(f'{enemy["name"]} has {enemy["hp"]} health and {enemy["sp"]} stamina remaining.')
    # Player chooses an attack from given options
    player["defendTemp"] = 0
    playerAction = choosePlayerAction()
    print(f'{player["name"]} uses {playerAction["name"]}')
    resolveAction(player, playerAction, enemy)
    player["sp"] -= playerAction["SPDrain"]
    if checkGameOver() == True:
        break
    # Enemy chooses a random attack from options
    enemy["defendTemp"] = 0
    enemyAction = chooseEnemyAction()
    print(f'{enemy["name"]} uses {enemyAction["name"]}')
    resolveAction(enemy, enemyAction, player)
    enemy["sp"] -= enemyAction["SPDrain"]
    print(f'{player["name"]} has {player["hp"]} health and {player["sp"]} stamina remaining.')
    print(f'{enemy["name"]} has {enemy["hp"]} health and {enemy["sp"]} stamina remaining.')
    if checkGameOver() == True:
        break
    input("Press any key to continue.")
if enemy["hp"] <= 0:
    print("You have defeated the enemy. Congratulations!")
elif player["hp"] <= 0:
    print("You were defeated. Better luck next time!")
