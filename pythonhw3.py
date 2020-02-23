class Boxer:
    def __init__(self,size,strength,wins,losses):
        self.size = size
        self.strength = strength
        self.wins = wins
        self.losses = losses

    # this function places all of the attributes into a list and returns the 
    # sum value of all attributes:
    def stats(self):
        return sum([self.size,self.strength,self.wins,self.losses])



boxer1 = Boxer(180,300,10,0)

boxer2 = Boxer(170,300,0,0)

print("**********************************************")

print(" ")

print("Boxer 1: Size:  {}, Strength: {}, Wins: {}, Losses: {}".format(boxer1.size,
boxer1.strength,boxer1.wins,
boxer1.losses))

print(" ")

print("**********************************************")

print("**********************************************")

print(" ")

print("Boxer 2: Size:  {}, Strength: {}, Wins: {}, Losses: {}".format(boxer2.size,
boxer2.strength,boxer2.wins,
boxer2.losses))

print(" ")

print("**********************************************")

userInput = 0

while userInput != 1 and userInput != 2:
    userInput = int(input("Please place your bet on Boxer 1 or Boxer 2. Input 1 or 2"))

winner = 0

if boxer1.stats() > boxer2.stats():
    winner = 1
else:
    winner = 2

if(winner == userInput):
    print("Congrats you won $10,000,000")
else:
    print("Sorry you lose")

