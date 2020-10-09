# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes: 
from turtle import *
from shapes import *
from time import sleep
from osstartexit import *

# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(10)
FONTSIZE = 18

FONT = ('Arial', FONTSIZE, 'normal')

# Draw three circles:
start()
startturtle()
draw_circle(tommy, "green", 50, 25, 150)
draw_circle(tommy, "blue", 50, 0, 150)
draw_circle(tommy, "yellow", 50, -25, 150)
tommy.penup()
tommy.goto(0, 120)
tommy.color("black")
tommy.write("Thanks to Trinket.io", align= "center", font=FONT)

# Write a little message:
tommy.goto(0, -30)
tommy.color("black")
tommy.write("Teach With Code!", align= "center", font=FONT)
tommy.goto(0, -130)
tommy.write("Made By Python 3.7 with help by 3 libraries", align= "center", font=FONT )
#    tommy.write('Hello World!', c, font=FONT)
tommy.goto(0,-80)
tommy.right(90)
stopturtle()
sleep(4)
shutdown()

# Try changing draw_circle to draw_square, draw_triangle, or draw_star