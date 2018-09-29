# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:33:49 2018

@author: Liam
"""

#Monty hall statistical generator
import random
"""Things to do: Have 3 choices.
Random number generates a positive on one door.
select door
Monty selects a losing door that you didn't choose.
program asks you to choose.

or program does this automatically without user input, and then displays results.
"""
def start():
    global didswitch
    global wincounter
    global gamecounter
    wincounter = 0
    gamecounter = 0
    didswitch = "null"
    print("\nThis program will run a simulation of the Monty Hall problem 100 times, and show the percentage of wins depending on whether you choose to switch or to stay")
    gamechoice = input(str("Do you want to switch? Y for Yes, N for No.\n>>>"))
    gamechoice = gamechoice.lower()
    if gamechoice == "y":
        didswitch = 1
    else:
        didswitch = 0
    maingenerator()

def maingenerator():
    global contestantchoice
    global montyshows
    global didswitch
    global windoor
    doors = {1:'loser', 2:'loser', 3:'loser'}
    contestantdoors = {1:'loser', 2:'loser', 3:'loser'}
    contestantdoors = {1:'loser', 2:'loser', 3:'loser'}
    windoor = random.randint(1,3)
    #print(str(windoor)  + "winner")

    doors[windoor] = 'winner'
    contestantdoors[windoor] = 'winner'
    #print(doors)

    contestantchoice = random.randint(1,3)
    contestantdoors = {1:'loser', 2:'loser', 3:'loser'}
    contestantdoors[contestantchoice] = 'chosen'
    #print(str(contestantchoice) + "chosen door")

    while True: #makes sure Monty doesn't choose the winner or the same as contestant.
        montyshows = random.randint(1,3)
        #print(str(montyshows) + "door monty opened")
        if montyshows == contestantchoice:
           # print("he opened the same door the contestant chose")
            continue
        if montyshows == windoor:
            #print("he opened the winning door")
            continue
        else:
            break
    if didswitch == 1:
        switchyes()
    elif didswitch == 0:
        switchno()
    else:
        print("something is wrong with the choice")

        
    #would you like to switch? yes
def switchyes():
    global newchoice
    global switchanswer
    switchanswer = "switching."
    while True: #changes choice to unopened door
        newchoice = random.randint(1,3)
        if newchoice == montyshows:
            continue
        if newchoice == contestantchoice:
            continue
        else:
            break
    results()

def switchno():
    global newchoice
    global switchanswer
    switchanswer = "not switching."
    newchoice = contestantchoice
    results()


def results():
    global newchoice
    global gamecounter
    global wincounter
    if newchoice == windoor:
        wincounter += 100
        gamecounter += 1
        print(str(gamecounter) +"Win!")
        maingenerator()
    elif gamecounter < 99:
        gamecounter += 1
        print(str(gamecounter) +"lose")
        maingenerator()
    elif gamecounter >= 99:
        printout()
        

def printout():
    global didswitch
    global gamecounter
    global wincounter
    winpercent = wincounter/gamecounter
    print("You won "+ str(round(winpercent, 2))+ "% of the time by " + str(switchanswer))#%s." %(winpercent, switchanswer))
    playagain = input("Press enter to play again, or press any key to exit.\n>>>")
    if playagain == "":
        start()
    else:
        print("Goodbye")
start()

