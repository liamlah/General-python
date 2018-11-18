# -*- coding: utf-8 -*-
#Created by Liam Jones 27/10/2018
#Apartment database searcher. Links to editable spreadsheets, for quick lookup and cross reference of resident information
import datetime
now = datetime.datetime.now()


log = open('adlogfile.txt', 'a')
log.write(str(now)+ '\n')
log.close()

import xlrd
loc = (r'C:\Users\Admin\OneDrive\Documents\Name_apartment_database.xlsx')
wb = xlrd.open_workbook(loc)
print("This program allows you to search information relating to Westralian residents,\nsuch as apartment numbers, car registration or names.\n\n")


def searchchoice(): # Menu 
    while True:
        print("-------------------------------------------------------------")
        lookupchoice = input("What information do you already have?\n\n1)Apt number\n2)Car rego\n3)Resident name\n4)Floor Number\n>>>")
        if lookupchoice == '1':            
            aptsearch()   
        elif lookupchoice == '2':
            regosearch()
        elif lookupchoice == '3':
            namesearch()
        elif lookupchoice == '4':
            floorsearch()
        else:
            print("please make a choice between 1 and 3!\n")


def aptsearch(): # search by apartment. Returns floor, names and rego
    aptNo = 0
    while True:
        try:
            aptNo = int(input("What apartment are you looking for details for?\n>>>"))
            break
        except ValueError:
            print("Only integers between 1 and 98 are valid. Try again.")
        if aptNo > 99 or aptNo < 1:
            print("Only integers between 1 and 98 are valid. Try again.")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    regosheet = wb.sheet_by_index(1)
    resident =(sheet.row_values(int(aptNo),0))
    rego =(regosheet.row_values(int(aptNo),0))
    if aptNo != 1 and aptNo !=6 and aptNo !=54 and aptNo !=98:
        resident[4] = int(resident[4])
    print("\nApartment {} is on floor {} of {}." .format(aptNo, resident[4], resident[5]))
    if resident[1] != '':
        print("Resident(s) recorded at this address:\n{}\n{}\n{}\n\n" .format(resident[1], resident[2], resident[3]))
    elif resident[1] == '':
        print("Apartment is vacant, or resident information has not yet been filled.\n")
    if rego[1] != '':
        print("Vehicle 1): {}. Registration: {}" .format(rego[2], rego[1]))
    if rego[3] !='':
        print("Vehicle 2): {}. Registration: {}\n" .format(rego[4], rego[3]))

def regosearch(): #Car registration search, returns model of car, apartment number, floor, and residents
    regoinput = input("What is the car registration number? Input numbers and letters without spaces, search is not case sensitive.\n>>>")
    regoinput = regoinput.upper()
    aptNo =''
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    regosheet = wb.sheet_by_index(1)
    for row in range(regosheet.nrows):
        for col in range(regosheet.ncols):
            if regosheet.cell_value(row,col) == regoinput:
                aptNo = row
                print(col)
                car = col + 1
                column = col
    if aptNo == '':
        print("No vehicle with that registration has been recorded.")
        searchchoice()
    resident =(sheet.row_values(int(aptNo),0))
    rego =(regosheet.row_values(int(aptNo),0))
    if aptNo != 1 and aptNo !=6 and aptNo !=54 and aptNo !=98:
        resident[4] = int(resident[4])
    print("The {}, with registration {} belongs to resident of apartment {}, on floor {} of {}.\n" .format(rego[car] ,rego[column], int(aptNo), resident[4], resident[5]))
    if resident[1] != '':
        print("Resident(s) recorded at this address:\n{}\n{}\n{}\n\n" .format(resident[1], resident[2], resident[3]))
    elif resident[1] == '':
        print("Apartment is vacant, or resident information has not yet been filled.\n")                                                                    
                

def namesearch(): #Searches by name, - Needs to be improved for partial string matches
    aptNo = ''
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    regosheet = wb.sheet_by_index(1)
    while True:
        nameinput = input("What is the name of the resident you wish to look up?\n>>>")
        if nameinput !="":
            break
    nameinput = nameinput.capitalize()
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if nameinput == sheet.cell_value(row,col): 
                aptNo = row
                #print(row)
    if aptNo == '':
        print("No resident with that name has been recorded.")
        searchchoice()
    resident =(sheet.row_values(int(aptNo),0))
    rego =(regosheet.row_values(int(aptNo),0))
    if aptNo != 1 and aptNo !=6 and aptNo !=54 and aptNo !=98:
        
        resident[4] = int(resident[4])
    print("A resident by the name of {} lives in apartment {}, on floor {} of {}.\n" .format(nameinput, aptNo, resident[4], resident[5]))
    if rego[1] != '':
        print("Vehicle 1): {}. Registration: {}" .format(rego[2], rego[1]))
    if rego[3] !='':
        print("Vehicle 2): {}. Registration: {}\n" .format(rego[4], rego[3]))


#search by floor, probably not necessary

    
def floorsearch():
    westfloors = { 2: '11,12,13', 3: '14,15,16', 4: '17,18,19', 5: '20,21,22', 6:'23,24,25', 7:'26,27,28.', 8:'29,30,31', 9:'32,33,34', 10:'35,36,37', 11:'38,39,40', 12:'41,42,43', 15:'44,45,46', 16:'47,48,49', 17:'50,51', 18:'52,53', 19:'54',}
    eastfloors ={2: '55,56,57', 3: '58,59,60', 4:'61,62,63', 5:'64,65,66', 6: '67,68,69', 7: '70,71,72', 8: '73,74,75', 9: '76,77,78', 10: '79,80,81', 11: '82,83,84', 12: '85,86,87', 15: '88,89,90', 16: '91,92,93', 17: '94,95', 18:'96,97', 19:'98',}
    while True:
        try:
            sidechoice = int(input("Which part of the building are you looking for information on?\n1)East\n2)West\n3)Podium\n>>>"))
            break
        except ValueError:
            print("Please make a valid selection.\n")

    while True:
        if sidechoice <1 or sidechoice >3:
            print("Please select from East, West or Podium.")
            floorsearch()
        elif sidechoice == 3:
            print("East podium has recipe #1 on Ground floor, #2 and #3 on floor 1, with #4 and #5 on floor 2.\nWest podium has Tan Lawyers #6 on Ground floor, #7 and #8 on floor 1, with #9 and #10 on floor 2.\n")
            furtherinfo()
            return
        else:
            break
    while True:
        try:
            sidefloor = int(input("Which floor are you looking for? (2-19)\n>>>"))
            if sidechoice == 2:  
                print("Apartments on floor {} of the west building are {}.\n ".format (sidefloor, westfloors[sidefloor]))
                furtherinfo()
                break
            elif sidechoice == 1:
                print("Apartments on floor {} of the East building are {}.\n ".format (sidefloor, eastfloors[sidefloor]))
                furtherinfo()
                break
        except KeyError:
            print("Such Floor does not exist.\n")
        except ValueError:        
            print("Such floor does not exist.\n")

def furtherinfo():
    while True:
        doapartment = input("Do you want to do a further search on one of these apartments?\n1)Yes\n2)No\n>>>")
        if doapartment == '1':
            aptsearch()
            break
        if doapartment == '2':
            searchchoice()
            break
        else:
            print("Make a valid selection, 1 or 2.")
            
                       



searchchoice()
