from sense_emu import SenseHat
sense = SenseHat()
sense.clear()

def weather():
    hum = sense.get_humidity()
    hum = round(hum, 1)
    print("Humidity: %s percent" % hum )
def orient():
    orient = sense.get_gyroscope_raw()
    print(orient)
sense.stick.direction_up = orient
sense.stick.direction_left = weather
while True:
    pass