

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
