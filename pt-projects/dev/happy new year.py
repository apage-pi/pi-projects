from ptpma import PMALed, PMAButton, PMABuzzer, PMAUltrasonicSensor, PMALightSensor, PMASoundSensor,  PMAPotentiometer
from time import sleep

gled = PMALed("D2")
yled = PMALed("D1")
rled = PMALed("D0")
button = PMAButton("D3")
buzz = PMABuzzer("D4")
us = PMAUltrasonicSensor("D5")
testrn = PMAButton("D6")
ls = PMALightSensor("A0")
ss = PMASoundSensor("A1")
select = PMAPotentiometer("A2")

def beep():
   buzz.on()
   sleep(1)
   buzz.off()