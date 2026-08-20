import machine
import time
from machine import Pin, PWM
trigger_pin = Pin(17, Pin.OUT) #Sets up gpio17 as an output for the trigger pin of the ultrasonic sensor
echo_pin = Pin(16, Pin.IN, Pin.PULL_DOWN)#Sets up gpio16 as an input for the echo pin of the ultrasonic sensor
digital = Pin(18,Pin.IN, Pin.PULL_UP)#Sets up gpio18 as an input for the digital pin of the sound sensor
pwm_pin = PWM(Pin(19))#Sets gpio19 as a PWM output for the buzzer

# this sets up the frequency that the pin is turned off and on (it is not duty cycle)
pwm_pin.freq(1000)

# this varaible is used to help calculate the required input from a duty cycle percentage
max = 65535


def door_open(): #Returns a value of 1 or 0 depending on if the ultrasonic sensor detects an object within 30cm
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
    distance = (duration * 0.0343) / 2 #calculates the distance using the speed of sound (343 m/s) and dividing by 2 to account for the round trip of the sound wave

    if distance < 30:  # I DONT KNOW THE DISTANCE AGGG
        return 1
    else:
        return 0
    
def heard_sound(): #Returns a value of 1 or 0 depending on if the sound sensor heard anything
    digital_value = digital.value()
    if digital_value == 0:
        return 1
    else:
        return 0
    
if __name__ == "__main__":
    while True:
        heard_sound()
        sound = heard_sound() #Checks and stores the value of the sound sensor
        door_open()
        move = door_open() #Checks and stores the value of the ultrasonic sensor
        print("I am running")
        if sound == 0:
            for i in range(10): #The for loop is used to check the ultra sonic sensor 10 times to continually check if the door is open or not
                print("I heard a sound")
                door_open()
                if door_open() == 1:
                    print("Door!")
                    time.sleep(4) #extra time to allow the door to be open longer if it was detected as to not buzz if somebody successfully knocked.
                time.sleep_us(1000)
        if move == 1: #If it detects that the door is open and it didnt hear a sound recently it plays a buzzer to alert the user that the door was opened.
            print("Youre so evil that youre kinda like a villain")

            PWM_value = int(0.5 * max)

            pwm_pin.duty_u16(PWM_value)
            time.sleep(5)
            pwm_pin.duty_u16(0)

