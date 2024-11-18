
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
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#-----functions-----
def tree(apple):
  if len(letters) > 0:
    newX = rand.randint(-200,200)
    newY = apple.ycor()
    new_letter = rand.choice(letters)

  for i in range(0, number_of_apples):

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_an_a()
  wn.update()

def drop_apple():
  apple.penup()
  x_coor = apple.xcor()
  y_coor = apple.ycor()
  apple.goto(x_coor, y_coor - 300)
  apple.pendown()

def draw_an_a():
  drawer.hideturtle()
  drawer.color("white")
  drawer.penup()
  drawer.goto(-7, -25)
  drawer.pendown()
  drawer.write("A", font=("Arial", 20, "bold"))
  wn.update()
  wn.listen()
  wn.onkeypress(draw_an_a, "A")
  drawer.penup()
  x_coor = drawer.xcor()
  y_coor = drawer.ycor()
  drawer.goto(x_coor, y_coor - 300)
  drawer.pendown()

#-----function calls-----
draw_apple(apple)


wn.onkeypress(draw_an_a, "a")
wn.onkeypress(drop_apple, "a")



wn.listen()
wn.mainloop()