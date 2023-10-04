# import package
import turtle
import pandas

screen = turtle.Screen()
screen.title("Bulgarian Provinces Game")
image = "Bulgaria.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("28_provinces.csv")
all_provinces = data.province.to_list()
guessed_provinces = []

while len(guessed_provinces) < 28:
    # taking input
    answer = turtle.textinput(
      title=f"{len(guessed_provinces)}/28 Provinces Correct",
      prompt="Do you know another province?")\
    .title()

    # print answer
    print(f"{answer} Province")

    if answer in all_provinces and answer not in guessed_provinces:
        guessed_provinces.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.province == answer]
        t.goto(float(province_data.x), float(province_data.y))
        t.write(answer)

screen.exitonclick()
