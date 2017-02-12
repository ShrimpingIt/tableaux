from time import sleep
from uos import urandom
from machine import Pin
from cockle import pins

dataPin = pins[1]
clockPin = pins[2]
latchPin = pins[3]

dataPin.init(Pin.OUT)
latchPin.init(Pin.OUT)
clockPin.init(Pin.OUT)

dataPin.low()
latchPin.low()
clockPin.low()

delay = 1

def setNumLights(value):
	global numLights, backBytes
	numLights = value
	backBytes = [0 for pos in range(numLights // 8)]

def latch():
    latchPin.high()
    latchPin.low()	

def clock():
	clockPin.high()
	clockPin.low()

def shiftByte(val):
    bit = 1
    for step in range(8):
        if val & bit != 0:
            dataPin.high()
        else:
            dataPin.low()
        clock()
        bit = bit << 1

def showBits():
    for pos in range(len(backBytes)):
        shiftByte(backBytes[pos])
    latch()
        
def assignBit(pos, on, autoShow=True):
    bytePos = pos // 8
    bitPos = pos % 8
    if on:
        backBytes[bytePos] = backBytes[bytePos] | (1 << bitPos)
    else:
        backBytes[bytePos] = backBytes[bytePos] & ~(1 << bitPos)
    if(autoShow):
		showBits()
        
def turnOn(lights):
    for pos in range(len(lights)):
        assignBit(lights[pos], True, False)
    showBits()

def turnOff(lights):
    for pos in range(len(lights)):
        assignBit(lights[pos], False, False)
    showBits()

def allOn():
	turnOn(range(numLights))

def allOff():
	turnOff(range(numLights))  

def sequence(lights, delay=0.1):
    while True:
        for outer in range(len(lights)):
            for inner in range(len(lights)):
                assignBit(lights[inner], inner==outer)
            sleep(delay)

def identify():
	for lightPos in range(numLights):
		assignBit(lightPos, False)
	for lightPos in range(numLights):
		assignBit(lightPos, True)
		input("Light Number " + str(lightPos))
		assignBit(lightPos, False)

def illuminateRandom():
	global backBytes
	backBytes=[ord(urandom(1)) for item in backBytes]
	showBits()

setNumLights(16)

jointWB = [7]
onlyB = [10]
onlyW = [11]
letterB = onlyB + jointWB
letterW = onlyW + jointWB

letterE1 = [9]
letterS = [8]
letterT = [12]

letterE2 = [13]
letterN = [14]
letterD = [15]

west = letterW + letterE1 + letterS + letterT
best = letterB + letterE1 + letterS + letterT
end = letterE2 + letterN + letterD

showDelay = 1
pauseDelay = 0.5

def run():
	turnOff(range(16))
	turnOn(west + end)
	sleep(showDelay)
	turnOff(west + end)
	sleep(pauseDelay)
	turnOn(best + end)
	sleep(showDelay)
	turnOff(best + end)
	sleep(pauseDelay)
	turnOn(west + end)
	turnOn(west)
	sleep(showDelay)
	turnOff(west)
	sleep(pauseDelay)
	turnOn(best)
	sleep(showDelay)
	turnOff(best)
	sleep(showDelay)
	turnOn(west)
	sleep(showDelay)
	turnOff(west)
	sleep(showDelay)
	turnOn(best)
	sleep(showDelay)
	turnOff(best)
	sleep(showDelay)
	turnOff(range(16))

while True:
	run()
