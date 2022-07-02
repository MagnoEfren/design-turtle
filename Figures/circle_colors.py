import turtle as t 
import colorsys

t.bgcolor("black")
t.speed("fastest")
t.pensize(3)
c = 0
for j in range(12):
    for i in range(10):
    	c+=0.05
    	color = colorsys.hsv_to_rgb(c, 1, 1)
    	t.pencolor(color)
    	t.goto(0,0)
    	t.pd()
    	t.circle(120,steps=12)
    	t.right(100)

t.exitonclick()