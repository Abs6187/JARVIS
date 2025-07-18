from tkinter import *  # pip install tkinter
from PIL import Image, ImageTk, ImageSequence  # pip install Pillow
import time
import pygame  # pip install pygame
from pygame import mixer
import os
try:
    from config import INTRO_WINDOW_SIZE, INTRO_GIF_SPEED, INTRO_MUSIC_FILE, INTRO_GIF_FILE
except ImportError:
    print("Warning: config.py not found. Using default values.")
    INTRO_WINDOW_SIZE = "1000x500"
    INTRO_GIF_SPEED = 0.05
    INTRO_MUSIC_FILE = "Startup2.mp3"
    INTRO_GIF_FILE = "ironsnap2.gif"

mixer.init()

root = Tk()
root.geometry(INTRO_WINDOW_SIZE)

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    
    # Check if GIF file exists
    if not os.path.exists(INTRO_GIF_FILE):
        print(f"Warning: {INTRO_GIF_FILE} not found. Skipping intro animation.")
        root.destroy()
        return
        
    img = Image.open(INTRO_GIF_FILE)
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    
    # Check if music file exists before playing
    if os.path.exists(INTRO_MUSIC_FILE):
        mixer.music.load(INTRO_MUSIC_FILE)
        mixer.music.play()
    else:
        print(f"Warning: {INTRO_MUSIC_FILE} not found. Playing without sound.")
    
    for img in ImageSequence.Iterator(img):
        width, height = map(int, INTRO_WINDOW_SIZE.split('x'))
        img = img.resize((width, height))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(INTRO_GIF_SPEED)
    root.destroy()

play_gif()
root.mainloop()
