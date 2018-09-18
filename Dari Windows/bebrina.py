import os
import time
import sys

os.system('cls')

print("\n\t\t== Fakhrizal Asshiddiq ==")

# input = int(input("\n\n [?] Masukkan Detik : "))
input = 90

jam = input // 3600
sisa = input % 3600

menit = sisa // 60
detik = sisa % 60

if(jam >= 1):
	print("\n\n {} : {} : {}\n".format(jam,menit,detik))
elif(jam <= 0):
	print("\n\n {} : {}\n".format(menit,detik))
else:
	print("\n ERROR")

print()

while True:
	if(jam == 0 and menit == 0 and detik == 0):
		print("\n\t\t== CountDown Complete ==")
		break
	if(detik <= 0):
		detik = 60
		if(menit - 1 <= -1):
			menit = 59
			if(jam - 1 <= -1):
				jam = 0
			else:
				jam = jam - 1
		else:
			menit = menit - 1
	
	detik = round(detik - 1,2)
	print("  {} : {} : {}\r".format(jam,menit,detik),end='')
	time.sleep(1)
	sys.stdout.flush()
	

