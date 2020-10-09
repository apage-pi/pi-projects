from guizero import App,Text,TextBox,PushButton,Picture,Window
from os import _exit
def picp():
    picw = Window(welcome, title="Debian Max Pictures")
    pithanks =Text(picw, text="Made Possible by Raspberry Pi and Raspibian", size=10, font="Times New Roman", color="red")
    pi = Picture(picw, image="1436.gif")
    raspb = Picture(picw, image="rasp.gif")
def exitax():
    _exit(0)
def welc():
    def mbu():
        tset.set( mb.get() )
    ga = Window(welcome, title="Debian Max Stater Page")
    welm = Text(ga, text="Welcome!", size=40, font="Times New Roman", color="lightblue")
    tset = Text(ga, text="", size=20, font="Times New Roman", color="lightblue")
    mb = TextBox(ga)
    update_tset = PushButton(ga, command=mbu, text="Display my text")
    picb = PushButton(ga, command=picp, text="Dev Pictures")
welcome = App(title="Load")
upapp = PushButton(welcome, command=welc, text="Start")
exita = PushButton(welcome, command=exitax, text="Exit")
welcome.display()
