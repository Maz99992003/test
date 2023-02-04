import random

class Player2:
   def show(self):
     
     self.power=6
     self.speed=4
     self.amour=5
     print("power=",self.power,"speed=",self.speed, "amour=", self.amour)
     

   def Player2Play(self):
      dice1 = random.randrange(1,7)
      dice2 = random.randrange(1,7)
      dice3 = random.randrange(1,7)
      print(dice1,dice2,dice3)
      if dice1>=1 and dice1<=3: 
        self.power=self.power+1
        self.speed=self.speed+2
        self.mour= self.amour-1
      else:
       self.power=self.power-1
       self.speed = self.speed-2
       self.speed = self.amour+2   

       print("power=",self.power,"speed=",self.speed, "amour=", self.amour)
    