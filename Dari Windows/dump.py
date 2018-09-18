from pyautogui import screenshot as s
import time

while True:
	timeInit = time.strftime("%S")
	print(timeInit)

	if(int(timeInit) % 5 == 0):
		print(int(timeInit))
		print()
# 	s("ical.jpg")
	time.sleep(1)