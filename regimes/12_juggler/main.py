from os import urandom
from time import sleep
from neopixel import NeoPixel
from machine import Pin
from math import floor

dataPin = Pin(15)
ledCount = 7
np = NeoPixel(dataPin, ledCount)

def blank():
	for pos in range(ledCount):
		np[pos]=(0,0,0)
	np.write();

def visitAll():
	for pos in range(ledCount):
		blank()
		np[pos]=(0,0,255)
		np.write()
		print(pos)
		input('...')

def log2_approx(val):
	val = floor(val)
	approx = 0
	while val != 0:
		val &= ~ (1<<approx)
		approx = approx + 1
	return approx
		
def rand_int(bound):
	byteCount = (log2_approx(bound) // 8) + 1 # each byte is 8 powers of two
	val = 0
	for idx, entry in enumerate(bytearray(urandom(byteCount))):
		val |= entry << (idx * 8)
	return val % bound
	
black = (0,0,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)

ledColors = [black for pos in range(ledCount)]

colors = [ yellow, green, blue ]
locations = [0 for pos in range(len(colors))]
directions = [0 for pos in range(len(colors))]
			
def colorBalls():
	for pos in range(ledCount):
		np[pos]=black
	for pos,color in enumerate(colors):
		np[locations[pos]]=color
	np.write()

def stepBalls():
	for ball, color in enumerate(colors):
		if directions[ball] == 0:
			pass
		elif directions[ball] == 1:
			if locations[ball] == 4:
				displaced = [testedBall for testedBall,location in enumerate(locations) if locations[testedBall] == 5]
				for displacedBall in displaced:
					directions[displacedBall]=-1
		elif directions[ball] == -1:
			if locations[ball] == 2:
				displaced = [testedBall for testedBall,location in enumerate(locations) if locations[testedBall] == 1]
				for displacedBall in displaced:
					directions[displacedBall]=1
	for ball, color in enumerate(colors):
		locations[ball] = locations[ball] + directions[ball]
		if locations[ball] == 1 or locations[ball] == 5:
			directions[ball] = 0

def run():
	locations[0] = 1
	locations[1] = 5
	locations[2] = 2
	directions[2] = 1
	while True:
		stepBalls()
		colorBalls()
		sleep(0.3)
		
run()
