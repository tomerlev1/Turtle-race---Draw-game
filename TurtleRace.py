from turtle import Turtle, Screen, forward
import random

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()

screen = Screen()

def t_shape(t_list):
  '''Shape all the turtles in the game'''
  for tur in t_list:

    tur.shape('turtle')
  


def color_Set(t_list):
  '''Set all the turtles colors'''
  color_list = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']

  for colors in range(6):

    t_list[colors].color(color_list[colors])
  

def position_Set(t_list):
  '''Set turtles positions'''
  y_pos = -125
  x_pos = -230

  for turtle in t_list:
    turtle.penup()

    turtle.goto(x= x_pos, y= y_pos)

    turtle.pendown()

    y_pos += 50


def start_game(color, pos, shape, t_list):
  '''The whole game process'''
  user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
  t_shape(turtle_list)
  color_Set(turtle_list)
  position_Set(turtle_list)
  
  is_on = True
  while is_on:
    for tur in t_list:
      tur.penup()
      tur.forward(random.randint(5, 15))
      tur.pendown()
      if tur.position()[0] > 230:
        is_on = False
        color_winner = tur.color()[0]
        if color_winner == user_bet:
          print(f'You win. The {user_bet} is the winner!🥇')
        else:
          print(f'You lose. The {color_winner} is the winner 😭')







if __name__=='__main__':

  screen.setup(width=500, height=400)
  screen.listen()

  turtle_list = [t1, t2, t3, t4, t5, t6] 
   
  start_game(color_Set, position_Set, t_shape, turtle_list)
  

  screen.exitonclick()