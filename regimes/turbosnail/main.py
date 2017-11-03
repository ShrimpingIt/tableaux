# turbosnail suffix '0fae49'
from ws2811 import *
from time import sleep
num=24
startPixels(num=num)

def turnOn(lights, color=red, show=True):
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

tail = [21, 22, 23]
behind = [20]

while True:
	for item in range(len(spiral)):
		turnOff(spiral, show=False)
		pos = spiral[item]
		turnOn([pos])
		sleep(0.02)
