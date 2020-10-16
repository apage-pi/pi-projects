import pygame
from pygame.locals import *
from time import sleep
from random import randrange
pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height))
gui = pygame.image.load('PYGUI.png')
gui = pygame.transform.scale (gui, (width, height))
screen.blit(gui, (0,0))
pygame.display.update()
sleep(randrange(20, 35))
pygame.quit()