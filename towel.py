from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

x, y, z = mc.player.getPos()

lava = 10
water = 8
air = 0

mc.setBlock(x+10, y+30, z, lava)
sleep(20)
mc.setBlock(x+10,y+32, z, water)
sleep(20)
mc.setBlock(x+10, y+32, z, air)
