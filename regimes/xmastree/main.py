from machine import Pin
from time import sleep
from uos import urandom

import ujson as json

config = {}

pins = [
    Pin(16),
    Pin(5),
    Pin(4),
    Pin(0),
    Pin(2),
    Pin(14),
    Pin(12),
    Pin(13),
    Pin(15),
    Pin(3),
    Pin(1),
]

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

numLights = 16
byteCount = numLights // 8
backBytes = [0 for pos in range(byteCount)]


def latch():
    latchPin.high()
    latchPin.low()


def clock():
    clockPin.high()
    clockPin.low()


def writeByte(val):
    bit = 1
    for step in range(8):
        if val & bit != 0:
            dataPin.high()
        else:
            dataPin.low()
        clock()
        bit = bit << 1


def send(lit):
    if (lit):
        dataPin.high()
    else:
        dataPin.low()
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


def loadConfig():
    with open("config.json", "r") as f:
        return json.loads(f.readall())


def saveConfig(config):
    with open("config.json", "w") as f:
        f.write(json.dumps(config))


def getConfigValue(name):
    try:
        config = loadConfig()
    except:
        config = {}
    return config[name]


def setConfigValue(name, value):
    try:
        config = loadConfig()
    except:
        config = {}
    config[name] = value
    saveConfig(config)


def countBoots():
    try:
        bootcount = getConfigValue('bootcount')
    except KeyError:
        bootcount = 0
    bootcount += 1
    setConfigValue('bootcount', bootcount)
    return bootcount


treeLeaves = [14]
treeLights = [15]
star = [13]
tree = treeLeaves + treeLights + star

present0 = [11, 7]
present1 = [0, 9]
present2 = [3, 1]
present3 = [5, 6, 2]

presents = present0 + present1 + present2 + present3

bottle = [8]
cane = [10, 12]

digits = [4]


def treeSequence():
    turnOff(range(numLights))
    turnOn(treeLeaves + digits)
    sleep(12)
    turnOff(digits)
    sleep(2)
    turnOn(treeLights)
    sleep(2)
    turnOn(star)
    sleep(6)
    for entry in [present1, bottle, cane, present2, present0, present3, digits]:
        turnOn(entry)
        sleep(1.5)
    sleep(12)


def animate():
    while True:
        treeSequence()


def illuminate():
    turnOn(range(numLights))


if countBoots() % 2 == 0:
    animate()
else:
    illuminate()
