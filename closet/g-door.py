import time
from machine import Pin

door = Pin(0, Pin.IN, Pin.PULL_UP)

def isclosed():
  return door.value()

def notify(isclosed):
  state = 'closed' if isclosed else 'opened'
  print(state)

wasclosed = isclosed()
while True:
  notify(wasclosed)
  while isclosed() == wasclosed:
    time.sleep(1)
  wasclosed = not wasclosed
