from turtle import Screen, Turtle

CURSOR_SIZE = 20

screen = Screen()
screen.setup(600, 600)  # 12 x 24 bricks
screen.setworldcoordinates(0, 0, 12, 24)  # coordinates based on bricks
screen.bgcolor('black')

turtle = Turtle('square', visible=False)
turtle.penup()
turtle.speed('fastest')
turtle.color('black', 'red')
turtle.shapesize(25 / CURSOR_SIZE, 50 / CURSOR_SIZE, 5)  # turn cursor into brick

for y in range(24):
    turtle.setposition(-0.5 * (y % 2), y + 0.3)

    for x in range(13):  # baker's dozen due to brick skew
        turtle.stamp()
        turtle.forward(1)

screen.mainloop()