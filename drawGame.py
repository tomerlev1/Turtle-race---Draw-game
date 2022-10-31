from turtle import Turtle, Screen, resetscreen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)
  
def left_Clockwise():
    tim.left(10)

def right_Clockwise():
    tim.right(10)

def clear_screen():
    screen.resetscreen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)

screen.onkey(key="s", fun=move_backwards)

screen.onkey(key="a", fun=left_Clockwise)

screen.onkey(key="d", fun=right_Clockwise)

screen.onkey(key="c", fun=clear_screen)



screen.exitonclick()