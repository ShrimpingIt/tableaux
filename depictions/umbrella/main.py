from os import urandom
from time import sleep
from neopixel import NeoPixel
from machine import Pin
from math import floor

dataPin = Pin(13)
ledCount = 27
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
	
blue = (0,0,255)
			
sequences = [
	[0],
	[17,1],
	[18,2,16],
	[19,3,15],
	[20,4,14,12],
	[21,5,13,11],
	[23,6,10],
	[24,7,9],
	[25,8],
	[26],
]

positions = [-1 for entry in sequences]

under = [
	3, 15, 
	4, 14, 12,
	5, 13, 11,
	6, 10
]

#sheltered = under
sheltered = []

d0 = Pin(16, Pin.OUT)
d1 = Pin(5, Pin.OUT)

d0.high()
d1.high()


'''
d1 = Pin(5, Pin.OUT)
pwm1 = PWM(d1)
pwm1.freq(1000)
pwm1.duty(256)
ramp = range(0,1024, 8)
while True:
	for duty in ramp:
		pwm1.duty(duty)
		sleep(0.05)
	for duty in reversed(ramp):
		pwm1.duty(duty)
		sleep(0.05)
'''

def run():	
	
	while True:
		blank()				
	
		for index, sequence in enumerate(sequences):
			# retrieve activity for this drop
			position = positions[index]

			if position == -1:
				# inactive drops sometimes become active (at 0)
				if rand_int(2) == 0:
					position = 0
			else:
				position = position + 1 # previously active drops fall one more step
				if position == len(sequence): # drops falling off the bottom become inactive
					position = -1
				elif sequence[position] in sheltered: # drops going into sheltered area become inactive
					position = -1
					
			# light any active lights
			if position != -1:
				pixel = sequence[position]
				np[pixel] = blue
				
			# store activity for this drop for next time round loop
			positions[index] = position
			
		np.write()
		sleep(0.05)
		
run()
