
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
drawer = trtl.Turtle()
apple_letter_x_offset = -25
apple_letter_y_offset = -50
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#-----functions-----
def reset_apple(apple):
  if len(letters) > 0:
    newX = rand.randint(-200,200)
    newY = apple.ycor()
    new_letter = rand.randint(0,len(letters))
    apple.goto(newX, newY)
    draw_apple(apple, letters.pop(new_letter))





# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_an_a()
  wn.update()

def drop_apple():
  apple.penup()
  x_coor = apple.xcor()
  y_coor = apple.ycor()
  apple.goto(0,-100)
  apple.pendown()
  apple.clear()

def draw_an_a():
  drawer.hideturtle()
  drawer.color("white")
  drawer.penup()
  drawer.goto(-7, -25)
  drawer.pendown()
  if  wn.onkeypress(draw_an_a, "a"):
    drawer.clear()
    random_letter = rand.choice(letters)
    drawer.write(random_letter, font=("Arial", 20, "bold"))



  drawer.penup()
  x_coor = drawer.xcor()
  y_coor = drawer.ycor()
  drawer.goto(0,-100)
  drawer.pendown()
  drawer.write("A", font=("Arial", 20, "bold"))
  wn.update()
  wn.listen()

#-----function calls-----
draw_apple(apple)



wn.onkeypress(drop_apple, "a")



wn.listen()
wn.mainloop()