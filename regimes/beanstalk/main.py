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

def sequence(lights, delay=0.1, count=1):
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

castle = [4]

jackPlant = [15]
jackJump = [5]
jackChop = [6]

jackUp1=[8]
jackUp2=[11]
jackUp3=[13]

jackDown1 = [9]
jackDown2 = [7]

trunk1 = [12]
trunk2 = [10]
trunk3 = [14]

growDelay = 5
showDelay = 5
pauseDelay = 3
upDelay = 5
downDelay = upDelay

def julesrun():
	turnOff(range(16))
	turnOn(jackPlant)
	sleep(showDelay)
	turnOff(jackPlant)
	sleep(pauseDelay)
	turnOn(trunk1)
	sleep(growDelay)
	turnOn(trunk2)
	sleep(growDelay)
	turnOn(trunk3)
	sleep(growDelay)
	turnOn(castle)
	sleep(pauseDelay)
	turnOn(jackUp1)
	sleep(upDelay)
	turnOff(jackUp1)
	turnOn(jackUp2)
	sleep(upDelay)
	turnOff(jackUp2)
	turnOn(jackUp3)
	sleep(upDelay)
	turnOff(jackUp3)
	sleep(showDelay)
	turnOn(jackDown1)
	sleep(downDelay)
	turnOff(jackDown1)
	turnOn(jackDown2)
	sleep(downDelay)
	turnOff(jackDown2)
	turnOn(jackChop)
	sleep(pauseDelay)
	turnOff(trunk1)
	sleep(pauseDelay)
	turnOff(trunk2)
	sleep(pauseDelay)
	turnOff(trunk3)
	sleep(pauseDelay)
	turnOff(castle)
	sleep(pauseDelay)
	turnOff(jackChop)
	turnOn(jackJump)
	sleep(showDelay)
	turnOff(range(16))
	sleep(showDelay)

def cefnrun():
	turnOff(range(16))
	turnOn(jackPlant)
	sleep(showDelay * 2)
	turnOff(jackPlant)
	sleep(pauseDelay)
	turnOn(trunk1)
	sleep(growDelay)
	turnOn(trunk2)
	sleep(growDelay)
	turnOn(trunk3)
	sleep(growDelay)
	turnOn(castle)
	sleep(pauseDelay)
	turnOn(jackUp1)
	sleep(upDelay)
	turnOff(jackUp1)
	turnOn(jackUp2)
	sleep(upDelay)
	turnOff(jackUp2)
	turnOn(jackUp3)
	sleep(upDelay)
	turnOff(jackUp3)
	sleep(showDelay)
	turnOn(jackDown1)
	sleep(downDelay)
	turnOff(jackDown1)
	turnOn(jackDown2)
	sleep(downDelay)
	turnOff(jackDown2)
	turnOn(jackChop)
	sleep(pauseDelay)
	turnOff(trunk1)
	sleep(pauseDelay)
	turnOff(trunk2)
	sleep(pauseDelay)
	turnOff(trunk3)
	sleep(pauseDelay)
	turnOff(castle)
	sleep(pauseDelay)
	turnOff(jackChop)
	turnOn(jackJump)
	sleep(showDelay)
	turnOff(range(16))
	sleep(showDelay)
	
while True:
	cefnrun()
