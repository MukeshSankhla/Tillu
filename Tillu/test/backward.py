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

# Function to move backward
def move_backward():
    while True:
        # Step 1: Lift the left foot
        print("Lifting left foot...")
        servo_foot_left.write_angle(120)
        servo_foot_right.write_angle(65)
        time.sleep(delayTime)
        servo_hip_left.write_angle(105)
        servo_hip_right.write_angle(75)
        time.sleep(delayTime)
        servo_foot_left.write_angle(80)
        servo_foot_right.write_angle(105)
        time.sleep(delayTime)
        servo_hip_left.write_angle(75)
        servo_hip_right.write_angle(105)
        time.sleep(delayTime)
        servo_foot_left.write_angle(100)
        servo_foot_right.write_angle(85)
        time.sleep(delayTime)
        servo_hip_left.write_angle(85)
        servo_hip_right.write_angle(95)
        time.sleep(delayTime)

# Main program
try:
    print("Starting backward movement...")
    move_backward()

except KeyboardInterrupt:
    print("Movement interrupted. Exiting program.")

finally:
    print("Resetting to rest positions...")
    servo_hip_right.write_angle(95)
    servo_hip_left.write_angle(85)
    servo_foot_right.write_angle(85)
    servo_foot_left.write_angle(100)
    print("All servos returned to rest positions.")
