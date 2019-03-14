from machine import Pin
import time

DOOR  = Pin(0, Pin.IN, Pin.PULL_UP)
LID  = Pin(2, Pin.IN, Pin.PULL_UP)
SWITCH0 = Pin(5, Pin.OUT)
SWITCH1 = Pin(4, Pin.OUT)

while True:
    first = LID.value()
    time.sleep(0.01)
    second = LID.value()
    if first and not second:
        print('Button pressed!')
    elif not first and second:
        print('Button released!')
