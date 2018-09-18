from pynput.keyboard import Key, Listener
import logging

# log_dir = ""

# logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# def on_press(key):
#     logging.info(str(key))

# with Listener(on_press=on_press) as listener:
#     listener.join()

import time;

localtime = time.localtime(time.time())
print ("Local current time :", localtime)
print(localtime[3:6])

print(time.strftime("%Y-%m-%d %H:%M:%S"))
print (time.strftime("%H:%M:%S"))