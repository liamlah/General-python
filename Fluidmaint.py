import random

def menu():
    print("Online fluid replacement and maintenance trainer.\n")
    while True:        
        try:
            menuchoice = int(input("Choose your difficulty level:\nPress 1 for fluid maintenance practice only (basic4:2:1)\nPress 2 for maintenance and replacement practice\n\n#"))
            break        
        except ValueError:
            print("please choose a number")
    if menuchoice == 1:
        print('You have chosen maintenance practice, enter 0 at any time to return to the menu.\n')
        fluidmaint()
    elif menuchoice == 2:
        print('You have chosen maintenance and replacement practice, enter 0 at any time to return to the menu.\n')
        fluidmaintreplace()
    else:
        print("please select 1 or 2")
         

def fluidmaint():
    ptweight = random.randint(1,50) #adjust the second number if you want a different weight limit
    if ptweight >19:
        extraweight = ptweight - 20
        maintrate =  extraweight + 60
    elif 9 < ptweight < 20:
        extraweight = ptweight - 10
        maintrate = extraweight * 2 + 40
    else:
        maintrate = ptweight * 4
    while True:        
        try:
            questionbox = int(input("What is the maintenance rate in ml/hr for a %skg patient?\n$"%(ptweight)))
            break        
        except ValueError:
            print("put an integer and try again") 
    if questionbox == maintrate:
        print("CORRECT, the maintenance rate is: %sml/hr\n"%(maintrate))
        fluidmaint()
    elif questionbox == 0:
        menu()
    else:
        print("WRONG the maintenance rate is: %sml/hr\n"%(maintrate))
        fluidmaint()

def fluidmaintreplace():
    ptweight = random.randint(1,50) #adjust the second number if you want a different weight limit
    ptdehydration = random.randint(1,12)
    hrday = ["*hourly*","*daily*"]
    hoursordays = hrday[random.randint(0,1)]
    if hoursordays =='*daily*':
        rehydrationoptions =[24,48]
        rehydrotime = rehydrationoptions[random.randint(0,1)]
    else:
        rehydrationoptions = [4,24,48]
        rehydrotime = rehydrationoptions[random.randint(0,2)]
    if ptweight >19:
        extraweight = ptweight - 20
        maintrate =  extraweight + 60
    elif 9 < ptweight < 20:
        extraweight = ptweight - 10
        maintrate = extraweight * 2 + 40
    else:
        maintrate = ptweight * 4
    totalreplace = ptweight *(ptdehydration*10) 
    hourlyreplace = totalreplace/rehydrotime
    if hoursordays == '*hourly*':
        finalanswer = hourlyreplace + maintrate
        finalanswer = int(finalanswer)
        rate ="hour"
    elif hoursordays == '*daily*':
        finalanswer = (hourlyreplace*24) + (maintrate*24)
        finalanswer = int(finalanswer)
        rate ="day"
    while True:        
        try:
            questionbox = int(input("What is the {} combined maintenance and replacement rate in ml for a {} percent dehydrated patient who weighs {}kg to be rehydrated over {} hours?\n$" .format(hoursordays, ptdehydration, ptweight, rehydrotime)))
            break        
        except ValueError:
            print("put an integer and try again") 
    if int(finalanswer) <= questionbox <= 1+int(finalanswer):
        print("CORRECT, the fluid amount is: {}ml/{}\nworking: the hourly rate is {}ml/hr and maintenance rate is {}ml/hr\n".format(finalanswer,rate,int(hourlyreplace),int(maintrate)))
        fluidmaintreplace()
    elif questionbox == 0:
        menu()
    else:
        print("WRONG the fluid amount is: {}ml/{}\nworking: the hourly rate is {}ml/hr and maintenance rate is {}ml/hr\n".format(finalanswer,rate,int(hourlyreplace),int(maintrate)))
        fluidmaintreplace()


menu()



