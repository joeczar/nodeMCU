from machine import Pin
import time

DOOR  = Pin(0, Pin.IN, Pin.PULL_UP)
LID  = Pin(2, Pin.IN, Pin.PULL_UP)
SWITCH0 = Pin(5, Pin.OUT)
SWITCH1 = Pin(4, Pin.OUT)

def dooropen():
        return DOOR.value()

while True:
    doorval = DOOR.value()
    olddoorval = DOOR.value
    if doorval != olddoorval and dooropen() == 0:
        SWITCH0.on()
        print('Door opened')
        time.sleep(0.5)
    else:
        SWITCH0.off()
        print('Door closed')
        time.sleep(0.5)
