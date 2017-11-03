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

dataPin.value(0)
latchPin.value(0)
clockPin.value(0)

delay = 1

numLights = 8
byteCount = numLights // 8
backBytes = [0 for pos in range(byteCount)]


def latch():
    latchPin.value(1)
    latchPin.value(0)


def clock():
    clockPin.value(1)
    clockPin.value(0)


def writeByte(val):
    bit = 1
    for step in range(8):
        if val & bit != 0:
            dataPin.value(1)
        else:
            dataPin.value(0)
        clock()
        bit = bit << 1


def send(lit):
    if (lit):
        dataPin.value(1)
    else:
        dataPin.value(0)
    for step in range(8):
        clock()
    latch()


def setLight(pos, lit, show=True):
    bytePos = pos // 8
    bitPos = pos % 8
    if lit:
        backBytes[bytePos] = backBytes[bytePos] | (1 << bitPos)
    else:
        backBytes[bytePos] = backBytes[bytePos] & ~(1 << bitPos)
    if (show):
        flip()


def flip():
    for pos in range(len(backBytes)):
        writeByte(backBytes[pos])
    latch()


def turnOn(lights):
    for pos in range(len(lights)):
        setLight(lights[pos], True, False)
    flip()


def turnOff(lights):
    for pos in range(len(lights)):
        setLight(lights[pos], False, False)
    flip()


def sequence(lights, delay=0.1, count=1):
    while True:
        for outer in range(len(lights)):
            for inner in range(len(lights)):
                setLight(lights[inner], inner == outer)
            sleep(delay)


def identify():
    for lightPos in range(numLights):
        setLight(lightPos, False)
    for lightPos in range(numLights):
        setLight(lightPos, True)
        input("Light Number " + str(lightPos))
        setLight(lightPos, False)


def walk():
    global backBytes
    while True:
        backBytes = [ord(urandom(1)) for item in backBytes]
        flip()
        sleep(1)

eyes = [0]
earsUp = [1] 
earLeft = [4]
earRight = [5]
earsDown = earLeft + earRight
glasses =  [2]
head = [3]

def sequence():
	turnOn(head + glasses + eyes)
	turnOff(earsUp); turnOn(earsDown)
	sleep(1)
	turnOff(earsDown); turnOn(earsUp)
	sleep(1)

def animate():
    while True:
        sequence()


def illuminate():
    turnOn(range(numLights))

animate()
