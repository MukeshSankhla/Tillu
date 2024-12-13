import time
import random
from pinpong.board import Board, Pin, Servo
from threading import Thread

# Initialize the board
Board().begin()

# Initialize the servos
servo1 = Servo(Pin(Pin.P21))
servo2 = Servo(Pin(Pin.P22))
servo3 = Servo(Pin(Pin.P23))
servo4 = Servo(Pin(Pin.P16))

# Set servos to 90° during initialization
servo1.write_angle(95)
servo2.write_angle(85)
servo3.write_angle(85)
servo4.write_angle(100)
time.sleep(2)
# servo3.write_angle(60)
print("All servos initialized to 90°")

try:
    for thread in threads:
        thread.start()

    # Keep the main program running
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    print("Cleaning up...")
    for thread in threads:
        thread.join()
