from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block
import sys

def make_room_of_file(filename,mc,basex,basey,basez,w,m):
	file=open(filename)
	rows=file.read().splitlines()
	height=len(rows)
	y1=0
	for row in rows:
		y1=y1+1
		x1=0
		for char in row:
			x1=x1+1
			if char != " ":
				if char == "*":
					m=block.WOOD_PLANKS.id
				if char == "a":
					m=block.AIR.id
				if char == "s":
					m=block.STONE.id
				if char == "w":
					m=block.WOOD.id
				if char == "l":
					m=block.LAVA.id
				if char == "g":
					m=block.GLASS.id
				if char == "t":
					m=block.TNT.id
				for z1 in range(0,w):
					mc.setBlock(basex+x1,basey+height-y1,basez+z1,m,1)
					#print(x1,y1)				
	
	

mc = Minecraft.create()
x, y, z = mc.player.getPos()
if len(sys.argv)<2 :
	print("Usage: python3 make.py blueprint.txt")
	make_room_of_file("p.txt",mc,x-25,y,z-25,10,block.WOOD.id)
else:
	make_room_of_file(sys.argv[1],mc,x-25,y,z-25,10,block.WOOD.id)

