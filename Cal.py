import pyttsx3
import speech_recognition
import wolframalpha
try:
    from config import WOLFRAM_API_KEY_1, VOICE_RATE, VOICE_INDEX
except ImportError:
    print("Warning: config.py not found. Using default values.")
    WOLFRAM_API_KEY_1 = "LR33QE-LUP5Q99YK4"
    VOICE_RATE = 200
    VOICE_INDEX = 0


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[VOICE_INDEX].id)
Assistant.setProperty('rate', VOICE_RATE)

def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f": {audio}")
    Assistant.runAndWait()

def Wolfram(query):
    api_key = WOLFRAM_API_KEY_1
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        Answer = next(requested.results).text
        return Answer
    except:
        Speak("Sorry sir but the value is not answerable!")



def calc(query):
    Term = str(query)
    Term = Term.replace("ERA"," ")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("multiply","*")

    Final = str(Term)
    
    try: 
        result = Wolfram(Final)
        print(f"{result}")
        Speak(result)

    except:
        Speak("Sorry sir the query is not ansewerable!")
