import turtle as t 
t.speed('fastest')
t.rt(-90)
t.goto(0, -100)
t.colormode(255)
t.bgcolor(0,0,0)
angle = 25

def draw(s, n):
    if n>0:
        t.pencolor(0, 255//n, 0)
        t.fd(s)
        t.rt(angle)
        draw(0.8*s, n-1)
        t.pencolor(0, 255//n, 0)
        t.lt(angle)
        draw(0.8*s, n-1)
        t.pencolor(0, 255//n, 0)
        t.lt(angle)
        draw(0.8*s, n-1)
        t.pencolor(0, 255//n, 0)
        t.rt(angle)
        t.fd(-s)
draw(60, 6)
t.exitonclick()