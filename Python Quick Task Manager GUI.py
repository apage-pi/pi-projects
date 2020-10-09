from guizero import App, Text, TextBox, PushButton, Picture, Window
from os import _exit
import pygame
from pygame.locals import *
from time import sleep
from random import randrange
from gpiozero import LED, Buzzer, Button
from sense_emu import SenseHat
def shatnew():
    shatw = Window(pqtm, title = "Sense Hat (Dev)")
    xpixel = Text(shatw, text = "X Pixel:")
    pixelx = TextBox(shatw)
    ypixel = Text(shatw, text = "Y Pixel:")
    pixely = TextBox(shatw)
    rt = Text(shatw, text = "Red value:")
    red = TextBox(shatw)
    yt = Text(shatw, text = "Green Value:")
    green = TextBox(shatw)
    bt = Text(shatw, text = "Blue value:")
    blue = TextBox(shatw)
    
def gpiozeroc():
    print("ERROR: No GPIO Coding")
def senseclear():
    sense = SenseHat()
    sense.clear()
def exitax():
    _exit(0)
def shat():
    sense = SenseHat()
    sense.clear()
    g = (0, 255, 0)
    k = (0, 0, 0,)
    r = (255, 0, 0,)
    y = (255, 255, 0,)



    draw_pixels = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, k, k, g, g, k, k, g,
        g, k, k, g, g, k, k, g, 
        g, g, g, k, k, g, g, g,
        g, g, k, k, k, k, g, g,
        g, g, k, k, k, k, g, g,
        g, g, k, g, g, k, g, g,
    ]


    sense.set_pixels(draw_pixels)
def shell():
    print("SHELL")
def pygamec():
    pygame.init()
    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h
    screen = pygame.display.set_mode((width, height))
    gui = pygame.image.load('PYGUI.png')
    gui = pygame.transform.scale (gui, (width, height))
    screen.blit(gui, (0,0))
    pygame.display.update()
    sleep(randrange(3, 5))
    pygame.quit()
pqtm = App(title="PythonOS")
wel = Text(pqtm, text="Welcome!", size=40, font="", color="lightblue")
shatb = PushButton(pqtm, command=shat, text="Sense HAT")
shellb = PushButton(pqtm, command=shell, text="Shell")
pygameb = PushButton(pqtm, command=pygamec, text="Pygame")
shatcb = PushButton(pqtm, command=senseclear, text="Clear Sense HAT Coding")
gpiob = PushButton(pqtm, command=gpiozeroc, text="GPIO")
exita = PushButton(pqtm, command=exitax, text="Exit")
shatc = PushButton(pqtm, command=shatnew, text="Sense HAT (Dev)")
pqtm.display()
    