#TO DO:
#Create function that detects the current volume
#Create function that detects if an object infront of it has moved
#Create a function that plays a buzzer
#Put 'em allll together
#Important tutorials for doing these things:    2.6/2.4 2.8 2.9 2.10 3.3
#Ok wait so. I need it to detect the volume and only ring the buzzer when it doesnt detect something,##
#So I need it to be constantly reading the volume, but i also need to read the distance with the ultrasonic sensor at the same time##
#How???
#Maybe I could just like, switch between them very quickly like
# no sound. no move. no sound. no move. no sound. MOVE! BUZZ
#no sound. no move. SOUND!....(Movement takes place here but its paused).... no move. no sound. SOUND!....... etc etc? Would that work?

import machine
import time
from machine import Pin, ADC
trigger_pin = Pin(17, Pin.OUT)
echo_pin = Pin(16, Pin.IN, Pin.PULL_DOWN)
digital = Pin(18,Pin.IN, Pin.PULL_UP)
buzzer = Pin(19, Pin.OUT, value=0)


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

    if distance < 10:  # I DONT KNOW THE DISTANCE AGGG
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
        sound = heard_sound()
        movement = door_open()
        if movement == 1:
            if sound == 0:
                buzzer.value(1)
                time.sleep(7)
                buzzer.value(0)
            else:
                time.sleep(12)

