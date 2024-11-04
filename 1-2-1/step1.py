# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand


from random import randint
font_setup= ("Arial", 20, "normal")
clicks = 1
score=0
timer=30
counter_interval=10000
timer_up= False

#-----game configuration----
spot_color= "gold"
spot_size = 5
spot_shape= "circle"
spot_movement="left"
#-----initialize turtle-----0
spot= trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)
spot.speed("fastest")

score_writer= trtl.Turtle()
score_writer.hideturtle()
score_writer.speed("fastest")

score_box=trtl.Turtle()
score_box.hideturtle()

counter=trtl.Turtle()

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
    score_writer.clear()
    score += 1
    score_writer.write(score,font=font_setup)
    score_writer.penup()
    score_writer.goto(-430,330)
    score_writer.pendown()

def countdown():
    # -----import statements-----
    import turtle as trtl

    # -----countdown variables-----
    font_setup = ("Arial", 20, "normal")
    timer = 30
    counter_interval = 1000  # 1000 represents 1 second
    timer_up = False

    # -----countdown writer-----
    counter = trtl.Turtle()
    counter.speed("fastest")
    # -----game functions-----
    counter.penup()
    counter.goto(-100, 330)
    counter.pendown()

    def countdown():
        global timer, timer_up
        counter.clear()
        if timer <= 0:
            counter.write("Time's Up", font=font_setup)
            timer_up = True
        else:
            counter.write("Timer: " + str(timer), font=font_setup)
            timer -= 1
            counter.getscreen().ontimer(countdown, counter_interval)

            # ---------events---------

    wn = trtl.Screen()
    wn.ontimer(countdown, counter_interval)
    wn.mainloop()
counter.penup()
counter.goto(250,300)
counter.pendown()

score_box.speed("fastest")
score_box.penup()
score_box.goto(-400,330)
score_box.pendown()
score_box.goto(-370,330)
score_box.goto(-370,370)
score_box.goto(-440,370)
score_box.goto(-440,330)
score_box.goto(-400,330)




#-----events----------------
spot.onclick(spot_clicked)
wn= trtl.Screen()
wn.ontimer(countdown,counter_interval)
wn.mainloop()