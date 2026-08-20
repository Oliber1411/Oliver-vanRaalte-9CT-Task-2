import machine
import time
from machine import Pin, PWM
trigger_pin = Pin(17, Pin.OUT)
echo_pin = Pin(16, Pin.IN, Pin.PULL_DOWN)
digital = Pin(18,Pin.IN, Pin.PULL_UP)
pwm_pin = PWM(Pin(19))

# this sets up the frequency that the pin is turned off and on (it is not duty cycle)
pwm_pin.freq(1000)

# this varaible is used to help calculate the required input from a duty cycle percentage
max = 65535


def door_open():
    trigger_pin.value(0) #off
    time.sleep(0.1)
    trigger_pin.value(1) #on
    time.sleep_us(2)
    trigger_pin.value(0)

    while echo_pin.value() == 0:
        pass
    start_time = time.ticks_us() #records the time when the echo pin turns on

    while echo_pin.value() == 1:
        pass
    end_time = time.ticks_us() #records the time when the echo pin turns off

    duration = time.ticks_diff(end_time, start_time)
    distance = (duration * 0.0343) / 2

    if distance < 30:  # I DONT KNOW THE DISTANCE AGGG
        return 1
    else:
        return 0
    
def heard_sound():
    digital_value = digital.value()
    if digital_value == 0:
        return 1
    else:
        return 0
    
if __name__ == "__main__":
    while True:
        heard_sound()
        sound = heard_sound()
        door_open()
        move = door_open()
        print("I am running")
        if sound == 0:
            for i in range(10):
                print("I heard a sound")
                door_open()
                if door_open() == 1:
                    print("Door!")
                    time.sleep(4)
                time.sleep_us(1000)
        if move == 1:
            print("Youre so evil that youre kinda like a villain")

            PWM_value = int(0.5 * max)

            pwm_pin.duty_u16(PWM_value)
            time.sleep(5)
            pwm_pin.duty_u16(0)

