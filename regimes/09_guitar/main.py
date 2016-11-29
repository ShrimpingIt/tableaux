from time import sleep
from machine import Pin

pinMap = (16, 5, 4, 0, 2, 14, 12, 13, 15, 3)
outputs = [Pin(gpio, Pin.OUT) for gpio in pinMap[:8]]

guitar = outputs[1]
notes = outputs[2:5] # note, this is 2->5 not including 5
notes.reverse()

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
	sleep(delay)
	allOn()
	sleep(delay)
	allOff()

def run():
	pause = 0.5
	guitar.high()
	while True:
		for note in notes:
			note.low()
		sleep(pause)
		for note in notes:
			note.high()
			sleep(pause)

run()
