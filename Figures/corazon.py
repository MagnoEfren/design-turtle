import turtle as t 
t.bgcolor('black')
t.width(3)

def curve():
	for i in range(200):
		t.right(1)
		t.fd(1)

def heart(color):
	t.color('white', color)
	t.begin_fill()
	t.left(140)
	t.fd(120)
	curve()
	t.left(125)
	curve()
	t.fd(120)
	t.end_fill()
heart('red')
t.setheading(90)
heart('blue')
t.setheading(180)
heart('green2')
t.setheading(270)
heart('magenta')

t.hideturtle()
t.exitonclick()