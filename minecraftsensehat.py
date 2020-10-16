from mcpi.minecraft import Minecraft
from sense_emu import SenseHat

mc = Minecraft.create()
sense = SenseHat()

owool = (35, 1)
mwool = (35, 2)
lbwool = (35, 3)
ywool = (35, 4)
lwool = (35, 5)
pwool = (35, 6)
gwool = (35, 7)
lgwool = (35, 8)
cwool = (35, 9)
purwool = (35, 10)
bwool = (35, 11)
brwool = (35, 12)
grwool = (35, 0)
rwool = (35, 0)
blwool = (35, 0)

while True:
    x, y, z = mc.player.getPos()
    block_beneath = mc.getBlock(x, y-1, z)
    print(block_beneath)
    
    if block_beneath == (35):
        sense.clear(255, 255, 255)
    if block_beneath == (35,:
        sense.clear(255, 165, 0)