import turtle

t = turtle.Turtle()

def draw_circle(radius, colour):
    t.color(colour)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def smile(radius):
    t.pensize(10)
    t.pencolor('red')
    t.circle(radius, 180)

draw_circle(100, 'Yellow')
t.penup()
t.goto(50, 90)
draw_circle(20, 'White')
t.goto(50, 100)
draw_circle(10, 'Black')
t.penup()
t.goto(-50, 90)
draw_circle(20, 'White')
t.goto(-50, 100)
draw_circle(10, 'Black')

t.penup()
t.goto(-75, 80)
t.right(90)
t.pendown()
smile(70)
turtle.done()