import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak_text(command):
    """
    Convert the given text into speech.
    :param command: Text to speak.
    """
    engine.say(command)
    engine.runAndWait()

# Function to listen for specific voice commands
def listen_for_command():
    """
    Continuously listens for specific voice commands and returns the recognized command.
    Recognized commands:
    - 'forward'
    - 'back'
    - 'turn left'
    - 'turn right'
    - 'dance'
    :return: The recognized command as a string, or None if no valid command is detected.
    """
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source:
            print("Listening for commands...")
            
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            
            # Listen to the user's input
            audio = recognizer.listen(source)
            
            # Recognize speech using Google Web Speech API
            recognized_text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {recognized_text}")
            
            # Check for specific commands
            commands = ["forward", "backward", "turn left", "turn right", "tillu dance"]
            for command in commands:
                if command in recognized_text:
                    speak_text(f"Executing {command}")
                    return command
            
            # If no valid command is detected
            print("No valid command detected.")
            return None

    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return None
    
    except sr.UnknownValueError:
        print("Speech not recognized. Please try again.")
        return None
