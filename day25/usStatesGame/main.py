import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)  # this shape can be any gif image file
turtle.shape(image)  # turtle can be shaped to an image file too
screen.tracer(0)

# find x and y values of all states
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()  # will keep the turtle screen open

data = pandas.read_csv('50_states.csv')
all_states = data['state'].to_list()  # or data.state
guessed_states = []
# correct_count = 0
# print(states)


def check_state(guessed_state):
    if guessed_state in all_states:
        # print('hii')
        guessed_states.append(guessed_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guessed_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guessed_state, align='left', font=('Arial','6','normal'))  # or state_data.state.item() : item is a method on pandas dataseries, which brings first
        # value in the data

        # global correct_count
        # correct_count += 1
        # pen = turtle.Turtle()
        # pen.hideturtle()
        # pen.penup()
        # pen.color('black')
        # guess = data[states[i] == data.state]  # previously i did data['state'].lower() == guessed_state here
        # new_x = guess.x
        # new_y = guess.y
        # pen.goto(new_x, new_y)
        # pen.write('guessed_state',move=False, align='left', font=('Arial', 8, 'normal'))

#
#

answer_state = (screen.textinput(title="Guess the State", prompt="What's another state's name")).title()
check_state(answer_state)

while len(guessed_states) < 50:
    if answer_state == 'Exit':
        missing_states = [ state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    time.sleep(0.08)
    screen.update()
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name")).title()
    check_state(answer_state)


# further projects: identify parts in image, world map, map of own country
