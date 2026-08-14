#Yes i jhust took this from the internet i dont careeeee i hate everything im genuinley gonna jump
# Load libraries
from machine import Pin
import time

# Initialization of GPIO16 as input and GPIO17 as output
trigger_pin = Pin(17, Pin.OUT)
echo_pin = Pin(16, Pin.IN, Pin.PULL_DOWN)

print("KY-050 Distance measurement")

# Endless loop for measuring the distance
while True:
     # Distance measurement is started using the 10us trigger signal
     trigger_pin.value(0)
     time.sleep(0.1)
     trigger_pin.value(1)

     # Now wait at the echo input until the signal has been activated 
     # Then the time is measured for how long it remains activated
     time.sleep_us(2)
     trigger_pin.value(0)
     while echo_pin.value()==0:
          pulse_start = time.ticks_us()
     while echo_pin.value()==1:
          pulse_end = time.ticks_us()
     pulse_duration = pulse_end - pulse_start

     # Now the distance is calculated using the recorded time
     distance = pulse_duration * 17165 / 1000000
     distance = round(distance, 0)

     # Serial output
     print ('Distance:',"{:.0f}".format(distance),'cm')
     time.sleep(1)