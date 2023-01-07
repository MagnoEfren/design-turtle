import turtle as t
from math import cos, sin

t.tracer(2)
t.bgcolor('black')
t.color('red')

def heartX(n):
	x = 15*sin(n)**3
	return x

def heartY(n):
	x = 12*cos(n)-5*cos(2*n)-2*cos(3*n)-cos(4*n)
	return x

for i in range(800):
	t.goto(heartX(i)*10, heartY(i)*10)
	t.goto(0,0)

t.exitonclick()
