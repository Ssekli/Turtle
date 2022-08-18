import turtle

t = turtle.Turtle()

#variable size of steps and numbers


"""def stairs(length, heigth, NB_OF_STEPS) :
    for i in range (0, NB_OF_STEPS) :
        t.forward(length)
        t.left(90)
        t.forward(heigth)
        t.right(90)
        length -= 2
        heigth -= 2
   
    t.forward(length)
    
   
stairs(30,30,10)"""


def square(size) :
    for i in range(0, 4) :
        t.forward(size)
        t.left(90)

#square(10)

def squares(starting_size, number) :
    for i in range(0, number) :
        size = (i+1)*starting_size
        square(size)

squares(5, 5)

turtle.done()