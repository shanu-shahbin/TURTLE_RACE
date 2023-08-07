from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? enter a color: ")
colours = ["red", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, -30, -60]
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colours[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])









screen.exitonclick()
