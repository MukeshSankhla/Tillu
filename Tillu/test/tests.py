from speech_recognition_modue import listen_for_command

def main():
    try:
        while True:
            # Listen for a command
            command = listen_for_command()
            
            if command:
                print(f"Command received: {command}")
                # Process the command (e.g., trigger robot actions)
                if command == "forward":
                    print("Triggering forward movement.")
                elif command == "backward":
                    print("Triggering backward movement.")
                elif command == "turn left":
                    print("Triggering left turn.")
                elif command == "turn right":
                    print("Triggering right turn.")
                elif command == "show me the dance":
                    print("Triggering dance routine.")
    
    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()
