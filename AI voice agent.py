import speech_recognition as sr
import pyttsx3
from datetime import datetime

class VoiceAgentSusan:
    def __init__(self):
        # Initialize speech recognition and text-to-speech engines
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.name = "Susan"

        # Configure TTS engine properties
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 1.0)  # Volume level

    def speak(self, text):
        """Convert text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Listen to user input and return the recognized text."""
        with sr.Microphone() as source:
            print(f"{self.name} is listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except sr.WaitTimeoutError:
                self.speak("I didn't hear anything. Please try again.")
            except sr.UnknownValueError:
                self.speak("I'm sorry, I didn't understand that.")
            except sr.RequestError:
                self.speak("There seems to be a problem with the speech recognition service.")
            return ""

    def greet(self):
        """Greet the user."""
        current_hour = datetime.now().hour
        if current_hour < 12:
            self.speak("Good morning! How can I assist you today?")
        elif current_hour < 18:
            self.speak("Good afternoon! How can I assist you today?")
        else:
            self.speak("Good evening! How can I assist you today?")

    def process_command(self, command):
        """Process the user's command."""
        if "time" in command:
            now = datetime.now().strftime("%H:%M")
            self.speak(f"The current time is {now}.")
        elif "name" in command:
            self.speak(f"My name is {self.name}, your virtual assistant.")
        elif "joke" in command:
            self.speak("Why don’t scientists trust atoms? Because they make up everything!")
        elif "exit" in command or "quit" in command:
            self.speak("Goodbye! Have a great day!")
            return False
        else:
            self.speak("I'm not sure how to help with that. Could you please rephrase?")
        return True

    def run(self):
        """Run the voice agent."""
        self.greet()
        active = True
        while active:
            command = self.listen()
            if command:
                active = self.process_command(command)

if __name__ == "__main__":
    susan = VoiceAgentSusan()
    susan.run()
