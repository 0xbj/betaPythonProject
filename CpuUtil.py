import os
from os import system as s
from time import sleep as t
import sys

def main():
	s('clear')
	print('\n\t\t == CPU Utillities Linux ==\n')


	print("\n    ++++++++ INFO +++++++++")	
	print(" [1] Show Current CPU Frequency")
	print(" [2] Setting Summary")
	print("\n    ++++++++ SET ++++++++++")
	print(" [3] D/E Core CPU")
	print(" [4] D/E Turbo Boost")
	print(" [5] Scaling Max CPU freq")
	
	userInput = int(input("\n\t[?] Masukkan Pilihan >> "))

	if(userInput == 1):
		pilihan1()	
	elif(userInput == 2):
		pilihan2()
	elif(userInput == 3):
		pilihan3()
	elif(userInput == 4):
		pilihan4()
	elif(userInput == 5):
		pilihan5()
	else:
		erorr_()
	

def pilihan1():
	try:
		while True:
			s("clear")
			cpu = os.popen("cat /proc/cpuinfo | grep -i MHZ")
			temp0 = os.popen("sensors | grep -i 'core 0' | head -n1 | sed -r 's/.*:\\s+[\\+-]?(.*C)\\s+.*/\\1/'")
			temp1 = os.popen("sensors | grep -i 'core 1' | head -n1 | sed -r 's/.*:\\s+[\\+-]?(.*C)\\s+.*/\\1/'")
			temp2 = os.popen("sensors | grep -i 'core 2' | head -n1 | sed -r 's/.*:\\s+[\\+-]?(.*C)\\s+.*/\\1/'")
			temp3 = os.popen("sensors | grep -i 'core 3' | head -n1 | sed -r 's/.*:\\s+[\\+-]?(.*C)\\s+.*/\\1/'")
			ram = os.popen("free -h")
			print("{} \nCore 0 = {}Core 1 = {}Core 2 = {}Core 3 = {} \n{}".format(cpu.read(),temp0.read(),temp1.read(),temp2.read(),temp3.read(),ram.read()))
			t(1)
			# s('watch -n1 "cat /proc/cpuinfo | grep MHz"')
	except KeyboardInterrupt:
		main()

def pilihan2():
	try:
		s("clear")
		print("\n ===== Cores CPU Online =====\n")
		s("cat /proc/cpuinfo | grep -i proc")

		print("\n ===== Max Cores Freq =====\n")
		for i in range(0,8):
			buffer_ = os.popen("cat /sys/devices/system/cpu/cpu{}/cpufreq/scaling_max_freq".format(i))
			bufferRead = format(int(buffer_.read()),',d')
			print("Proc {} Max Freq = {}".format(i,bufferRead))

		print("\n ===== Turbo Boost =====\n")
		command = os.popen("cat /sys/devices/system/cpu/intel_pstate/no_turbo")
		cmdRead = format(int(command.read()),',d')
		print("no_turbo = {}".format(cmdRead))
		
		if(cmdRead == "1"):
			print("Turbo Boost = Disabled")
		elif(cmdRead == "0"):
			print("Turbo Boost = Enabled")

		print("\n ===== HyperThreading =====\n")
		s("grep -H . /sys/devices/system/cpu/cpu*/topology/thread_siblings_list")
		
		t(15)
		main()
	except KeyboardInterrupt:
		main()

def pilihan3():
	try:
		s("clear")
		s("cat /proc/cpuinfo | grep -i proc")
		userInput = input("\n\t [?] Disable / Enable CPU Cores? [d/e] >> ")
		if(userInput == 'd'):
			for i in range(4,8):
				print(i)
				s("sudo bash -c 'echo 0 > /sys/devices/system/cpu/cpu{}/online'".format(i))
		elif(userInput == 'e'):
			for i in range(4,8):
				print(i)
				s("sudo bash -c 'echo 1 > /sys/devices/system/cpu/cpu{}/online'".format(i))
		else:
			erorr_()

		t(15)
		main()
	except KeyboardInterrupt:
		main()

def pilihan4():
	try:
		s("clear")
		command = os.popen("cat /sys/devices/system/cpu/intel_pstate/no_turbo")
		cmdRead = format(int(command.read()),',d')
		print("no_turbo = {}".format(cmdRead))
		
		if(cmdRead == "1"):
			print("Turbo Boost = Disabled")
		elif(cmdRead == "0"):
			print("Turbo Boost = Enabled")
		
		userInput = input("\n\t [?] Disable / Enable Turbo Boost? [d/e] >> ")
		if(userInput == 'd'):
			s("sudo bash -c 'echo 0 > /sys/devices/system/cpu/intel_pstate/no_turbo'")
		elif(userInput == 'e'):
			s("sudo bash -c 'echo 1 > /sys/devices/system/cpu/intel_pstate/no_turbo'")
		else:
			erorr_()
		t(15)
		main()
	except KeyboardInterrupt:
		main()
	

def pilihan5():
	try:
		s("clear")
		for i in range(0,8):
			buffer_ = os.popen("cat /sys/devices/system/cpu/cpu{}/cpufreq/scaling_max_freq".format(i))
			bufferRead = format(int(buffer_.read()),',d')
			print("Proc {} Max Freq = {}".format(i,bufferRead))
		userInput = int(input("\n\t [?] Masukkan Max Core Freq CPU :"))
		for i in range(0,8):
			s("echo {} | sudo tee /sys/devices/system/cpu/cpu{}/cpufreq/scaling_max_freq".format(userInput,i))
		t(15)
		main()
	except KeyboardInterrupt:
		main()

def erorr_():
	print("\n\n\t\t ERROR | Back To Main Menu")
	main()




if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:	
		print("\n\n [!] Exiting Program")
		sys.exit()

main()