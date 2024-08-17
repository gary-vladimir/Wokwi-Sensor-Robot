from utime import sleep
from machine import Pin


class LED:
    def __init__(self, pin):
        self.pin = Pin(pin, mode=Pin.OUT, pull=None)
        self.pin.value(0)

    def on(self):
        self.pin.value(1)

    def off(self):
        self.pin.value(0)

    def blink(self, time):
        self.on()
        sleep(time)
        self.off()
