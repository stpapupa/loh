import turtle
t= turtle.Turtle()
t.fillcolor("pink")
t.begin_fill()
for _ in range (3):
    for _ in range (4):
        t.forward(200)
        t.right(90)
    t.left(90)
    t.forward(10)
t.left(90)
t.forward(10)
t.left(180)
t.home()
t.forward(50)
t.right(90)
t.forward(50)
t.end_fill()