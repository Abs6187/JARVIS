import wolframalpha
import pyttsx3
import speech_recognition
try:
    from config import WOLFRAM_API_KEY_2, VOICE_RATE, VOICE_INDEX
except ImportError:
    print("Warning: config.py not found. Using default values.")
    WOLFRAM_API_KEY_2 = "UQ4E6L-64JWP8VLVT"
    VOICE_RATE = 170
    VOICE_INDEX = 0

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[VOICE_INDEX].id)
rate = engine.setProperty("rate", VOICE_RATE)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = WOLFRAM_API_KEY_2   # Now uses config
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")

        