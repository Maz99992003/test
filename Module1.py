import random

class Player1:
   def show(self):
     
     self.power=5
     self.speed=5
     self.amour=3
     print("power=",self.power,"speed=",self.speed, "amour=", self.amour)
     

   def Player1Play(self):
      dice1 = random.randrange(1,7)
      dice2 = random.randrange(1,7)
      dice3 = random.randrange(1,7)
      print(dice1,dice2,dice3)
      if dice1>=1 and dice1<=3: 
        self.power=self.power+1
        self.speed=self.speed+2
        self.amour=self.amour-1
      else:
       self.power=self.power-1
       self.speed = self.speed-2
       self.speed = self.amour+2   

       print("power=",self.power,"speed=",self.speed, "amour=", self.amour)
    