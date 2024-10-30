# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

from random import randint
font_setup= ("Arial")
clicks = 1
score=0

#-----game configuration----
spot_color= "pink"
spot_size = 2
spot_shape= "circle"
spot_movement="left"
#-----initialize turtle-----0
spot= trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)
spot.speed("fastest")

score_writer= trtl.Turtle()

#-----game functions--------
spot.penup()
def change_position():
    X_position = rand.randint(-400,400)
    Y_position = rand.randint(-300,300)
    spot.goto(X_position,Y_position)
def spot_clicked(x,y):
       change_position()
       update_score()

def update_score():
    global score
    score += 1
    print(score)

score_writer.penup()
score_writer.goto(-400,350)
score_writer.pendown()




#-----events----------------
spot.onclick(spot_clicked)
wn= trtl.Screen()
wn.mainloop()