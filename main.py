from machine import SoftI2C, Pin, time_pulse_us
from led import LED
from button import Button
from buzzer import Buzzer
from stepper import Stepper
from utime import sleep
from hcsr04 import HCSR04
import oled
import mpu6050

my_led = LED(12)
my_btn = Button(27)
my_buzz = Buzzer(15)
leftWheel = Stepper(13, 14)
rightWheel = Stepper(19, 18)
ultrasonic = HCSR04(5, 17)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = oled.I2C(128, 64, i2c)
mpu = mpu6050.accel(i2c)

my_led.on()
my_btn.wait_button_press()
my_led.off()
my_buzz.beep_once()

for i in range(20):
    leftWheel.move_one_step(1)
    rightWheel.move_one_step(1)

my_btn.wait_button_press()

for i in range(20):
    leftWheel.move_one_step(0)
    rightWheel.move_one_step(0)

my_btn.wait_button_press()

while True:
    values = mpu.get_values()
    acy = values["AcY"] / 16384
    oled.clear()
    oled.text(str(acy), 10, 3)
    oled.show()

    sleep(0.1)

"""
while True:
  if my_btn.is_pressed():
    my_led.on()
    my_buzz.beep_once()
  else:
    my_led.off()

"""
