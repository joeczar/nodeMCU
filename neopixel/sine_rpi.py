import time
import math
from neopixel import *


# LED strip configuration:
LED_COUNT      = 8
PIXEL_WIDTH    = 2      # Number of LED pixels.
PIXEL_HEIGHT   = 1
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

# Main program logic follows:
while True:
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    current = time.clock()
    for x in range(PIXEL_WIDTH):
        for y in range(PIXEL_HEIGHT):
            v = math.sin(x*0.05+current)
            v = (v+1.0)/2.0
            strip.setPixelColor((y*PIXEL_WIDTH+x) Color(int(155.0*v), 0, 0)
    strip.show()
