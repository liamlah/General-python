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
#would you like to switch? yes

while True: #changes choice to unopened door
    newchoice = random.randint(1,3)
    if newchoice == montyshows:
        continue
    if newchoice == contestantchoice:
        continue
    else:
        break

if newchoice == windoor:
    print("you won")
else:
    print("you lost")
#put these into functions so you can repeat it x number of times, or have them stay
