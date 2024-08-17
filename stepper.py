import machine, utime
from machine import Pin


class Stepper:
    def __init__(self, step_pin, dir_pin):
        self.step_pin = Pin(step_pin, mode=Pin.OUT, pull=None)
        self.dir_pin = Pin(dir_pin, mode=Pin.OUT, pull=None)

    def move_one_step(self, direction):
        self.dir_pin.value(direction)
        self.step_pin.value(True)
        utime.sleep(0.001)
        self.step_pin.value(False)
        utime.sleep(0.001)
