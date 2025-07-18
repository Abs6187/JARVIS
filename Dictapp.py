import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
try:
    from config import VOICE_RATE, VOICE_INDEX, APP_COMMANDS
except ImportError:
    print("Warning: config.py not found. Using default values.")
    VOICE_RATE = 200
    VOICE_INDEX = 0
    APP_COMMANDS = {
        "commandprompt": "cmd", "paint": "paint", "word": "winword",
        "excel": "excel", "chrome": "chrome", "vscode": "code", "powerpoint": "powerpnt"
    }

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[VOICE_INDEX].id)
engine.setProperty("rate", VOICE_RATE)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(APP_COMMANDS.keys())
        for app in keys:
            if app in query:
                os.system(f"start {APP_COMMANDS[app]}")

def closeappweb(query):
    speak("Closing, sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    else:
        keys = list(APP_COMMANDS.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {APP_COMMANDS[app]}.exe")

    