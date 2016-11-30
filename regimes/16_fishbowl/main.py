from time import sleep
from machine import Pin

defaultDelay = 1

pinMap = (16, 5, 4, 0, 2, 14, 12, 13, 15, 3)
outputs = [Pin(gpio, Pin.OUT) for gpio in pinMap[:8]]

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

def flashOne(index, delay=defaultDelay):
	outputs[index].high()
	sleep(delay)
	outputs[index].low()
	sleep(delay)

def flashAll(delay=defaultDelay):
	allOn()
	sleep(delay)
	allOff()		
	sleep(delay)
	
def sequenceAll(positions=range(len(outputs)), delay=defaultDelay):
	for position in positions:
		flashOne(position, delay=delay)
	
bowl = outputs[3]
fishMap = [1,2,4]
fishes = [outputs[pos] for pos in fishMap]

def run():
	
	allOff()
	bowl.high()
		
	while True:
		fishes[0].high()
		sleep(5)
		fishes[0].low()
		fishes[1].high()
		sleep(1)
		fishes[1].low()
		fishes[2].high()
		sleep(1)
		fishes[2].low()
		sleep(5)

run()
