from machine import Pin
from time import sleep

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


byteCount = 4


dataPin = pins[1]
latchPin = pins[2]
clockPin = pins[3]

dataPin.init(Pin.OUT)
latchPin.init(Pin.OUT)
clockPin.init(Pin.OUT)

dataPin.low()
latchPin.low()
clockPin.low()

backBytes = [0 for pos in range(byteCount)]

def latchBytes():
    latchPin.high()
    latchPin.low()

def writeByte(val, latch=True):
    bit = 1
    for step in range(8):
        if val & bit != 0:
            dataPin.high()
        else:
            dataPin.low()
        clockPin.high()
        clockPin.low()
        bit = bit << 1
    if latch:
        latchBytes()
        
def flip():
    for pos in range(len(backBytes)):
        writeByte(backBytes[pos], False)
    latchBytes()

def setLight(pos, lit):
    bytePos = pos // 8
    bitPos = pos % 8
    if lit:
        backBytes[bytePos] = backBytes[bytePos] | (1 << bitPos)
    else:
        backBytes[bytePos] = backBytes[bytePos] & ~(1 << bitPos)
    flip()

flip()

delay = 1

leftEye =   [25,26,27,28,24,29]
rightEye =  [19,16,17,18,20,31]

leftFoot =  [04,07]
rightFoot = [05,06]

greenRightCog =  [1,2,3]
pinkCentralCog = [13,14,15]
blueLeftCog =    [21,22,23]

leftArm =   [08,09,10,11,12]
blueSpark = [30]

lightNames = [
    None,
    "CogGreenRight0",
    "CogGreenRight1",
    "CogGreenRight2",
    "FootDownLeft",
    "FootDownRight",
    "FootUpRight",
    "FootUpLeft",
    "ArmLeft0",
    "ArmLeft1",
    "ArmLeft2",
    "ArmLeft3",
    "ArmLeft4",
    "CogPinkCentral0",
    "CogPinkCentral1",
    "CogPinkCentral2",
    "EyeRightLookRight",
    "EyeRightLookDown",
    "EyeRightLookLeft",
    "EyeRightLookUp",
    "EyeRightLookStraight",
    "CogBlueLeft0",
    "CogBlueLeft1",
    "CogBlueLeft2",
    "EyeLeftLookStraight",
    "EyeLeftLookUp",
    "EyeLeftLookRight",
    "EyeLeftLookDown",
    "EyeLeftLookLeft",
    "EyeLeftSclera",
    "BlueSpark",
    "EyeRightSclera"
]

def turnOff(lights):
    for pos in range(len(lights)):
        setLight(lights[pos], 0)

def sequence(lights, delay=0.1, count=1):
    while True:
        for outer in range(len(lights)):
            for inner in range(len(lights)):
                setLight(lights[inner], inner==outer)
            sleep(delay)

'''
while True:
    for pos in range(len(backBytes) * 8):
        print(str(pos) + " : " + str(lightNames[pos]))
        setLight(pos, 1)
        sleep(1)
        setLight(pos,0)
'''
