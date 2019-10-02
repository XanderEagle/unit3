# by Xander Eagle
# October 2, 2019
# this draws 4 octagons in different colors without touching
import turtle

turtle.speed(0)


# this function tells turtle where to draw the plus signs


def goto(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()


# this function tells to turtle the size it and the color it will use


def plus_sign(size, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.fd(size)
    turtle.left(90)
    turtle.fd(size * 2)
    turtle.right(90)
    turtle.fd(size * 2)
    turtle.left(90)
    turtle.fd(size)
    turtle.right(90)
    turtle.back(size * 2)
    turtle.left(90)
    turtle.fd(size * 2)
    turtle.left(90)
    turtle.fd(size)
    turtle.left(90)
    turtle.fd(size * 2)
    turtle.right(90)
    turtle.fd(size * 2)
    turtle.left(90)
    turtle.fd(size)
    turtle.left(90)
    turtle.fd(size * 2)
    turtle.right(90)
    turtle.fd(size * 2)
    turtle.end_fill()


# this is where the user chooses the specific size and the color


size = int(input("What is the size?"))
color = str(input( "What is the color?"))

# this is where the functions are called
plus_sign(size, color)
turtle.seth(0)
goto(0, 0)
goto(0, -5 * size)
plus_sign(size, color)
turtle.seth(0)
goto(0, 0)
goto(5 * size, 0)
plus_sign(size, color)
turtle.seth(0)
goto(0, 0)
goto(-5 * size, 0)
plus_sign(size, color)
turtle.seth(0)
goto(0, 0)
goto(0, 5 * size)
plus_sign(size, color)

turtle.exitonclick()
