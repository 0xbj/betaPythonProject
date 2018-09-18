import os
import getpass

def main():
	os.system("clear")

	ical = getpass.getpass(prompt=" Masukkan Password Key >> ")
	print(ical)

main()