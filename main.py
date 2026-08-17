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

while True:
    def volume():
        while True:
            #read pin xx and output like 1 or smth when it detects smth
            

    def movement():
        while True:
        #Read pin xx and aoutput smth when smths distance changes