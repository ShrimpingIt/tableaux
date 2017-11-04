# turbosnail suffix '0fae49'
from ws2811 import *
from time import sleep
from cockle import randint
num=25
startPixels(num=num, order=RGB)

def turnOn(lights, color=blue, show=True):
	for light in lights:
		setPixel(light, color, show=False)
	if show:
		showPixels()
		
def turnOff(lights, show=True):
	turnOn(lights, color=black, show=show)

# counted from the centre 0 to the outside 0-20 = 21 lights
spiral = [
	13,
	14,
	12,
	7,
	6, 
	5, 
	4, 
	17,
	16,
	15,
	11,
	8,
	1,
	2,
	3, 
	18,
	19,
	20,
	10,
	9,
	0,
]

tail = [22, 23, 24]
behind = [21]

spiralPos = 0
while True:
	turnOff(spiral, show=False)
	light = spiral[spiralPos]
	turnOn([light])
	for light in tail:
		setPixel(light, [int(brightness * randint(255) / 255) for brightness in orange])
	spiralPos += 1
	if spiralPos >= len(spiral):
		spiralPos = 0
