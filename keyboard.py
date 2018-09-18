import os
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
import sys

def clear():
	os.system("clear")

def jeda(waktu):
	time.sleep(waktu)

def main():
	
	clear()
	jeda(5)

	keyboard = Controller()
	string = """Aesop was one of the great Greek writers. He is best known for his fables, stories that have a moral. They teach us something about how we should live our lives. Aesop wrote thousands of these stories. Here are a few. [ENTER] The Wolf in Sheep's Clothing [ENTER] Once upon a time, a Wolf decided to disguise the way he looked. He thought it would help him get food more easily. He put on the skin of a sheep, then he went out with the flock into the pasture. Even the shepherd was fooled by his clever costume. In the evening, the shepherd put him in with the rest of the sheep. He closed the gate and made sure it was secure before he went to bed. In the middle of the night, he came back to the fold to get some meat for the next day. Instead of a sheep, though, he grabbed the Wolf, killing him instantly. [ENTER] Those who look to harm others will be harmed themselves. [ENTER] The Bat and the Weasel [ENTER] A Bat fell on the ground and was caught by a Weasel. It begged the Weasel to spare its life, but the Weasel refused. It told the Bat that birds, by nature, were its enemy. The Bat assured him that it was not a bird, it was a mouse. The Weasel thought a moment, then set it free. A while later, the Bat fell again to the ground, and it was caught by another Weasel. It begged this Weasel not to eat him, either. The Weasel, though, said it did not like mice at all and would eat it. The Bat told the Weasel that it was not a mouse, but a bat. The second Weasel had no good answer, so he let it go. [ENTER] The Bat knew it is always wise to turn events to your advantage. [ENTER] The Lion and the Mouse [ENTER] A sleeping Lion was woken up by a Mouse running over his face. He got up angrily and caught the scared little Mouse. He was about to kill the Mouse, but it said in its squeaky little voice, \"If you would only spare my life, I would be sure to repay your kindness.\" The Lion laughed at such nonsense, but he let him go. A short time later, though, the Lion was caught by some hunters. They bound him by ropes to the ground. The Mouse recognized his roar, and he rushed over and gnawed the rope with his teeth, setting the Lion free. The Mouse said \"You laughed at the idea of my ever being able to help you. Now you know that it is possible for even a small little Mouse to help a great big Lion.\""""

	a = 1
	while a < 3:
		buffer_ = string.split()
		for i in range(len(buffer_)):
			if(buffer_[i] == "[ENTER]"):
				keyboard.press(Key.enter)
				keyboard.release(Key.enter)
				continue
			keyboard.type(buffer_[i])
			keyboard.type(" ")
			# with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
			# 	listener.join()
				# pass
			jeda(0.1)
		a += 1

main()