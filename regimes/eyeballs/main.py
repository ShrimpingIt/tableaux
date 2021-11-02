# Driven from pin 14
# RGB is to target the PL9823
from time import sleep
from machine import Pin
from vgkits.ws2811 import *
from vgkits.random import randint


def configurePixels(num=12, pin=Pin(14), order = RGB):
    pixels = startPixels(pin=pin, num=num)
    NeoPixel.ORDER=order
    return pixels

def pause(lower=0, upper=1.0):
    sleep(lower + ( (upper - lower) / 10 * randint(10)))

def open(eyeId, color):
    setPixel(eyeId * 2, color)
    setPixel((eyeId * 2) + 1, color)
    showPixels()

def openOnly(eyeId, color):
    clearPixels()
    open(eyeId, color)

def close(eyeId):
    open(eyeId, black)

def closeAll():
    clearPixels()
    showPixels()

def randomColor():
    quantisedHue = float(randint(12))
    return hueToRgb(quantisedHue / 12)


pixels = configurePixels()
numEyes = pixels.n / 2

def randomSpiral(delay=0.2):
    for eyeId in range(numEyes):
        openOnly(eyeId, color=randomColor())
        if delay > 0:
            sleep(delay)

while True:
    openOnly(2, red)
    sleep(1.0)
    closeAll()
    sleep(1.0)
    openOnly(1, red)
    sleep(1.0)
    openOnly(2, red)
    sleep(1.0)
    closeAll()
    sleep(1.0)
    openOnly(4, red)
    sleep(1.0)
    closeAll()
    sleep(1.0)
    openOnly(5, red)
    sleep(1.0)
    openOnly(1, red)
    sleep(1.0)
    closeAll()
    sleep(1.0)
    open(2, red)
    open(3, red)
    sleep(1.0)
    open(1, red)
    sleep(1.0)
    closeAll()
    openOnly(4, red)
    sleep(1.0)
    closeAll()
    sleep(1.0)
    openOnly(5, red)
    sleep(1.0)
    closeAll()
    sleep(1.0)
    openOnly(3, red)
    sleep(1.0)
    closeAll()
    sleep(1.0)
    open(1, red)
    open(2, red)
    open(3, red)
    sleep(1.0)

    for count in range(10):
        randomSpiral()
    for count in range(10):
        randomSpiral(0)
