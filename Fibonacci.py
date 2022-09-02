import turtle
import math

ok = int(input("Enter no. of elements: "))

wn = turtle.screensize(1000, 800, "white")
pen = turtle.Turtle()
pen.pensize(5)
pen.color("blue")
pen.shape("circle")
sp_pen = turtle.Turtle()
sp_pen.pensize(1)
sp_pen.color("yellow")
sp_pen.shape("turtle")


def main(N):
    valueOne = 0
    valueTwo = 1
    fib = 1
    pen.fillcolor("black")
    pen.begin_fill()
    for i in range(N):
        pen.right(90)
        drawSq(fib * 20)
        fib = valueOne + valueTwo
        valueOne = valueTwo
        valueTwo = fib


def drawSq(sides):
    for n in range(6):
        pen.forward(sides)
        pen.left(90)


def spiral():
    r = 20
    angle = 90
    sp_pen.right(90)
    sp_pen.penup()    
    sp_pen.setpos(0,0)
    sp_pen.pendown()
    arc(20, angle)
    arc(20, angle)
    arc(40, angle)
    arc(60, angle)
    arc(100, angle)
    arc(160, angle)
    arc(260, angle)
    arc(420, angle)


def arc(r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    # Before starting making a slight left turn.
    sp_pen.left(step_angle / 2)
    arcLine(n, step_length, step_angle)
    sp_pen.right(step_angle / 2)


def arcLine(n, length, angle):
    for i in range(n):
        sp_pen.forward(length)
        sp_pen.left(angle)


main(ok)
pen.end_fill()
spiral()


'''
def fibonacci(N):
    start = [1, 1]
    for i in range(2, N):
        next_num = start[-1] + start[-2]
        start.append(next_num)
    return start

print(fibonacci(int(input("Enter length of sequence: "))))
'''
