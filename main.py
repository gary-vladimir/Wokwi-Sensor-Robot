from led import LED
from button import Button
from buzzer import Buzzer
from stepper import Stepper
from utime import sleep

my_led = LED(12)
my_btn = Button(27)
my_buzz = Buzzer(15)
leftWheel = Stepper(13, 14)
rightWheel = Stepper(19, 18)


my_led.on()
my_btn.wait_button_press()
my_led.off()
my_buzz.beep_once()

for i in range(20):
    leftWheel.move_one_step(1)
    rightWheel.move_one_step(1)

"""
while True:
  if my_btn.is_pressed():
    my_led.on()
    my_buzz.beep_once()
  else:
    my_led.off()

"""
