import turtle
import turtle as trtl


wn = trtl.Screen()
wn.bgcolor('lightblue')
ball = turtle.Turtle()
#player list
Player1_score=0
Player2_score=0
score = turtle.Turtle()
score.hideturtle()
score.speed(0)
game_over = False
winner = None


score.color("black")
score.penup()
score.goto(-250, 300)
score.write("Player 1 score : 0   Player 2 score: 0",
            font=("arial", 24, "normal"))






def leftstick():
    leftpaddle = trtl.Turtle()
    leftpaddle.speed(0)
    leftpaddle.penup()
    leftpaddle.goto(-400,0)
    leftpaddle.shape("square")
    leftpaddle.color("white")
    leftpaddle.shapesize(stretch_wid=5,stretch_len=1)


leftstick()

def rightstick():
    rightpaddle = trtl.Turtle()
    rightpaddle.speed(0)
    rightpaddle.penup()
    rightpaddle.goto(400,0)
    rightpaddle.shape("square")
    rightpaddle.color("white")
    rightpaddle.shapesize(stretch_wid=5,stretch_len=1)

rightstick()



# Update score display


def leftstick_up():
    leftstick.
def leftstick_down():
    if wn.onkeypress(leftstick, "s"):
        leftstick.down = -10
def rightstick_up():
    if wn.onkeypress(rightstick, "Up"):
        rightstick.up = 10

def rightstick_down():
    if wn.onkeypress(rightstick, "Down"):
        rightstick.down = -10

# Set up keyboard bindings
wn.listen()
wn.onkeypress(leftstick_up, "w")
wn.onkeypress(leftstick_down, "s")
wn.onkeypress(rightstick_up, "Up")
wn.onkeypress(rightstick_down, "Down")









ball.shape("circle")
ball.color("white")
ball.goto(0,0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1,stretch_len=1)




wn.mainloop()
