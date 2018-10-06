#C1V1 calculator. pretty simple stuff

print("This program will calculate your missing variable in a dilution. please enter the digit 0 for the value you do not know\n")

print("Enter the values for")
c1 = input("C1:")
c2 = input("C2:")
v1 = input("V1:")
v2 = input("V2:")

if c1 and c2 and v1 and v2 < 0:
    print("it looks like you have all your values")
else:
    print("A-ok")
