from time import sleep
from os import _exit
from guizero import App,Text,TextBox,PushButton,Picture,Window
import pygame
from pygame.locals import *
from time import sleep
from random import randrange
from gpiozero import LED, Buzzer, Button
from sense_emu import SenseHat
def pygame():
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
def she():
    shew = Window(title = "Sense Hat Emulator")
def shutdown():
    print("Shutting Down")
    sleep(5)
    _exit(0)
print("Booting PythonOSDev...")
sleep(3)
print("Booted...Wating for Password...")
password = input("Password: ")
if password == "9746":
     print("Hello, Adam!")
     os = App(title="PythonOSTest")
else:
    print("Shutting Down...")
    sleep(3)
    _exit(0)
pygameb = PushButton(os, command=pygame, text="Pygame")
sensehatemulator = PushButton(os, command=she, text="Sense Hat Emulator")
shutdown = PushButton(os, command=shutdown, text="Shutdown")
