###  Youtube: Magno Efren
###  Texto con Turtle

import numpy as np 
import turtle as t 

t.bgcolor('black')
t.colormode(255)
t.penup()
t.setup(width = 1.0, height =1.0)
h = 320
t.setx(-320)
t.sety(h)

for i in range(60):
	color = np.random.choice(range(256), size=3)
	t.pencolor(color)
	t.write( 'TIKTOK', 
		font= ('arial', 18, 'bold'))
	t.fd(160)
	d = t.xcor()
	if d == 320:
		h -=50
		t.setx(-320)
		t.goto(-320, h)
t.exitonclick()
