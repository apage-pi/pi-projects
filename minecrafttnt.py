from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.postToChat("Hello TNT")

x, y, z = mc.player.getPos()

mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 46, 1)