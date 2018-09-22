#Created by Liam Jones 09/2018
#Designed to make it easier for me to find the floor for a particular apartment
#in the building I work at.

def frontbuilding(): #if the number is below 11
    global aptNo
    firstfloor = [8,7,3,2]
    secondfloor = [10,9,5,4]
    westpo = [7,8,9,10]
    eastpo = [2,3,4,5]
    if aptNo in westpo:
        podcompass = "west"
    elif aptNo in eastpo:
        podcompass = "East"
    if aptNo in firstfloor:
        print("Floor 1, at the %s podium.\n" %(podcompass))
    elif aptNo in secondfloor:
        print("Floor 2, at the %s podium.\n" %(podcompass))
    elif aptNo == 1:
        print("East podium, the Restaurant.\n")
    elif aptNo == 6:
        print("West podium, Tan Lawyers.\n")
    start()

def between1144(): #algorithm for floors 11 between 44 where  
    global aptNo
    global floor
    floor = int(round(aptNo - 9)/3 +0.5) +1
    #print(str(floor))
    result()
        
def between4449():
    global aptNo
    global floor
    floor = int((aptNo)/3 +.5)
    #print(str(floor))
    result()
    
def between5053():
    global aptNo
    global floor
    floor = int((aptNo)/3 +.7)
    #print(str(floor))
    result()

def between5587():
    global aptNo
    global floor
    floor = int(round(aptNo - 50)/3 +0.5)
    #print(str(floor))
    result()
            
def between8893():
    global aptNo
    global floor
    floor = int((aptNo -42) /3 -.2)
    #print(str(floor))
    result()

def between9497():
    global aptNo
    global floor
    floor = int((aptNo - 42)/3)
    #print(str(floor))
    result()

def start():
    global aptNo
    global compass
    print("This program will tell you which floor the apartment is on.")
    while True:
        try:
            aptNo = int(input("What apartment number are you looking for?\n>>>"))
        except ValueError:
            print("That's not an apartment number. Try again.")
            continue
        else: 
            break 
        
    if aptNo > 10 and aptNo < 55:
        compass = "West"
    else:
        compass = "East"


    ifsandbuts()

def ifsandbuts():
    while True:
        if aptNo < 11 and aptNo > 0:
            frontbuilding()
        elif aptNo > 10 and aptNo < 44:
            between1144()
        elif aptNo > 43 and aptNo < 50:
            between4449()
        elif aptNo > 49 and aptNo < 54:
            between5053()
        elif aptNo == 54:
            print("Apartment 54 is Floor 19, the Penthouse, West wing.\n")
            start()
        elif aptNo > 54 and aptNo < 88:
            between5587()
        elif aptNo > 87 and aptNo < 94:
            between8893()
        elif aptNo > 93 and aptNo < 98:
            between9497()
        elif aptNo == 98:
            print("Apartment 98 is Floor 19, The penthouse, East wing\n")
            start()
        else:
            print("That Number is out of range. Please try again\n")
            start()
def result():
    global compass
    global floor
    global aptNo
    aptNo = str(aptNo)
    floor = str(floor)
    compass = str(compass)
    print("Apartment %s is on floor %s and is in %s wing.\n\n\n" %(aptNo, floor, compass))
    start()
start()
