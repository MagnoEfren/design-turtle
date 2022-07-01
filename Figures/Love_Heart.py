import turtle as t 

t.bgcolor('black')
t.color('red')

def curve():
	for i in range(200):
		t.right(1)
		t.fd(1)

t.begin_fill()
t.left(140)
t.fd(120)
curve()
t.left(125)
curve()
t.fd(120)
t.end_fill()
t.hideturtle()
t.up()
t.goto(0,80)
t.color('white')
t.write('LOVE', align='center', 
	font=('Hearts (BRK)', 40, 
		'bold'))

t.exitonclick()