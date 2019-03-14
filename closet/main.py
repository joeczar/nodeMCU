from machine import Pin
import time

DOOR  = Pin(0, Pin.IN, Pin.PULL_UP)
LID  = Pin(2, Pin.IN, Pin.PULL_UP)
SWITCH0 = Pin(5, Pin.OUT)
SWITCH1 = Pin(4, Pin.OUT)

def dooropen():
        return DOOR.value()

while True:
    first = DOOR.value()
    time.sleep(0.01)
    second = DOOR.value()
    if first and not second:
        SWITCH1.off()
    elif not first and second:
        SWITCH1.on()
