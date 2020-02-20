import random

correctnumber = random.randint(1,10)

print("CORRECT NUMBER ", correctnumber)

userguess = int(input("Guess a number from 1 to 10 please!"))

while correctnumber != userguess:
    if userguess > correctnumber:
        print ("Number is too high try again")
        userguess = int(input("Guess a number from 1 to 10 please!"))

    if userguess < correctnumber:
        print ("Number is too low try again")
        userguess = int(input("Guess a number from 1 to 10 please!"))

print("Congratulations the correct number is ", correctnumber)