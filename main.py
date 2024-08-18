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


def get_steps_from_distance(distance):
    wheelDiameter = 6  # cm
    wheelPerimeter = wheelDiameter * 3.141519
    return distance * 200 / wheelPerimeter


while True:
    my_led.off()
    oled.clear()
    oled.text("Press button", 1, 2)
    oled.text("To Start", 1, 3)
    oled.show()
    my_btn.wait_button_press()
    my_buzz.beep_once()
    distance = ultrasonic.distance_cm()
    oled.clear()
    oled.text(str(distance) + "cm", 10, 2)
    target_steps = get_steps_from_distance(distance)
    oled.text("Steps> " + str(target_steps), 10, 3)
    oled.show()
    current_steps = 0
    success = True

    while current_steps < target_steps:
        values = mpu.get_values()
        if values["AcY"] > 12000 or values["AcY"] < -12000:
            success = False
            break
        leftWheel.move_one_step(0)
        rightWheel.move_one_step(1)
        current_steps += 1

    if success:
        my_buzz.beep_once()
        oled.clear()
        oled.text("REACHED", 10, 3)
        oled.show()
    else:
        my_led.on()
        oled.clear()
        oled.text("TILTED", 10, 3)
        oled.show()
        my_buzz.beep_once()
        sleep(0.2)
        my_buzz.beep_once()
        sleep(0.2)
        my_buzz.beep_once()

    sleep(2)
