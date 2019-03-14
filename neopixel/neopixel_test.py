
import machine
import math
import neopixel
import time

PIXEL_WIDTH = 1
PIXEL_HEIGHT = 144

np = neopixel.NeoPixel(machine.Pin(14), PIXEL_WIDTH*PIXEL_HEIGHT)

#clear all the pixels and turn them off
np.fill((0,0,0))
np.write
current = lambda: int(round(time.time()* 10 ))
while True:
        np.fill((0,0,0))
        current = time.ticks_ms() / 200.0
        for x in range(PIXEL_WIDTH):
            for y in range(PIXEL_HEIGHT):
                v = math.sin(x*10+current)
                v = (v+1.0)/2.0
                np[y*PIXEL_WIDTH+x] = (int(25.0*v), 0, 0)

        np.write()
