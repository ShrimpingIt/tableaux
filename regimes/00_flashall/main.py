from time import sleep
from machine import Pin

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

def flash(delay=1):
	allOn()
	sleep(delay)
	allOff()		
	sleep(delay)

def run():
	while True:
		flash()

run()
