from time import sleep
from machine import Pin

pinMap = (16, 5, 4, 0, 2, 14, 12, 13, 15, 3)
outputs = [Pin(gpio, Pin.OUT) for gpio in pinMap[:8]]

background = outputs[1:3]
letters = outputs[3:5]

def show_code(name='main.py'):
	with open(name) as f:
		for line in f.readlines():
			print(line, end='')

def allOff():
	for output in outputs:
		output.low()
		
def allOn():
	for output in outputs:
		output.high()

def flashOne(index, delay=1):
	outputs[index].high()
	sleep(delay)
	outputs[index].low()
	sleep(delay)

def flashAll(delay=1):
	allOn()
	sleep(delay)
	allOff()		
	sleep(delay)

def run():
	for light in background:
		light.high()
	while True:
		for light in letters:
			light.low()
		sleep(1)
		letters[0].high()
		sleep(0.5)
		letters[1].high()
		sleep(0.5)
		
run()
