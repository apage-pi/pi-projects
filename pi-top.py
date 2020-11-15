# Import modules
from ptoled import PTOLEDDisplay
from time import sleep
from ptbuttons import PTUpButton, PTDownButton, PTCancelButton
from os import _exit
from random import randrange

# Initialise the Mini Screen
miniscreen = PTOLEDDisplay()
up = PTUpButton()
down = PTDownButton()
#select = PTSelectButton()
cancel = PTCancelButton()

# Action for a pi-top screen
def pi_top():
    miniscreen.draw_multiline_text('pi-top [4]', font_size=29)

# Action for UP
def upact():
    print("ptbuttons.PTUpButton.pressed()")
    miniscreen.draw_multiline_text(name + ', UP was pushed', font_size=20)
    sleep(3)
    pi_top()

# Action for DOWN
def downact():
    print("ptbuttons.PTDownButton.pressed()")
    miniscreen.draw_multiline_text(name + ', DOWN was pushed', font_size=20)
    sleep(3)
    pi_top()

# Action for CANCEL
def endoperation():
    print("ptbuttons.PTCancelButton.pressed()")
    print("Ending program. Goodbye.")
    sleep(randrange(1,5))
    _exit(0)
# Prompt for user input from the console
name = input("Type your name here, then press Enter: ")

# pi-top welcome
start = input(name + ", Do you have a pi-top [4] that is set up and are you running this on that pi-top? Enter yes or no. ")
if start == "yes":
    print("Welcome to pi-top [4]")
    print("Handing control to pi-top [4] OLED and buttons. Please wait...")
    sleep(randrange(3, 10))
    print("OLED and button connect sucessful. Look on OLED now.")
    miniscreen.draw_multiline_text('Hello, ' + name, font_size=20)
    sleep(5)
    pi_top()
else:
    _exit(0)
# Input buttons
while True:
    up.when_pressed = upact
    down.when_pressed = downact
    # select.when_pressed = green.toggle
    cancel.when_pressed = endoperation