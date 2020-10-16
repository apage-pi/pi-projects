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
    g, k, r, g, g, r, k, g, 
    g, g, g, k, k, g, g, g,
    g, g, k, k, k, k, g, g,
    g, g, k, k, k, k, g, g,
    g, g, k, r, r, k, g, g,
]


sense.set_pixels(draw_pixels)