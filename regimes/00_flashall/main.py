from time import sleep
from machine import Pin
from os import urandom
from math import floor


pinMap = (16, 5, 4, 0, 2, 14, 12, 13, 15, 3)
outputs = [Pin(gpio, Pin.OUT) for gpio in pinMap[:8]]

def show_code(name='main.py'):
	with open(name) as f:
		for line in f.readlines():
			print(line, end='')
			
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


def allOff():
	for output in outputs:
		output.low()
		
def allOn():
	for output in outputs:
		output.high()

def flashOne(pin, delay=1):
	pin.high()
	sleep(delay)
	pin.low()
	sleep(delay)

def flashAll(delay=1):
	allOn()
	sleep(delay)
	allOff()		
	sleep(delay)

def run():
	while True:
		flashAll()

run()
