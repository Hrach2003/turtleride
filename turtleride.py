import turtle
from turtle import Turtle, Screen
import random
is_rise_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your best turtle", prompt="Which turtle will win the rise? ").lower()
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)
def my_function():
    global is_rise_on
    while is_rise_on:
        for turtle in all_turtles:
            distance = random.randint(0, 10)
            turtle.forward(distance)
            if turtle.xcor() > 230:
                winner_color = turtle.pencolor()
                if winner_color == user_bet:
                    print(f"Your turtle win {winner_color}")
                else:
                    print(f"You lose! {winner_color}")
                is_rise_on = False
                break


is_rise_on = True
my_function()




