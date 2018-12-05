"""#numberguesser
high= 100
low = 0
noguesses = 0
theanswer = low+high/2
print("I will guess a number between 0 and 100 within 7 guesses. Think of that number.\n simply tell me if it's higher or lower.")"""

def startreset():
    global high
    global low
    global noguesses
    global theanswer
    high= 100
    low = 0
    noguesses = 0
    theanswer = low+high/2
    print("I will guess a number between 0 and 100 within 7 guesses. Think of that number.\n simply tell me if it's higher or lower.\n")
    question()
    

def question():
    global high
    global low
    global noguesses
    global theanswer
    noguesses += 1
    if noguesses >7:
        fail()
    theanswer = (low+high)/2
    hilo = int(input("Is your number {}?\n1)Yes\n2)Higher\n3)Lower\n>>>".format(int(theanswer))))
    if hilo == 1:
        print("Yay! I did that in {} guesses.".format(noguesses))
        again = int(input("Do you want me to guess another number?\n1)Yes\n2)No\n>>>"))
        if again == 1:
            startreset()
    elif hilo == 2:
         higher()
    elif hilo == 3:
         lower()
    


def higher():
    global low
    global theanswer
    low = theanswer
    question()


def lower():
    global high
    global theanser
    high = theanswer
    question()

def fail():
    print("Looks like I didn't get the number, are you sure it didn't change?")
    again = int(input("Do you want me to guess another number?\n1)Yes\n2)No\n>>>"))
    if again == 1:
        startreset()    


startreset()
      
