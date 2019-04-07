# CTI-110 
# P4T1C - turtleSnowflakes
# Aaliyah Hubbard 
# 03242019
#

#import turtle & random modules, create canvas
#define variables + attributes
#create loops for both instances (two seperate snowflakes)

#import turtle & random modules, create canvas
import turtle
import random
wn = turtle.Screen()

#define variables + attributes
wn.title('P4T1C_hubbard')
wn.bgcolor('GhostWhite')

turtle.shape('triangle')
turtle.color('PowderBlue')
turtle.speed(0)

sfcolors = ['PowderBlue','SlateBlue3','silver']

#create loops for both instances (two seperate snowflakes)
#first instace
for sf in range(10):
    for sf in range(2):
        turtle.forward(50)
        turtle.right(60)
        turtle.forward(50)
        turtle.right(120)
    turtle.right(36)
    turtle.color(random.choice(sfcolors))

turtle.penup()
turtle.backward(100)
turtle.pendown()

#second instance
def branch():
    for sf in range(3):
        for sf in range(3):
            turtle.forward(30)
            turtle.backward(30)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(30)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(90)

for sf in range(8):
    turtle.color(random.choice(sfcolors))
    branch()
    turtle.left(45)
 

