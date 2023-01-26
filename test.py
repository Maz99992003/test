class Car:
    def _init_(self,name,numb,eng):
      self.name=name
      self.notyres=Tyers(numb)
      self.eng=eng
       

class Tyers:
    def  _init_(self,num):
        self.num=num

class Engine:
    def  _init_(self,eng):
        self.enf=eng
    
         
t = Tyers(4)
en = Engine(1)
mycar=Car("Honda", t, en)