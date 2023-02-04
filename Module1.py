import random

class Player1:
   def show(self):
     
     self.power=5
     self.speed=5
     self.amour=3
     print("power=",self.power,"speed=",self.speed, "amour=", self.amour)
     

     
     dice1 = random.randrange(1,7)
     dice2 = random.randrange(1,7)
     dice3 = random.randrange(1,7)
     print(dice1,dice2,dice3)