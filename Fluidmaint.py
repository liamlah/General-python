import random

def fluidgame():
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
        fluidgame()
    else:
        print("WRONG the maintenance rate is: %sml/hr\n"%(maintrate))
        fluidgame()


fluidgame()


