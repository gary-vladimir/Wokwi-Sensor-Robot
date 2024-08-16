import machine, utime
from machine import Pin


class Stepper:
    def __init__(self, step_pin):
        self.step_pin = Pin(step_pin, mode=Pin.OUT, pull=None)

    def move_one_step(self):
        self.step_pin.value(True)
        utime.sleep(0.001)
        self.step_pin.value(False)
        utime.sleep(0.001)
