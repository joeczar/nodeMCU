from machine import Pin

DOOR  = Pin(5, Pin.IN, Pin.PULL_UP)
SWITCH0 = Pin(2, Pin.OUT)

while True:
    if DOOR.value() == 0:
        SWITCH0.on()
    else:
        SWITCH0.off()
