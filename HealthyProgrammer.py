#Healthy Programmer
#Dhruvin Prajapati

from pygame import mixer
from datetime import datetime
from time import time

def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input(">>")
        if a == stopper:
            mixer.music.stop()
            break

def log(msg):
    with open("logs/HealthyLog.txt", "a") as f:
        f.write(f"{msg}{datetime.now()}\n")

if __name__ == '__main__':
    print("-------| Healthy Programmer |-------\n")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_sec = 1800
    eyes_sec = 1200
    exercise_sec = 3000

    while True:
        if time() - init_water > water_sec:
            print("Water drinking time, Enter 'drunk' to stop the alarm >")
            musicloop("music/water1.mp3", "drunk")
            init_water = time()
            log("Water drunk at: ")
        if time() - init_eyes > eyes_sec:
            print("Eyes exercise time, Enter 'done' to stop the alarm >")
            musicloop("music/eyes2.mp3", "done")
            init_eyes = time()
            log("Eyes relaxed at: ")
        if time() - init_exercise > exercise_sec:
            print("Physical Activity time, Enter 'done' to stop the alarm >")
            musicloop("music/gym.mp3", "done")
            init_exercise = time()
            log("Body relaxed at: ")
