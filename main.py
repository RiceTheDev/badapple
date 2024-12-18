"""
---------- Bad Apple, but in Python ----------
*   To run it, just use the "run.sh" or "run.bat"
    Not the most optimized code, but works!    
----------------------------------------------
"""

import time
import os
from playsound3 import playsound # To install the requirements, run "run.sh" or "run.bat"
import threading

def playAudio():
    playsound('badapple.mp3') # Plays the music

frame = 0

def showVideo():
    global frame
    threading.Thread(target=playAudio).start()
    for x in range(13140): # 13,140 frames 
        time.sleep(0.01667)
        os.system('clear') # Clears the screen, change to "cls" if you are on Windows.
        print(open(f"frames/frame_{frame}.txt").read()) # Prints the current frame
        frame += 1

threading.Thread(target=showVideo).start()