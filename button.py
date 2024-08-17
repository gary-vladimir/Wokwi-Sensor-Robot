from utime import sleep
from machine import Pin


class Button:
    def __init__(self, pin):
        self.pin = Pin(pin, mode=Pin.IN)

    def is_pressed(self):
        return self.pin.value() == 1

    def wait_button_press(self):
        while self.is_pressed() == False:
            sleep(0.01)
        return
