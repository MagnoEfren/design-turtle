import turtle as t 

t.bgcolor('black')
t.width(2)

def form(x, color):
	t.pencolor(color)
	t.begin_fill()
	t.fillcolor(color)
	t.circle(100,x)
	t.up()
	t.goto(0,0)
	t.down()
	t.circle(-100,x)
	t.end_fill()
	t.up()
	t.goto(0,0)
	t.down()

def color_form(size, color, rad):
	for i in range(0,360, 90):
		t.setheading(i+rad)
		form(size, color)

color_form(100,"#9AB628", 0)
color_form(80,"#32FA05", 45)
color_form(60,"#3AB824", 90)

t.exitonclick()