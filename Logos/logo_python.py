# Python - Logo
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import turtle as t 

t.bgcolor('black')
t.speed('fastest')
t.pensize(5)
t.pencolor('white')
t.shapesize(4,3)

def curve_one():
	for i in  range(90):
		t.left(1)
		t.fd(1)
def curve_two():
	for i in range(90):
		t.right(1)
		t.fd(1)
def curve_three(d):
	curve_one()
	t.fd(d)
	curve_one()

def halt_logo():
	t.fd(50)
	curve_one()
	t.fd(90)
	curve_three(80)
	t.fd(40)
	t.left(90)
	t.fd(80)
	t.right(90)
	t.fd(10)
	t.right(90)
	t.fd(120)
	curve_three(90)
	t.fd(30)
	t.left(90)
	t.fd(50)
	curve_two()
	t.fd(40)

def point_pos(x, y):
	t.penup()
	t.goto(x,y)
	t.dot(40, 'black')
	t.pendown()

t.begin_fill()
t.fillcolor("#306998")
halt_logo()
t.end_fill()
t.penup()
t.goto(20,-10)
t.pendown()
t.fillcolor("#FFD43B")
t.begin_fill()
t.setheading(180)
halt_logo()
t.end_fill()
point_pos(-50, 150)
point_pos(60, -160)
t.hideturtle()

t.exitonclick()


