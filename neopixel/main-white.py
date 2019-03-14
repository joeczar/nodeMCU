import machine
import math
import neopixel
import time

PIXEL_WIDTH = 3
PIXEL_HEIGHT = 8
MAX_BRIGHT = 50.0
TIME_DIV = 500.0

np = neopixel.NeoPixel(machine.Pin(14), PIXEL_WIDTH*PIXEL_HEIGHT)

#clear all the pixels and turn them off
np.fill((0,0,0))
np.write
current = lambda: int(round(time.time()* math.pi ))
while True:
        np.fill((0,0,0))
        current = time.ticks_ms() / TIME_DIV
        for x in range(PIXEL_WIDTH):
            for y in range(PIXEL_HEIGHT):
                #v = math.sin(x*2.0+current)
                v = math.sin(1.0*(x*math.sin(current/2.0)+y*math.cos(current/3.0))+current)
                v = (v+1.0)/2.0
                np[y*PIXEL_WIDTH+x] = (0, 0, int(MAX_BRIGHT*v))

        np.write()
