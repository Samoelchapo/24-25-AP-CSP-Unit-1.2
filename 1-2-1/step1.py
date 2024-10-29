# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl


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

#-----game functions--------
def spot_clicked(x,y):
    print(1)


#-----events----------------
spot.onclick(spot_clicked)
wn= trtl.Screen()
wn.mainloop()