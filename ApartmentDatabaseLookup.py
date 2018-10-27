# -*- coding: utf-8 -*-
#Created by Liam Jones 27/10/2018
#Apartment database searcher. Links to editable spreadsheets, for quick lookup and cross reference of resident information
import xlrd
loc = (r'C:\Users\Admin\OneDrive\Documents\Name_apartment_database.xlsx')
wb = xlrd.open_workbook(loc)




def searchchoice(): # Menu 
    while True:
        print("-------------------------------------------------------------")
        lookupchoice = input("What information do you already have?\n\n1)Apt number\n2)Car rego\n3)Resident name\n>>>")
        if lookupchoice == '1':            
            aptsearch()   
        elif lookupchoice == '2':
            regosearch()
        elif lookupchoice == '3':
            namesearch()
        #elif lookupchoice == '4':
          #  floorsearch()
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
    nameinput = input("What is the name of the resident you wish to look up?\n>>>")
    nameinput = nameinput.capitalize()
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if nameinput == sheet.cell_value(row,col): 
                aptNo = row
                print(row)
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
"""
    
def sidechoice():
    sidechoice = int(input("Which side of the building are you looking for information on?\n1)East\n2)West")
    while True:
        if sidechoice == 1:
            westfloor()
            break
        if sidechoice == 2:
            eastfloor()
            break

def eastfloor():
    floorchoice = int(input("What Floor are you looking for information on in the west side?


def westfloor():                     
"""

searchchoice()
