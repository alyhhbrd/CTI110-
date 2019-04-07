# CTI-110 
# P4T1A - turtleShapes 
# Aaliyah Hubbard 
# 03202019
#

#import turtles, create canvas
#define variables + attributes for turtles and canvas
#create loops for both instances (cosmo + wanda)  

#import turtle and create canvas
import turtle
win = turtle.Screen()

#define variables + attribute
cosmo = turtle.Turtle()
wanda = turtle.Turtle()

cosmo.color('SeaGreen')
cosmo.shape('turtle')
wanda.color('DeepPink')
wanda.shape('turtle')

win.bgcolor('PapayaWhip')
win.title('Hubbard_P4T1A_Shapes')

#create loops (sq + tri) for instances (cosmo + wanda)
for sq in [0,1,2,3]:
    cosmo.forward(125)
    cosmo.left(90)

for tri in [0,1,2]:
    wanda.forward(250)
    wanda.left(120)

win.mainloop()
