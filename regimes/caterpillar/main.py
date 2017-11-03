#  caterpillar suffix '0fa8f3''
from ws2811 import *
from time import sleep
num=12
startPixels(num=num)

def turnOn(lights, color=red, show=True):
	for light in lights:
		setPixel(light, color, show=False)
	if show:
		showPixels()
		
def turnOff(lights, show=True):
	turnOn(lights, color=black, show=show)

# counted from the centre 0 to the outside 0-20 = 21 lights
pairs = [
	[11, 10],
	[9, 8],
	[7, 6],
	[5, 4],
	[3, 2],
	[1, 0],
]

colors = [ yellow, red, blue, green, white, yellow]

forward = [True for pair in pairs]

while True:
	for step in range(2):
		forward = [not(val) for val in forward] # switches legs
		for leg,pair in enumerate(pairs):
			turnOff(pair, show=False)
			if forward[leg]:
				setPixel(pair[0], colors[leg])
			else:
				setPixel(pair[1], colors[leg])
			sleep(0.1)
		sleep(0.3)
