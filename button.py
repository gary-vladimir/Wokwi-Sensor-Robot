from utime import sleep
from machine import Pin


class Button:
    def __init__(self, pin):
        self.pin = Pin(pin, mode=Pin.IN)

    def is_pressed(self):
        print(self.pin.value())
        return self.pin.value() == 1
