from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block
def make_floor(mc,x,y,z,w,m):
    for i in range(-w,w):
        for j in range(-w,w):
            mc.setBlock(x+i,y,z+j,m)
    return
def make_walls(mc,x,y,z,w,m):
    for i in range(-w,w):
        mc.setBlock(x+i,y,z+j,m)
    return



def make_room(mc,x,y,z,w,m):
    #main
    mc.setBlocks(x-w,y-1,z-w,x+w,y+w,z+w,m) 
    mc.setBlocks(x-w+1,y,z-w+1,x+w-1,y+w-1,z+w-1,0) 
    mc.setBlocks(x-w,y,z,x-w,y+1,z+1,0) 
    #mc.setBlock(x-w,y,z,23) 
    mc.setBlock(x-w,y+1,z,block.DOOR_WOOD.id-1)
    mc.setBlock(x-w,y,z,block.DOOR_WOOD.id)
    for r in range(0,w):
        mc.setBlock(x-w+3+r,y+r,z+1,block.STAIRS_WOOD.id,0) 
        mc.setBlock(x-w+3+r,y+w,z+1,0)
        if r<w-1 :
            mc.setBlock(x-w+3+r,y-1,z+1,0)
        
    mc.setBlocks(x-w,y,z,x-w,y+1,z+1,0) 
    mc.setBlocks(x+w,y+1,z-1,x+w,y+2,z+1,block.GLASS.id)
    mc.setBlocks(x-1,y+1,z+w,x+1,y+ 2,z+w,block.GLASS.id)
    mc.setBlocks(x-1,y+1,z-w,x+1,y+2,z-w,block.GLASS.id)

    
    return

mc = Minecraft.create()
x, y, z = mc.player.getPos()
for q in range(0,8):
    for p in range(0,8):
        for r in range(0,2):
            make_room(mc,x+(q+2)*(6*2+2),y+6*r,z-p*(6*2+2),6,block.WOOD_PLANKS.id    )

