import Module1
import Module2

Play1 = Module1.Player1()
Play2 = Module2.Player2()

input(print("Enter the name:"))

Roles = input(print("Enter a role:"))

if Roles == "a":
    print("Welcome Hunter")
    Play1.show()
    print("You must cross a dangerous bridge to save a villager")
    Play1.Player1Play
    if Play1.speed > 6:
      print("You pass the bridge and save the villager")
    else:
        print("You Lose")



if Roles == "b":
    print("Welcome Knight")
    Play2.show()
    print("You must defeat an enemy to save a villager")
    Play2.Player2Play
    if Play2.power > 6:
      print("You defeat the enemy and save the villager")
    else:
        print("You Lose")  


    

