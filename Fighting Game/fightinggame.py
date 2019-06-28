#!/usr/bin/python3

from random import randint

def playerHeal():
    return randint(player['minHeal'],player['maxHeal'])

def monsterAttack():
    return randint(monster['minAttack'],monster['maxAttack'])

gamePlaying = True
# Init game
player = {'name':'','attack':8,'minHeal':5,'maxHeal':15,'health':100}
monster = {'name':'The Best Ever','minAttack':0,'maxAttack':20,'health':100}
print("What is your name stranger?")
print()
player['name'] = input()
print()
print("Your name is " + player['name'])
print()
print("The monster is " + monster['name'])
print()
print()
print("DUEL!")
print("-"*30)
print()

while gamePlaying == True:
    
    # round start
    roundCount = 1
    print("Start round " + str(roundCount))
    print("What will you do next?")
    print("1) Attack")
    print("2) Heal")
    print("3) Run")
    print("-"*30)
    playerChoice = input()

    # Turn start
    if playerChoice == '1':
        monster['health'] = monster['health'] - player['attack']
        print(monster['name'] + "'s health is now " + str(monster['health']))
        player['health'] = player['health'] - monsterAttack()
        print(player['name'] + "'s health is now " + str(player['health']))
        print("-"*30)
    
    elif playerChoice == '2':
        print(monster['name'] + "'s health is now " + str(monster['health']))
        player['health'] += playerHeal()
        player['health'] = player['health'] - monsterAttack()
        print(player['name'] + "'s health is now " + str(player['health']))
        print("-"*30)

    elif playerChoice == '3':
        print(player['name'] + " have ran.")
        exit()

    else:
        print()
        print("-"*30)
        print("Please enter 1,2 or 3.")
        print("-"*30)
        print()

    winnerReward = '''
    (”)….(”)
    ( ‘ o ‘ )
    (”)––––(”)
    (””’)-(””’)
    '''

    loserPunishment = '''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄██████▄
▒▒▒▒▒▒▒▒▒▒▄▄████████████▄
▒▒▒▒▒▒▄▄██████████████████
▒▒▒▄████▀▀▀██▀██▌███▀▀▀████
▒▒▐▀████▌▀██▌▀▐█▌████▌█████▌
▒▒█▒▒▀██▀▀▐█▐█▌█▌▀▀██▌██████
▒▒█▒▒▒▒████████████████████▌
▒▒▒▌▒▒▒▒█████░░░░░░░██████▀
▒▒▒▀▄▓▓▓▒███░░░░░░█████▀▀
▒▒▒▒▀░▓▓▒▐█████████▀▀▒
▒▒▒▒▒░░▒▒▐█████▀▀▒▒▒▒▒▒
▒▒░░░░░▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒
▒▒▒░░░░░░░░▒▒
    '''

    # End game
    if monster['health'] <= 0:
            print(winnerReward)
            print("You won the round " + player['name'])
            roundCount += 1
    
    elif player['health'] <= 0:
            print(loserPunishment)
            print("You lost to " + monster['name'])
            gamePlaying = False

    else:
        continue
