import turtle
import pandas


screen = turtle.Screen()
screen.screensize(600, 500)
screen.title("Regions In Ghana")
image = "blank_ghana_map_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("16_regions_ghana.csv")
all_state = data.region.to_list()
guessed_regions = []

while len(guessed_regions) < 16:
    answer_region = screen.textinput(title=f"{len(guessed_regions)}/16 Regions Correct",
                                     prompt="What is another region name?").title()
    print(answer_region)
    if answer_region == "Exit":
        missing_state = [state for state in all_state if state not in guessed_regions]

# This code work the same as the above, but the above is optimized
        # missing_state = []
        # for state in all_state:
        #     if state not in guessed_regions:
        #         missing_state.append(state)
        # new_data = pandas.DataFrame(missing_state)
        # new_data.to_csv("regions_to_learn.txt")
        break

    if answer_region in all_state:
        guessed_regions.append(answer_region)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        region_data = data[data.region == answer_region]
        t.goto(int(region_data.x), int(region_data.y))
        t.write(answer_region)





# def get_mouse_click(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()

# screen.exitonclick()