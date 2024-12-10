
import turtle as trtl
import random as rand

#variables


wn = trtl.Screen()
maze_painter = trtl.Turtle()
wall_len=35
path_width=30



#setup turtle
maze_painter.left(90)
maze_painter.pensize(5)
maze_painter.speed(0)

#draw maze

#process:
#draw a line

#Turn left
#increment length
#repeat
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)



for wall in range(21):
    first_length = wall_len/rand.randint(1,5)
    maze_painter.forward(first_length)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if wall>5 :
        draw_barrier()
    maze_painter.forward(wall_len - path_width - first_length)
    maze_painter.left(90)
    wall_len += 15




# randomize location of doors and barriers in wall

#Pong_ball
def draw_pong(active_pong):
    active_pong.shape(pong_ball)
    active_pong.showturtle()
    wn.addshape(pong_ball)
    wn.update()














wn.listen()
wn.mainloop()