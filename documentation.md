

# Requirements outline

### The Need
My parents keep walking into my room without knocking, this doesnt matter at all but its the principal of the invasion of privacy. I need a way to make sure that I know when they enter
### Proposed Solutions
A device that detects wether or not a loud sound, such as kocking on a door has been made in the last three seconds, if there hasnt been a knock an ultrasonic sensor will detect if the door opens and play a loud sound to alert the person in the room. 

A device that detects movement outside the room and plays a loud sound if someone gets clost to the door
### Key Actions
 - Constantly detects sound level
 - Detects distance from door
 - Buzzer rings loudly if theres no sound and the door opens
 
 OR

- Constantly detects movement outside
- Buzzer rings loudly if theres movement outside

 ### Functional Requirements
 Volume sensor input: Detects if volume has exceeded boundary values
 Ultrasonic sensor input: Detects if an object has moved closer
 Volume output: Plays a loud sound when the ultrasonic sensor has detected movement and the volume sensor has not detected any sound exceeding boundary values

 OR

 Ultrasonic sensor input: Detects if an object has moved infront of it
 Volume output: Plays a loud sound when the ultrasonic sensor has detected movement.

 ### Test Cases

 | Test Case | Input     | Expected Output   |
|--------- |---------- |----------------   |
|     Decently loud sound is made      |     Volume sensor detects the increase in decibles      |        Plays loud sound (in the actual program it would move onto the next subroutine, this would just be a test to see if the volume sensor is working)           |
|       Object has moved    |     Ultrasonic sensor detects that an object has moved outside of the boundary values      |        Plays loud sound            |
|      Object has moved after a sound     |      Volume sensor has detected the sound + Ultrasonic sensor has detected movement     |          Does not activate the speaker         |

OR

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|     Something has moved infront of door    |     Ultrasonic sensor detects that an object has moved outside of the boundary values      |        Plays a loud sound           |


Prototype: 
 ```Python 

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
print("Hello world!")

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
        heard_sound()
        sound = heard_sound()
        door_open()
        move = door_open()
        print("Hello world!1")
        if sound == 0:
            for i in range(10):
                print("Hello world!2")
                door_open()
                if door_open() == 0:
                    print("Hello world!3")
                    time.sleep_us(1000)
                time.sleep_us(1)
        if move == 0:
            buzzer.on()
            print("Hello world!4")
            time.sleep(7)
            buzzer.off()



 ```
 The only problem with the prototype is that the ultrasonic sensor never picked anything up.

 ### Testing and debugging:
 This (thankfully) will actually be pretty short as the only problem with the program was that the ultrasonic sensor wouldnt activate, I can easily test whether its a wiring issue or a code issue by running a very simple test of the ultrasonic sensor.

The test from the ultrasonic sensor was actually somewhat inconclusive, as it always read the distance as 1 cm no matter what way it was facing.