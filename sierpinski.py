
import turtle
import random

tri = turtle.Turtle()
window = turtle.Screen()

tri.pu()
tri.left(270)
tri.forward(100)
tri.left(90)
tri.pd()

tri.forward(200)
A = tri.pos()
tri.left(120)
tri.forward(400)
B = tri.pos()
tri.left(120)
tri.forward(400)
C = tri.pos()
tri.left(120)
tri.forward(200)

def distance(x, y):
    return ((x[0] +y[0])/2 , (x[1] + y[1])/2)

curr = (random.uniform(A[0], B[0]), random.uniform(A[1], B[1]))

Points = [A, B, C]
for i in range(20000):
    p = Points[random.randint(0, 2)]
    curr = distance(curr, p)
    tri.pu()
    tri.setpos(curr)
    tri.pd()
    tri.dot()




tri.end_fill()
turtle.done()
