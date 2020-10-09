#This Is a Custom Module for starts and exits.
from os import _exit
from time import sleep

def start():
    print("Booting...")
    sleep(3)
def shutdown():
    print("Shutting Down...")
    sleep(3)
    _exit(0)
def startturtle():
    print("Starting Turtle...")
    sleep(1)
def stopturtle():
    print("Stopping Turtle...")
    sleep(1)