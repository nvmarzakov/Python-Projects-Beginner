# import package
import turtle
import pandas

screen = turtle.Screen()
screen.title("Bulgarian Provinces Game")
image = "Bulgaria.gif"
turtle.addshape(image)
turtle.shape(image)

# see the location o
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

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
    if answer == 'Exit':
        missing_provinces = []
        for province in all_provinces:
            if province not in guessed_provinces:
                missing_provinces.append(province)
        new_data = pandas.DataFrame(missing_provinces)
        new_data.to_csv("provinces_to_learn.csv")
        break

    if answer in all_provinces and answer not in guessed_provinces:
        guessed_provinces.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.province == answer]
        t.goto(float(province_data.x), float(province_data.y))
        t.write(f'{answer} province')


# provinces_to_learn.csv
