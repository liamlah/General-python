# Battle calculator for Daniel's DnD style game.
# Author: Liam, created on 12/10/2018 in python 3.7.0
import random
whichround = 0

def inputs(): # function takes your and the enemy's character stats to begin battle
    global yourhealth
    global yourattack
    global enemyhealth
    global enemyattack
    global enemyname
    enemyname = str(input("What is the name of your enemy?\n>>>"))
    enemyname = enemyname.capitalize()
    #subsequent set of loops validates stat inputs as integers
    while True:        
        try:
            enemyhealth = int(input("How much health does {} have?\n>>>".format(enemyname)))
            break        
        except ValueError:
            print("It needs to be a whole number. Try again.")

    while True:        
        try:
            enemyattack = int(input("How much damage does {} do?\n>>>".format(enemyname)))
            break        
        except ValueError:
            print("It needs to be a whole number. Try again.")
            
    while True:
        try:
            yourhealth = int(input("How much health do you have?\n>>>"))
            break        
        except ValueError:
            print("It needs to be a whole number. Try again.")

    while True:
        try:
            yourattack = int(input("How much damage do you do?\n>>>"))
            break        
        except ValueError:
            print("It needs to be a whole number. Try again.")
    
    battlegenhuman() #assumes player character initiated combat



def battlegenhuman(): #generates round based battle stats for the player character
    global whichround
    global yourattackpercent
    global yourdodgepercent
    global totalattackpercent
    global enemydodgepercent
    whichround += 1
    print("\nRound {}\n" .format(whichround))
    yourattackpercent = random.randint(0,10) #attack and 'dodge' are randomly generated as values between 0 and 10
    enemydodgepercent = random.randint(0,10) 
    totalattackpercent = (yourattackpercent - enemydodgepercent) #The dodge is subtracted from the attack, then the remaining is multiplied by the characters base attack stat 
    if totalattackpercent <1: # If the dodge is greater than the attack, then damage is nothing. This line prevents unnecessary calling of results function.
        print("You rolled {}0% damage and {} dodged {}0%" .format(yourattackpercent, enemyname, enemydodgepercent))
        print("You did no damage")
        print("It is {}'s turn to attack" .format(enemyname))
        stopper = input("Press enter to continue...\n")
        battlegenNPC() # moves on to NPC's turn if no further calculations are required.
    else:
        resultshuman()



def resultshuman(): # provides results of the attack, displays the stats to the player before moving on.
    global yourattackpercent
    global enemydodgepercent
    global enemyhealth
    global totalattackpercent
    global realattack
    global yourattack
    global enemyname
    realattack = yourattack * totalattackpercent/10 
    print("You rolled {}0% of your total attack, and {} dodged {}0% of it." .format(yourattackpercent, enemyname, enemydodgepercent))
    print("You inflicted a damage of {} hitpoints on {}." .format(realattack, enemyname))
    enemyhealth = enemyhealth - realattack
    print("{} now has a total of {} hitpoints" .format(enemyname, enemyhealth))
    if enemyhealth > 0: # if health reaches 0, battle is terminated and winner is declared
        stopper = input("Press enter to continue...\n") #This is here to provide pacing to the battle. Allowing the player or DM to intervene.
        battlegenNPC()
    else:
        print("You have defeated {}!".format(enemyname))

def battlegenNPC(): # same as player generator, but for the NPC
    global enemyattackpercent
    global enemydodgepercent
    global totalenemyattackpercent
    global yourdodgepercent
    global enemyname
    enemyattackpercent = random.randint(0,10)
    yourdodgepercent = random.randint(0,10)
    totalenemyattackpercent = (enemyattackpercent - yourdodgepercent)
    if totalenemyattackpercent <1:
        print("{} rolled {}0% damage and you dodged {}0%." .format(enemyname,enemyattackpercent, yourdodgepercent))
        print("{} did no damage." .format(enemyname))
        print("It is your turn to attack.")
        stopper = input("Press enter to continue...")
        battlegenhuman()
    else:
        resultsNPC()

def resultsNPC():  # same as player results but for the NPC
    global enemyattackpercent
    global yourdodgepercent
    global yourhealth
    global totalenemyattackpercent
    global realenemyattack
    global enemyattack
    global enemyname
    realenemyattack = enemyattack * totalenemyattackpercent/10 
    print("{} rolled {}0% of their total attack, and you dodged {}0% of it." .format(enemyname, enemyattackpercent, yourdodgepercent))
    print("You have receieved a damage of {} hitpoints from {}." .format(realenemyattack, enemyname))
    yourhealth = yourhealth - realenemyattack
    print("You now have a total of {} hitpoints." .format(yourhealth))
    if yourhealth > 0: # if health reaches 0, battle is terminated and winner is declared
        stopper = input("Press enter to continue...\n")
        battlegenhuman()
    else:
        print("You have have been slain by {}!".format(enemyname))
        
inputs()


