import random
class BigCat:
    def __init__(self):
        self.speed = 5
        self.strength = 5
        self.intelligence=5
        self.durability=5
        self.health=5

class Lion(BigCat):
    def __init__(self):
      self.strength=50
      self.health=50

    def king(self, bigcat):
       if isinstance(bigcat,Cheetah) :
           if random.random() < .6:
               return "The cheetah has gotten away"
           else:
                bigcat.health = 0
                return "The cheetah has been defeated by the Lion"
       else:
           bigcat.health=0
           return "The big cat has been defeated by the Lion"

class Leopard(BigCat):
    def __init__(self):
        self.strength =30
        self.health =30
        self.intelligence =30

    def attack(self,bigcat):
        if isinstance(bigcat,Lion):
             bigcat.king(self)
        elif isinstance(bigcat,Cheetah) :
            if random.random() < .6:
                return "The cheetah has gotten away"
            else:
                 bigcat.health = 0
                 return "The cheetah has been defeated by the Leopard"
        else:
            bigcat.health -= 15
class Cheetah(BigCat):
    def __init__(self):
      self.speed =75
      self.strength =25
      self.intelligence=25
      self.durability=25
      self.health=25
    def run(self,bigcat):
        if isinstance(bigcat,Leopard):
            bigcat.attack(self)
        elif isinstance(bigcat,Lion):
            bigcat.king(self)
        else:
            return "There has been stalemate between two cheetahs"
             
# Basically this is what the assignment was supposed to look like. 
# From this point on it was your job to take the code and build a game out of it.
