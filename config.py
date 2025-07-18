# JARVIS Configuration File
# This file contains default configuration that works out of the box

# Wolfram Alpha API Keys (You should replace these with your own)
WOLFRAM_API_KEY_1 = "LR33QE-LUP5Q99YK4"  # Replace with your API key
WOLFRAM_API_KEY_2 = "UQ4E6L-64JWP8VLVT"  # Replace with your API key

# Voice Settings
VOICE_RATE = 200  # Speech rate (words per minute)
VOICE_INDEX = 0   # Voice index (0 for male, 1 for female on most systems)

# Audio Settings
INTRO_GIF_SPEED = 0.05  # Seconds between frames in intro
INTRO_MUSIC_FILE = "Startup2.mp3"
ALARM_MUSIC_FILE = "music.mp3"

# Window Settings
INTRO_WINDOW_SIZE = "1000x500"

# Focus Mode Settings
BLOCKED_WEBSITES = [
    "www.facebook.com",
    "facebook.com", 
    "www.instagram.com",
    "instagram.com",
    "youtube.com",
    "www.youtube.com"
]

# Application Dictionary for Voice Commands
APP_COMMANDS = {
    "commandprompt": "cmd",
    "paint": "paint", 
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt"
}

# File Paths
FOCUS_DATA_FILE = "focus.txt"
ALARM_DATA_FILE = "Alarmtext.txt"
INTRO_GIF_FILE = "ironsnap2.gif"