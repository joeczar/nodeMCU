import machine
import math
import neopixel
import time

PIXEL_WIDTH = 2
PIXEL_HEIGHT = 8
MAX_BRIGHT = 30.0
TIME_DIV = 600.0

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
                v = 0.0
                v += math.sin(x*2.0+current)
                v += math.sin(1.0*(x*math.sin(current/2.0)+y*math.cos(current/3.0))+current)
                cx = x + 3.0*math.sin(current/5.0)
                cy = y + 3.0*math.cos(current/3.0)
                v = math.sin(math.sqrt((math.pow(cx, 2.0)+math.pow(cy, 2.0))+1.0)+current)
                v = (v+1.0)/2.0
                r = math.sin(v*math.pi)
                #g = math.sin(v*math.pi+2.0*math.pi/3.0)
                #b = math.sin(v*math.pi+4.0*math.pi/3.0)
                np[y*PIXEL_WIDTH+x] = (int(MAX_BRIGHT*r), int(MAX_BRIGHT*r), int(MAX_BRIGHT*r))

        np.write()
