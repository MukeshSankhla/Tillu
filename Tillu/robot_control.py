import time
from pinpong.board import Board, Pin, Servo
from pinpong.extension.unihiker import *

# Initialize the board
Board().begin()
buzzer.play(buzzer.POWER_UP, buzzer.Once)
delayTime = 0.2

# Initialize the servos
servo_hip_right = Servo(Pin(Pin.P21))
servo_hip_left = Servo(Pin(Pin.P22))
servo_foot_right = Servo(Pin(Pin.P23))
servo_foot_left = Servo(Pin(Pin.P16))

# Set rest positions
def reset_positions():
    servo_hip_right.write_angle(95)
    servo_hip_left.write_angle(85)
    servo_foot_right.write_angle(85)
    servo_foot_left.write_angle(100)

# Movement functions
def forward():
    print("Moving forward...")
    for _ in range(5):
        servo_foot_right.write_angle(65)
        servo_foot_left.write_angle(120)
        time.sleep(delayTime)
        servo_hip_right.write_angle(105)
        servo_hip_left.write_angle(75)
        time.sleep(delayTime)
        servo_foot_right.write_angle(105)
        servo_foot_left.write_angle(80)
        time.sleep(delayTime)
        servo_hip_right.write_angle(75)
        servo_hip_left.write_angle(105)
        time.sleep(delayTime)
        servo_foot_right.write_angle(85)
        servo_foot_left.write_angle(100)
        time.sleep(delayTime)
        servo_hip_right.write_angle(95)
        servo_hip_left.write_angle(85)
        time.sleep(delayTime)

def backward():
    print("Moving backward...")
    for _ in range(5):
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

def left_turn():
    print("Turning left...")
    for _ in range(5):
        servo_foot_left.write_angle(90)
        servo_foot_right.write_angle(95)
        time.sleep(delayTime)
        servo_hip_right.write_angle(95)
        servo_hip_left.write_angle(85)
        time.sleep(delayTime)
        servo_foot_left.write_angle(110)
        servo_foot_right.write_angle(75)
        time.sleep(delayTime)
        servo_hip_left.write_angle(125)
        servo_hip_right.write_angle(135)
        time.sleep(delayTime)
    reset_positions()

def right_turn():
    print("Turning right...")
    for _ in range(5):
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
    reset_positions()

# Dance modes (1 to 13)
def dance1():
    print("Dance 1: Side sway")
    for _ in range(5):
        servo_hip_right.write_angle(80)
        servo_hip_left.write_angle(100)
        time.sleep(delayTime)
        servo_hip_right.write_angle(110)
        servo_hip_left.write_angle(70)
        time.sleep(delayTime)

def dance2():
    print("Dance 2: Foot tapping")
    for _ in range(5):
        servo_foot_right.write_angle(65)
        time.sleep(delayTime)
        servo_foot_right.write_angle(85)
        time.sleep(delayTime)
        servo_foot_left.write_angle(120)
        time.sleep(delayTime)
        servo_foot_left.write_angle(100)
        time.sleep(delayTime)

def dance3():
    print("Dance 3: Hip rolling")
    for _ in range(5):
        servo_hip_right.write_angle(105)
        servo_hip_left.write_angle(75)
        time.sleep(delayTime)
        servo_hip_right.write_angle(85)
        servo_hip_left.write_angle(95)
        time.sleep(delayTime)

def dance4():
    print("Dance 4: Foot kick")
    for _ in range(5):
        servo_foot_right.write_angle(50)
        time.sleep(delayTime)
        servo_foot_right.write_angle(85)
        time.sleep(delayTime)
        servo_foot_left.write_angle(150)
        time.sleep(delayTime)
        servo_foot_left.write_angle(100)
        time.sleep(delayTime)

def dance5():
    print("Dance 5: Twist")
    for _ in range(5):
        servo_hip_right.write_angle(70)
        servo_hip_left.write_angle(110)
        time.sleep(delayTime)
        servo_hip_right.write_angle(110)
        servo_hip_left.write_angle(70)
        time.sleep(delayTime)

def dance6():
    print("Dance 6: Jump simulation")
    for _ in range(5):
        servo_foot_right.write_angle(90)
        servo_foot_left.write_angle(90)
        time.sleep(delayTime)
        servo_foot_right.write_angle(85)
        servo_foot_left.write_angle(100)
        time.sleep(delayTime)

def dance7():
    print("Dance 7: Alternate foot lift")
    for _ in range(5):
        servo_foot_right.write_angle(50)
        time.sleep(delayTime)
        servo_foot_right.write_angle(85)
        time.sleep(delayTime)
        servo_foot_left.write_angle(150)
        time.sleep(delayTime)
        servo_foot_left.write_angle(100)
        time.sleep(delayTime)
        

def dance8():
    print("Dance 8: Circle motion")
    for _ in range(5):
        servo_hip_right.write_angle(80)
        time.sleep(delayTime)
        servo_hip_left.write_angle(100)
        time.sleep(delayTime)
        servo_hip_right.write_angle(110)
        time.sleep(delayTime)
        servo_hip_left.write_angle(70)
        time.sleep(delayTime)

def dance9():
    print("Dance 9: Hip and foot sync")
    for _ in range(5):
        servo_hip_right.write_angle(105)
        servo_hip_left.write_angle(75)
        servo_foot_right.write_angle(50)
        servo_foot_left.write_angle(150)
        time.sleep(delayTime)
        servo_hip_right.write_angle(85)
        servo_hip_left.write_angle(95)
        servo_foot_right.write_angle(85)
        servo_foot_left.write_angle(100)
        time.sleep(delayTime)

def dance10():
    print("Dance 10: Flutter feet")
    for _ in range(5):
        servo_foot_right.write_angle(60)
        servo_foot_left.write_angle(140)
        time.sleep(delayTime / 3)
        servo_foot_right.write_angle(85)
        servo_foot_left.write_angle(100)
        time.sleep(delayTime / 3)

def dance11():
    print("Dance 11: Circular hips")
    for _ in range(5):
        servo_hip_right.write_angle(80)
        time.sleep(delayTime)
        servo_hip_left.write_angle(100)
        time.sleep(delayTime)
        servo_hip_right.write_angle(110)
        time.sleep(delayTime)
        servo_hip_left.write_angle(70)
        time.sleep(delayTime)

def dance12():
    print("Dance 12: Lift and sway")
    for _ in range(5):
        servo_hip_right.write_angle(70)
        servo_hip_left.write_angle(110)
        time.sleep(delayTime)
        servo_hip_right.write_angle(95)
        servo_hip_left.write_angle(85)
        time.sleep(delayTime)

def dance13():
    print("Dance 13: Sync stomp")
    for _ in range(5):
        servo_foot_right.write_angle(50)
        servo_foot_left.write_angle(150)
        time.sleep(delayTime)
        servo_foot_right.write_angle(85)
        servo_foot_left.write_angle(100)
        time.sleep(delayTime)
