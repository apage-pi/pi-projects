wel = input("Welcome to Python Quick Task! Press N to continue, or type GUI to use the Alpha GUI Interface. ")
if wel == " N":
    print("Lets go!")
if wel == "GUI":
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
    setup = pygame.image.load('PYGUI2.png')
    setup = pygame.transform.scale (setup, (width, height))
    sleep(randrange(3, 5))
    screen.blit(setup, (0,0))
    pygame.display.update()
    sleep(randrange(3, 5))
    pygame.quit()
sel = input ("Do you want to run the Sense HAT, if so, type SHAT, if you want to run the shell type S. If you want to run the Turtle type T. If you want to run the GUI type GUI. ")
if sel == "SHAT":
    from sense_emu import SenseHat
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
if sel == "T":
    import turtle
    t = turtle.Turtle()
    for i in range (10):
        for i in range(2):
            t.forward(100)
            t.right(90)
            t.forward(100)
            t.right(90)
        t.right(32)
if  sel == "S":
    print("SHELL")
if sel == "GUI":
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
