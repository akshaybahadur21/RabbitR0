from gtts import gTTS
import playsound
import os

def gtts_speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "abc.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


