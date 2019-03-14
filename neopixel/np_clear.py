import neopixel
import machine

np = neopixel.NeoPixel(machine.Pin(14), 144)

np.fill((0, 0, 0))
np.write()
