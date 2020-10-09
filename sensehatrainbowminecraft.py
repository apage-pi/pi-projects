from sense_emu import SenseHat
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

sense = SenseHat()
sense.clear()
sense.set_pixel(7, 7,(255, 255, 255))
def rwmf():
    while true:
        x, y, z = mc.player.getPos()  # player position (x, y, z)
        block_beneath = mc.getBlock(x, y-1, z)  # block ID

        if block_beneath == grass:
            mc.setBlock(x, y, z, flower)
rwmf()