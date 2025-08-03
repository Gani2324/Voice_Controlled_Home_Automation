
import speech_recognition as sr
import pyttsx3
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

speak("Voice control started. Say turn on light or turn off light.")

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Command: {command}")
            if "turn on light" in command:
                speak("Turning on the light.")
                print("Light ON")
            elif "turn off light" in command:
                speak("Turning off the light.")
                print("Light OFF")
            elif "stop" in command:
                speak("Stopping voice control.")
                break
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
