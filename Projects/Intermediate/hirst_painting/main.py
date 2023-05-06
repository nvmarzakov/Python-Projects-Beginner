# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# colors_added = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_added.append(new_color)
#
# print(colors_added)
import turtle
import random

color_list = [(153, 91, 49), (209, 156, 107), (42, 111, 146), (60, 116, 75), (199, 157, 31), (240, 58, 34), (131, 170, 183), (248, 211, 75), (155, 7, 26), (145, 64, 87), (146, 219, 161), (29, 178, 108), (188, 132, 139), (253, 232, 0), (125, 181, 123), (23, 55, 82), (222, 49, 52), (193, 234, 198), (46, 151, 194), (17, 90, 59), (250, 147, 138), (3, 78, 45), (250, 146, 159), (218, 231, 237), (192, 26, 13), (245, 229, 232), (3, 82, 118), (81, 71, 41), (46, 62, 86)]

from turtle import Turtle, Screen

turtle.colormode(255)
object = Turtle()
screen = Screen()

object.hideturtle()
object.setheading(225)
object.penup()
object.forward(300)
object.setheading(0)
object.pendown()

number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):

    object.dot(20, random.choice(color_list))
    object.penup()
    object.forward(50)

    if dot_count % 10 == 0:
        object.setheading(90)
        object.forward(50)
        object.setheading(180)
        object.forward(500)
        object.setheading(0)

screen.exitonclick()

