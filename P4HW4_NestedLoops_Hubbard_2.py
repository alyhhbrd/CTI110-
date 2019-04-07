# Programs displays n-polygon using nested loops
# 032219
# P4HW4 - Nested Loops
# Aaliyah Hubbard
#

# import turtle, create canvas
# define variables
# using nested loop, create shape that arguably looks like pacman.
    # may or may not have been done accidentally on purpose.

def main():
    
    #create turtle
    import turtle

    #define variables
    wn = turtle.Screen()
    wn.bgcolor('MistyRose')

    pacMan = turtle.Turtle()
    pacMan.color('Yellow')
    pacMan.shape('turtle')
    pacMan.pensize(8)
    pacMan.speed(11)

    #create shapes using nested loops
    pacMan.left(25)
    
    for x in range(13):
        for y in range(4):
            pacMan.forward(100)
            pacMan.left(90)
        pacMan.left(17)        

#initialize
main()









