
import os
import time
from sys import platform
from datetime import date


def delete_on_linux(file):
    delete_decision = input(f"Would you like to remove this file? {file} (y/N)").lower()
    if "yes" in delete_decision or "y" in delete_decision:
        os.remove(file)
    elif "no" in delete_decision or "n" in delete_decision:
        pass
    else:
        print("Didn t understand. Can you repeat?")
        delete_on_linux(file)


def on_linux():
    print("U smartass")
    current_date = date.today()
    path = os.getcwd()
    sem = 0
    for file in os.listdir(path):
        lastmodsinceepoch = os.path.getmtime(file)
        lastmod = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lastmodsinceepoch))
        if os.path.isfile(file):
            pass
        else:
            modifiedArray = lastmod.split(" ")[0]
            modifiedArray = modifiedArray.split("-")
            current_dateArray = str(current_date).split("-")
            if current_dateArray[0] > modifiedArray[0]:
                delete_on_linux(file)
                sem = 1
            elif int(current_dateArray[1])-int(modifiedArray[1]) > 7:
                delete_on_linux(file)
                sem = 1

    if sem == 0:
        print("No old files in this directory!🐧")


def on_mac():
    print("U rich rich")


def on_windows():
    print("bAsIc")


def choose_by_platform():
    #     THIS FUNTION CHECKS THE PLATFORM USED BY THE SCRIPT
    if platform == "linux" or platform == "linux":
        on_linux()
    elif platform == "darwin":
        on_mac()
    elif platform == "win32":
        on_windows()


choose_by_platform()
