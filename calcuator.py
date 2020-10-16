import math
shutdown = "on"
def calc():
    numone = int(input("First number: "))
    numtwo = int(input("Second number: "))
    add = numone + numtwo
    subtract = numone - numtwo
    multiply = numone * numtwo
    divide = numone / numtwo
    print(add)
    print(subtract)
    print(multiply)
    print(divide)
while shutdown == "on":
    calc()