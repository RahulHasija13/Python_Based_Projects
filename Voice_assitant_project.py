# Mega Project 1 --> Jarvis
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    command = command.lower()
    
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com") 
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif command.startswith("play"):
        song=command.split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    else:
        speak("Sorry, I didn't understand that.")


if __name__ == "__main__":
    speak("Initializing Beta....")
    
    while True:
        try:
            print("Listening for 'Beta'...")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce noise
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)  # Increased timeout
            
            word = recognizer.recognize_google(audio).lower()
            print(f"Detected: {word}")  # Debugging print

            if "beta" in word:
                speak("Yes, how can I help you?")
                
                # Listen for command
                print("Listening for command...")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
                
                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")  # Debugging print
                process_command(command)

        except sr.WaitTimeoutError:
            print("No speech detected, please try again.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Please repeat.")
        except sr.RequestError:
            print("Could not connect to Google Speech Recognition service.")
        except Exception as e:
            print(f"Error: {e}")


     

