# Load libraries
from machine import Pin, ADC
from time import sleep


# Initialization of ADC0
adc = ADC(0)
# Initialization of GPIO18 as input
digital = Pin(18,Pin.IN, Pin.PULL_UP)

led = Pin(16, Pin.OUT) # Set up the onboard LED (can replace "LED" with a pin GPIO number)

print("KY-038 Microphone test")

led.value(0)

# Endless loop for reading out the ADC
while True:
    raw_value = adc.read_u16()
    # Conversion from analog value to voltage
    Volt = round(raw_value* 3.3 / 65536, 2)
    digital_value = digital.value()
    print(digital_value)
    # Serial output of the analog value and the calculated voltage
    print("Analog voltage value: " + str(Volt) + " V\t Threshold value: ", end="")

    sleep(1)

    