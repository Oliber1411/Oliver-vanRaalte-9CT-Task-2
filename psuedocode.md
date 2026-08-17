WHILE TRUE
    volume = CALL volume
    distance =  CALL distance
    IF distance != 1 THEN
        IF volume == 1:
            WAIT 30 seconds
        ELSE:
                buzzer
        END IF
END WHILE

volume:

digital_output = READ digital output of microphone
RETURN digital_output

distance:

SET trigger_pin = 0 (off)
WAIT 0.1 seconds
SET trigger_pin = 1 (on)
WAIT 2 micro seconds
SET trigger_pin = 0
WHILE echo_pin is off
    pulse_start = time in millieseconds
WHILE echo_pin is off
    pulse_end = time in millieseconds
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17165 / 1000000
IF distance < 500 (i dont know the value yet) THEN
    door_open = 1
else 
    door_open = 0
RETURN digital_output