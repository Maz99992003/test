import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for c in [10, 16, 22, 28]:     # repeat four times
    for i in [0,1,3,4,]:
     alex.forward(50+c)
     alex.left(90)

wn.exitonclick()