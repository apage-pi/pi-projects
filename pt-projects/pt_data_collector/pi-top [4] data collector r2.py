# import modules or classes for controlling components and code from code libraries
# import the PMA Ultrasonic Sensor class from the ptpma library (PMA = pi-top Maker Architecture)
# sleep lets us tell our components to wait (on or off) for a specified amount of time
from ptpma import PMAUltrasonicSensor, PMALightSensor, PMASoundSensor, PMAButton
from time import sleep

# name the component(s) and state which port(s) they are connected to
ultrasonic_sensor = PMAUltrasonicSensor("D4")
light_sensor = PMALightSensor("A2")
sound_sensor = PMALightSensor("A3")
caller = PMAButton("D5")

# the loop will return a constant distance reading
while True:
    if caller.is_pressed:
        print(ultrasonic_sensor.distance)
        sleep(0.1)
        print(light_sensor.reading)
        sleep(0.1)
        print(sound_sensor.reading)
        sleep(0.1)