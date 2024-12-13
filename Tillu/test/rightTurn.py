import time
from pinpong.board import Board, Pin, Servo

# Initialize the board
Board().begin()

# Initialize the servos
servo_hip_right = Servo(Pin(Pin.P21))
servo_hip_left = Servo(Pin(Pin.P22))
servo_foot_right = Servo(Pin(Pin.P23))
servo_foot_left = Servo(Pin(Pin.P16))

# Set rest positions
servo_hip_right.write_angle(95)
servo_hip_left.write_angle(85)
servo_foot_right.write_angle(85)
servo_foot_left.write_angle(100)

delayTime = 0.2

print("Servos initialized to rest positions.")

# Function to turn left
def turn_left():
    while True:
        servo_foot_left.write_angle(90)
        servo_foot_right.write_angle(95)
        time.sleep(delayTime)
        servo_hip_right.write_angle(95)
        servo_hip_left.write_angle(85)
        time.sleep(delayTime)
        servo_foot_left.write_angle(110)
        servo_foot_right.write_angle(75)
        time.sleep(delayTime)
        servo_hip_right.write_angle(55)
        servo_hip_left.write_angle(45)
        time.sleep(delayTime)

# Main program
try:
    print("Starting left turn...")
    turn_left()

except KeyboardInterrupt:
    print("Movement interrupted. Exiting program.")

finally:
    print("Resetting to rest positions...")
    servo_hip_right.write_angle(95)
    servo_hip_left.write_angle(85)
    servo_foot_right.write_angle(85)
    servo_foot_left.write_angle(100)
    print("All servos returned to rest positions.")
