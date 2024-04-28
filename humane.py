import RPi.GPIO as GPIO
import speech_recognition as sr
import pyttsx3

from src.service.GeminiService import GeminiService


class Humane:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.BUTTON_PIN = 2
        GPIO.setup(self.BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.recognizer = sr.Recognizer() 
        self.gemini_service = GeminiService()
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('volume', 1.0)
        self.tts_engine.setProperty("rate", 178)

    def pin(self):
        print("Pinned")
        while True:
            if GPIO.input(self.BUTTON_PIN) == GPIO.LOW:
                while GPIO.input(self.BUTTON_PIN) == GPIO.LOW:
                    print("Button Pressed")
                    with sr.Microphone() as source:
                        print("Listening...")
                        self.recognizer.adjust_for_ambient_noise(source)
                        audio = self.recognizer.listen(source)
                        print("Recognizing...")
                        try:
                            speech = self.recognizer.recognize_google(audio)
                            print("You said: " + speech)
                            response = self.gemini_service.converse(speech)
                            self.tts_engine.say(response['answer'])
                            self.tts_engine.runAndWait()
                        except sr.UnknownValueError:
                            print("Google Speech Recognition could not understand audio")
                        except sr.RequestError as e:
                            print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == '__main__':
    humane = Humane()
    humane.pin()
