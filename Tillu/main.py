import random
import threading
import time
from pinpong.board import Pin
from robot_control import *
from facial_expressions import *
from speech_text import listen_for_command

# Initialize the touch button
touch = Pin(Pin.P24, Pin.IN)

# Lock to ensure mutual exclusion between touch and voice inputs
action_lock = threading.Lock()

reset_positions()

def random_movement_and_expression():
    """
    Perform a random movement and expression for 5 seconds or until interrupted.
    """
    with action_lock:
        print("Executing random movement and expression.")

        # Choose random movement and facial expression
        movements = [dance1, dance2, dance3, dance4, dance5, dance6, dance7, dance8, dance9, dance10, dance11, dance12, dance13]
        expressions = [angry, heart, love, loading, music, scarry, cute]

        chosen_movement = random.choice(movements)
        chosen_expression = random.choice(expressions)

        # Start movement and expression in parallel
        movement_thread = threading.Thread(target=chosen_movement)
        expression_thread = threading.Thread(target=chosen_expression)

        movement_thread.start()
        expression_thread.start()

        # Wait for 5 seconds
        start_time = time.time()
        while time.time() - start_time < 5:
            time.sleep(0.1)

        # Stop the robot and reset to blink expression
        reset_positions()
        blink()
        print("Random action completed.")

def touch_listener():
    """
    Continuously listens for the touch button to trigger random movements and expressions.
    """
    while True:
        if touch.read_digital():  # Button is pressed
            if action_lock.locked():
                print("Action in progress. Ignoring touch input.")
                continue

            time.sleep(0.2)  # Debounce
            print("Touch detected! Starting random movement and expression...")
            random_movement_and_expression()


def voice_listener():
    """
    Continuously listens for voice commands to control the robot.
    """
    while True:
        if action_lock.locked():  # Skip voice processing if an action is already running
            continue

        command = listen_for_command()
        if command:
            print(f"Voice command received: {command}")

            # Map voice commands to actions
            commands_map = {
                "forward": forward,
                "backward": backward,
                "turn left": left_turn,
                "turn right": right_turn,
                "tillu dance": random_movement_and_expression
            }

            # Execute the mapped function if available
            action = commands_map.get(command)
            if action:
                if command == "tillu dance":
                    # Run random_movement_and_expression in a separate thread
                    threading.Thread(target=random_movement_and_expression).start()
                else:
                    with action_lock:
                        action()
                        reset_positions()
                        blink()
                        print(f"Action from voice command '{command}' completed.")
            else:
                print(f"Unknown command: {command}")


def cleanup():
    """
    Cleanup function to stop the robot and perform any necessary cleanup.
    """
    print("Cleaning up resources...")
    reset_positions()
    blink()
    print("Cleanup complete.")

def main():
    """
    Main function to handle touch and voice inputs in parallel.
    """
    try:
        # Start with the blink expression
        blink()

        # Start the touch and voice listeners as daemon threads
        threads = [
            threading.Thread(target=touch_listener, daemon=True),
            threading.Thread(target=voice_listener, daemon=True),
        ]
        for thread in threads:
            thread.start()

        # Keep the main program running
        while True:
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    finally:
        cleanup()

if __name__ == "__main__":
    main()