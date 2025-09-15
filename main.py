import time
import threading
from playsound3 import playsound

with open("frames.txt", "r", encoding="utf-8") as f:
    data = f.read()

frameList = data.split("\n---FRAME---\n")

def playAudio():
    playsound("badapple.mp3")

def showVideo():
    start_time = time.time()
    threading.Thread(target=playAudio, daemon=True).start()

    for i, frame in enumerate(frameList):
        target = start_time + i * (1/60)
        now = time.time()

        if target > now:
            time.sleep(target - now)

        print(frame, end="")

showVideo()
