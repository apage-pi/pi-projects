from ptoled import PTOLEDDisplay
from time import sleep
from ptbuttons import PTSelectButton

# initialise the Mini Screen, set the frames-per-second rate and font size
mini_screen = PTOLEDDisplay()
mini_screen.set_max_fps(1)
canvas = mini_screen.canvas
canvas.set_font_size(20)
select = PTSelectButton()

# Declare new function for program
def pitop() :
    canvas.multiline_text(canvas.middle_center(), "pi-top [4]")
    mini_screen.draw
    
# Now, the algorithm
# clear the screen, align the message top left, 'draw' this to the screen for a few seconds, then clear
canvas.clear()
canvas.multiline_text(canvas.middle_middle(), "Welcome to your pi-top [4]!")
mini_screen.draw()
sleep(5)
canvas.clear()
mini_screen.draw()
canvas.multiline_text(canvas.middle_middle(), "Loading Program...")
mini_screen.draw()
sleep(3)
mini_screen.clear()
canvas.multiline_text(canvas.middle_middle(), "pi-top [4]")
mini_screen.draw()