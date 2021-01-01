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

def sswarn():
   if ss.reading <30:
      gled.on()
      sleep(1)
      gled.off()
   if ss.reading >30 and ss.reading <75:
      yled.on()
      sleep(1)
      yled.off()
   if ss.reading >75 and ss.reading <150:
      rled.on()
      sleep(1)
      rled.off()
   if ss.reading >150:
      rled.on()
      buzz.on()
      sleep(1)
      buzz.off()
      rled.off()

def uswarn():
   if us.distance >1:
      gled.on()
      sleep(1)
      gled.off()
   if us.distance <1 and us.distance >0.5:
      yled.on()
      sleep(1)
      yled.off()
   if us.distance <0.5 and us.distance >0.1:
      rled.on()
      sleep(1)
      rled.off()
   if us.distance <0.1:
      rled.on()
      buzz.on()
      sleep(1)
      buzz.off()
      rled.off()
def lswarn():
   if ls.reading >5:
      gled.on()
      sleep(1)
      gled.off()
   if ls.reading <5 and ls.reading >2.5:
      yled.on()
      sleep(1)
      yled.off()
   if ls.reading <2.5 and ls.reading >0.5:
      rled.on()
      sleep(1)
      rled.off()
   if ls.reading <0.5:
      rled.on()
      buzz.on()
      sleep(1)
      buzz.off()
      rled.off()

def read():
    print("Reading in 3 sec. Move sensors to desired spot/place now.")
    sleep(3)
    print(us.distance)
    uswarn()
    sleep(0.3)
    print(ls.reading)
    lswarn()
    sleep(0.3)
    print(ss.reading)
    sswarn()
    sleep(0.2)
def readfortest():
    sleep(0.1)
    print(us.distance)
    sleep(0.1)
    print(ls.reading)
    sleep(0.1)
    print(ss.reading)
    sleep(0.2)
def test():
    gled.on()
    yled.on()
    rled.on()
    buzz.on()
    print("Reading in 5 sec. Move sensors to desired LED/buzzer now.")
    sleep(5)
    readfortest()
    gled.off()
    yled.off()
    rled.off()
    buzz.off()
def party():
    print("Party Time!")
    for i in range(10):
        gled.on()
        buzz.on()
        sleep(0.5)
        gled.off()
        yled.on()
        sleep(0.5)
        buzz.off()
        yled.off()
        rled.on()
        sleep(0.5)
        buzz.on()
        rled.off()
        sleep(0.3)
        buzz.off()
        sleep(0.1)
    gled.on()
    yled.on()
    rled.on()
    buzz.on()
    sleep(3)
    buzz.off()
    rled.off()
    yled.off()
    gled.off()
    print("And the party is done!")
print("")
print("Reading Guide:")
print("-----------------")
print("Ultrasonic Sensor")
print("Light Sensor")
print("Sound Sensor")

while True:
    gled.off()
    if button.is_pressed:
        print("Traffic Lights Starting...")
        gled.on()
        sleep(1.5)
        gled.off()
        sleep(0.1)
        yled.on()
        sleep(3)
        yled.off()
        sleep(0.1)
        rled.on()
        sleep(0.1)
        buzz.on()
        sleep(6)
        buzz.off()
        sleep(0.1)
        rled.off()
        sleep(0.1)
        print("Traffic Lights Done")
    if testrn.is_pressed:
        if select.position <500:
            read()
        elif select.position >500 and select.position <900:
            test()
        elif select.position >900:
            party()