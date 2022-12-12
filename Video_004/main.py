import turtle as t 
import colorsys as cs 

t.bgcolor('black')
t.tracer(40)
t.shape('circle')
c = 0 
for i in range(600):
	c += 0.005
	color = cs.hsv_to_rgb(c,1,1)
	t.color(color)
	t.fillcolor('black')
	t.begin_fill()
	t.circle(i/4, 60)
	t.rt(20)
	t.bk(180)
	t.up()
	t.goto(0,0)
	t.down()
	t.circle(i/4, 20)
	t.rt(55)
	t.fd(i/6)
	t.end_fill()

t.exitonclick()