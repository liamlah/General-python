# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:33:49 2018

@author: Liam
"""

#Monty hall statistical generator. Designed to run the simluation 100 times as either switching or staying. According to theory, result should be 66% wins for switching, and 33% for staying.
import random

def start():
    global didswitch
    global wincounter
    global gamecounter
    wincounter = 0
    gamecounter = 0
    print("\nThis program will run a simulation of the Monty Hall problem 100 times, and shows the percentage of wins depending on whether you choose to switch or to stay")
    gamechoice = input(str("Do you want to switch? Y for Yes, N for No.\n>>>"))
    gamechoice = gamechoice.lower()
    if gamechoice == "y":
        didswitch = 1
    elif gamechoice =="n":
        didswitch = 0
    else:
        start()
    maingenerator()

def maingenerator():
    global contestantchoice
    global montyshows
    global didswitch
    global windoor
    windoor = random.randint(1,3)
    contestantchoice = random.randint(1,3)

    while True: #makes sure Monty doesn't choose the winner or the same as contestant.
        montyshows = random.randint(1,3)
        if montyshows == contestantchoice:
            continue
        if montyshows == windoor:            
            continue
        else:
            break
    if didswitch == 1:
        switchyes()
    elif didswitch == 0:
        switchno()


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
        print(str(gamecounter) +".Win!")
        maingenerator()
    elif gamecounter < 99:
        gamecounter += 1
        print(str(gamecounter) +".Lose!")
        maingenerator()
    elif gamecounter >= 99:
        printout()
        

def printout():
    global didswitch
    global gamecounter
    global wincounter
    winpercent = wincounter/gamecounter
    print("You won "+ str(round(winpercent, 2))+ "% of the time by " + str(switchanswer))
    playagain = input("Press enter to play again, or press any key to exit.\n>>>")
    if playagain == "":
        start()
    else:
        print("Goodbye")
start()

