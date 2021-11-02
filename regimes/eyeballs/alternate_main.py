# Driven from pin 14
# RGB is to target the PL9823
from time import sleep
from machine import Pin
from vgkits.ws2811 import *
from vgkits.random import randint

NeoPixel.ORDER=RGB

numPixels = 12

pixels = startPixels(pin=Pin(14), num=numPixels)

while True:
    sleep(0.25 * randint(10))
    clearPixels()
    pair = randint(numPixels // 2)
    setPixel(pair * 2, blue)
    setPixel((pair * 2) + 1, blue)
    showPixels()
    sleep(0.1 * (1 + randint(9)))
    clearPixels()
    showPixels()
