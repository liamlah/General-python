# -*- coding: utf-8 -*-
#Created by Liam Jones 20/09/2018
#Designed to make it easier for me to find the floor for a particular apartment
#in the building I work at.
import xlrd
loc = (r'C:\Users\Admin\OneDrive\Documents\Name_apartment_database.xlsx')
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
def frontbuilding(): #Called if the apartment is below 11. The math based algorithms do not apply.
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
    residentname()


#functions for each floor plan section. Because there are two sides to the building, Some floors have three apartments, some two, and there are some floor numbers not named in the building (such as 13)
def between1144(): 
    global aptNo
    global floor
    floor = int(round(aptNo - 9)/3 +0.5) +1
    result()
        
def between4449():
    global aptNo
    global floor
    floor = int((aptNo)/3 +.5)
    result()
    
def between5053():
    global aptNo
    global floor
    floor = int((aptNo)/3 +.7)
    result()

def between5587():
    global aptNo
    global floor
    floor = int(round(aptNo - 50)/3 +0.5)
    result()
            
def between8893():
    global aptNo
    global floor
    floor = int((aptNo -42) /3 -.2)
    result()

def between9497():
    global aptNo
    global floor
    floor = int((aptNo - 42)/3)
    result()

def start(): #beginning. Takes input and passes to ifsandbuts function.
    global aptNo
    global compass
    print("-----------------------------------------------------------\nThis program will tell you which floor the apartment is on.")
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

def ifsandbuts(): #determines which function to call based on the floor plan of the section of building the apartment is in.
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
            residentname()
        elif aptNo > 54 and aptNo < 88:
            between5587()
        elif aptNo > 87 and aptNo < 94:
            between8893()
        elif aptNo > 93 and aptNo < 98:
            between9497()
        elif aptNo == 98:
            print("Apartment 98 is Floor 19, The penthouse, East wing\n")
            residentname()
        else:
            print("That Number is out of range. Please try again\n")
            start()

def result(): #prints out result of floor calculation along with apartment number and the wing.
    global sheet
    global compass
    global floor
    global aptNo
    aptNo = str(aptNo)
    floor = str(floor)
    compass = str(compass)
    print("Apartment %s is on floor %s and is in %s wing." %(aptNo, floor, compass))
    #sheet.cell_value(0,0)
    #resident =(sheet.row_values(int(aptNo),0))
    #print("Residents recorded at this address are: {} {} {}" .format(resident[1], resident[2], resident[3])) 
    residentname()

def residentname():
    global sheet
    global aptNo
    sheet.cell_value(0,0)
    resident =(sheet.row_values(int(aptNo),0))
    print("Resident(s) recorded at this address:\n{}\n{}\n{}\n\n" .format(resident[1], resident[2], resident[3]))
    start()

start()
