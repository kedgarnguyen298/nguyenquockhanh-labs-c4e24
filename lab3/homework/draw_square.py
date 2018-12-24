from turtle import *

def draw_square(length, color_name):
    color(color_name)

    for i in range(4):
        forward(length)
        left(90)

speed(200)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()