# import modules or classes for controlling components and code from code libraries
# import the PMA Ultrasonic Sensor class from the ptpma library (PMA = pi-top Maker Architecture)
# sleep lets us tell our components to wait (on or off) for a specified amount of time
from ptpma import PMAUltrasonicSensor, PMALightSensor, PMASoundSensor, PMAButton, PMABuzzer, PMALed, PMAPotentiometer
from time import sleep

# name the component(s) and state which port(s) they are connected to
ultrasonic_sensor = PMAUltrasonicSensor("D4")
light_sensor = PMALightSensor("A2")
sound_sensor = PMALightSensor("A3")
caller = PMAButton("D5")
test = PMAButton("D6")
buzz = PMABuzzer("D7")
led = PMALed("D0")
select = PMAPotentiometer("A0")

# the loop will return a constant distance reading
while True:
    if select.position >500:
        print("Recieve Mode")
    if caller.is_pressed:
        print(ultrasonic_sensor.distance)
        sleep(0.1)
        print(light_sensor.reading)
        sleep(0.1)
        print(sound_sensor.reading)
        sleep(0.1)
    if test.is_pressed:
        led.on()
        sleep(0.1)
        buzz.on()
        print(ultrasonic_sensor.distance)
        sleep(0.1)
        print(light_sensor.reading)
        sleep(0.1)
        print(sound_sensor.reading)
        sleep(0.1)
        led.off()
        sleep(0.1)
        buzz.off()
        sleep(0.1)