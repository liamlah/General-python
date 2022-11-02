import random
print("Simple fluid replacement and maintenance trainer.\n")
def menu():
    while True:        
        try:
            menuchoice = int(input("Choose your difficulty level:\nPress 1 for fluid maintenance practice only (basic 4:2:1)\nPress 2 for maintenance and replacement practice\nPress 3 for instructions\n\n#"))
            break        
        except ValueError:
            print("***Please choose a number***\n")
    if menuchoice == 1:
        print("You have chosen maintenance practice, enter 0 at any time to return to the menu.\n")
        fluidmaint()
    elif menuchoice == 2:
        print('You have chosen maintenance and replacement practice, enter 0 at any time to return to the menu.\nIf you end up with a decimal, round down to the nearest integer.\n')
        fluidmaintreplace()
    elif menuchoice == 3:
        
        print("\n+------INSTRUCTIONS-------+")
        print("MAINTENANCE: 4:2:1 algorithm for maintenance fluids is 4ml/kg of bodyweight/hr for the first 10kg an addional 2ml/kg/hr for every kilo between 11 and anď 20, then 1ml/kg/hr for each additional kilo.")
        print("\nREPLACEMENT: Volume loss is represented as a percentage of dehydration. E.g if a 12kg child is 5% dehydrated, we assume 1kg of bodyweight == 1 litre of fluid. So we need to replace 12kg x 0.05, which is 600ml.")
        print("Answering the rest of the question will require paying attention to the periods over which fluids are replaced.")
        print("+-------------------------+\n")
        menu()
    else:
        print("***Please select 1 or 2***\n")
        menu()#this part is lazy, I know
        
         

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
            print("Put an integer and try again") 
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
            questionbox = int(input("What is the {} combined maintenance and replacement rate in ml for a {}% dehydrated patient who weighs {}kg to be rehydrated over {} hours?\n$" .format(hoursordays, ptdehydration, ptweight, rehydrotime)))
            break        
        except ValueError:
            print("put an integer and try again") 
    if int(finalanswer) <= questionbox <= 1+int(finalanswer):
        print("CORRECT. The fluid amount is: {}ml/{}\nworking: the hourly rate is {}ml/hr and maintenance rate is {}ml/hr\n".format(finalanswer,rate,int(hourlyreplace),int(maintrate)))
        fluidmaintreplace()
    elif questionbox == 0:
        menu()
    else:
        print("WRONG. The fluid amount is: {}ml/{}\nworking: the hourly rate is {}ml/hr and maintenance rate is {}ml/hr\n".format(finalanswer,rate,int(hourlyreplace),int(maintrate)))
        fluidmaintreplace()


menu()



