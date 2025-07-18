import pyttsx3
import datetime
try:
    from config import VOICE_RATE, VOICE_INDEX
except ImportError:
    print("Warning: config.py not found. Using default values.")
    VOICE_RATE = 200
    VOICE_INDEX = 0

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[VOICE_INDEX].id)
engine.setProperty("rate", VOICE_RATE)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")

    speak("Please tell me, How can I help you ?")

