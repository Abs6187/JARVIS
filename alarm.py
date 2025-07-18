import pyttsx3
import datetime
import os 
try:
    from config import VOICE_RATE, VOICE_INDEX, ALARM_DATA_FILE, ALARM_MUSIC_FILE
except ImportError:
    print("Warning: config.py not found. Using default values.")
    VOICE_RATE = 200
    VOICE_INDEX = 0
    ALARM_DATA_FILE = "Alarmtext.txt"
    ALARM_MUSIC_FILE = "music.mp3"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[VOICE_INDEX].id)
engine.setProperty("rate", VOICE_RATE)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def run_alarm():
    if not os.path.exists(ALARM_DATA_FILE):
        print(f"Error: {ALARM_DATA_FILE} not found.")
        return
        
    extractedtime = open(ALARM_DATA_FILE, "rt")
    time = extractedtime.read()
    Time = str(time)
    extractedtime.close()

    deletetime = open(ALARM_DATA_FILE, "r+")
    deletetime.truncate(0)
    deletetime.close()

    def ring(time):
        timeset = str(time)
        timenow = timeset.replace("jarvis", "")
        timenow = timenow.replace("set an alarm", "")
        timenow = timenow.replace(" and ", ":")
        Alarmtime = str(timenow)
        print(Alarmtime)
        while True:
            currenttime = datetime.datetime.now().strftime("%H:%M:%S")
            if currenttime == Alarmtime:
                speak("Alarm ringing, sir")
                if os.path.exists(ALARM_MUSIC_FILE):
                    os.startfile(ALARM_MUSIC_FILE)
                else:
                    print(f"Warning: {ALARM_MUSIC_FILE} not found.")
            elif currenttime + "00:00:30" == Alarmtime:
                exit()

    ring(time)

if __name__ == "__main__":
    run_alarm()
