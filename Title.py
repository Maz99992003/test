import Module1
import Module2

Play1 = Module1.Player1()
Play2 = Module2.Player2()

input(print("Enter the name:"))

Roles = input(print("Enter a role: "))

if Roles == "a":
    Play1.show()
if Roles == "b":
    Play2.show()
