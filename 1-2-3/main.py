#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.addshape(pear_image)# Make the screen aware of the new file
wn.bgpic('background.gif')
apple = trtl.Turtle()
pear= trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def draw_pear(active_pear):
  pear.penup()
  pear.goto(100,0)
  pear.pendown()
  active_pear.shape(pear_image)
  wn.update()

def apple_down(active_apple):
  active_apple.shape('apple.gif')
  wn.setup(width=1.0, height=1.0)
  wn.onkeypress(, "a")
  apple.goto(0,-100)




#-----function calls-----
draw_apple(apple)
draw_pear(pear)
apple_down(apple)


wn.mainloop()
wn.listen()

wn.update()
