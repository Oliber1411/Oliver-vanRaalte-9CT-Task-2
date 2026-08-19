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


from machine import Pin, ADC
from time import sleep
import utime
adc = ADC(0)
perchance = True
digital = Pin(18,Pin.IN, Pin.PULL_UP)
button = Pin(16, Pin.IN, Pin.PULL_UP)
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
mid = 1.96
max = 2
greg = 12.5
accordingtoallknownlawsofaviationthereisnowayabeeshouldbeabletofly = True
def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   return distance
def sond():
    raw_value = adc.read_u16()
    # Conversion from analog value to voltage
    Volm = round(raw_value* 3.3 / 65536, 2)
    Volt = Volm
    digital_value = digital.value()
    sleep(0.5)
    return Volt
def menu():
    while True:
        if button.value() == 0:
            print("off")
        else:
            IT = True
            if accordingtoallknownlawsofaviationthereisnowayabeeshouldbeabletofly == True:
                while IT == True:
                    ultra()
                    sond()
                    sound = sond()
                    distance = ultra()
                    print(sound)
                    print(distance)
                    if sound < mid or sound > max:
                       perchance = True
                    else:
                       perchance = False
                    if distance > greg:
                        if perchance == False:
                           print("alarm")
                    if button.value() != 0:
                        IT = False
menu()