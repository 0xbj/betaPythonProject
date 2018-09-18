import getpass
import pyAesCrypt
from cryptography.fernet import Fernet
import hashlib
import os
import time
import sys

def main():
	os.system("cls")

	print("\n\t\t ====== Password Store ======\n")

	userInput = getpass.getpass(prompt='\n [?] Enter Password >> ')
	hashInput = hashlib.sha512(userInput.encode()).hexdigest()

	keyInput = getpass.getpass(prompt='\n [?] Enter USB Key >> ')

	if(hashInput == keyInput):
	# if(True):
		os.system("cls")
		print("\n [+] LOGIN SUCCESS\n");time.sleep(2)
		userChoice()
		# with open("hasil.txt",'r') as file_read:
		# 	text = file_read.read()
		# 	print("\n\n{}".format(text))
		# 	file_read.close()
	else:
		os.system("cls")
		print("\n\n\t [-] LOGIN FAILED")
		time.sleep(3)
		main()

def userChoice():
	try:
		os.system("cls")
		print("\n\n\t## Standard Operation ##")
		print("[1] Encrypt / Decrypt String")
		print("[2] Encrypt / Decrypt File")
		print("\n\t## Advance Operation ##")
		print("[3] Encrypt String and File")
		print("[4] Decrypt String and File")

		userInput = input("\n\t [?] Enter Your Choice >> ")
		if(userInput == "1"):
			encryptDecryptString()
		elif(userInput == "2"):
			encryptDecryptFile()
		elif(userInput == "3"):
			encryptStringAndFile()
		elif(userInput == "4"):
			# decryptFile()
			pass
		else:
			os.system("cls")
			print("\n [-] ERROR, Must Assign 1 / 2")
			time.sleep(2)
			main()	
	except KeyboardInterrupt:
		main()

def encryptStringAndFile():
	try:
		os.system("cls")
		print("\n\t\t++ Encrypt Text ++\n")

		plainText = input("\n [?] Enter Text >> ")
		userInput = getpass.getpass(prompt='\n [?] Enter Key >> ')

		key = userInput.encode()
		initAwal = Fernet(key)
		chiperText = initAwal.encrypt(plainText.encode())

		####################################################

		bufferSize = 64 * 1024
		userInput = input('\n [?] Enter Password File >> ')
		pathInput = input('\n [?] Enter File Name >> ')
		hashInput = hashlib.sha512(userInput.encode()).hexdigest()

		# encrypt
		pyAesCrypt.encryptFile(r'{}'.format(pathInput), "{}.ENCRYPTED.aes".format(pathInput), hashInput, bufferSize)
		print("\n [+] Done");time.sleep(5);userChoice()
	except KeyboardInterrupt:
		userChoice()

def encryptDecryptFile():
	try:
		os.system("cls")

		bufferSize = 64 * 1024
		userInput = input('\n [?] Enter Password >> ')
		pathInput = input('\n [?] Enter File Name >> ')
		hashInput = hashlib.sha512(userInput.encode()).hexdigest()

		# encrypt
		pyAesCrypt.encryptFile(r'{}'.format(pathInput), "{}.ENCRYPTED.aes".format(pathInput), hashInput, bufferSize)
		# decrypt
		pyAesCrypt.decryptFile(r'{}.ENCRYPTED.aes'.format(pathInput), "{}.DECRYPTED.aes".format(pathInput), hashInput, bufferSize)

		print("\n [+] Done");time.sleep(5);userChoice()
	except KeyboardInterrupt:
		userChoice()

def encryptDecryptString():
	try:
		os.system("cls")
		print("\n\t\t++ Encrypt Text ++\n")

		plainText = input("\n [?] Enter Text >> ")
		userInput = getpass.getpass(prompt='\n [?] Enter Key >> ')

		key = userInput.encode()
		initAwal = Fernet(key)
		chiperText = initAwal.encrypt(plainText.encode())

		# print(" \n [+] Your Key :\n{}".format(key.decode()))
		print(" \n [+] Your Encrypted Text :\n{}".format(chiperText.decode()))	

		print("\n\n\t\t-- Decrypt Text --\n")
		initAwal = Fernet(key)
		plainText = initAwal.decrypt(chiperText)

		print(" [+] Your Plain Text : {}".format(plainText.decode()))

		print("\n [+] Done");time.sleep(5);userChoice()
	except KeyboardInterrupt:
		userChoice()
	except ValueError:
		os.system("cls");print("\n [x] Key Problem For Ecnryption");time.sleep(3);encryptDecryptString()


# def decryptString(key,chiperText):
# 	# os.system("cls")
# 	print("\n\t\t-- Decrypt Text --\n")

# 	# key = input("\n [?] Enter Key :\n")
# 	# chiperText = input("\n [?] Enter Chiper Text :\n")

# 	initAwal = Fernet(key)
# 	plainText = initAwal.decrypt(chiperText.encode())

# 	# print(" \n [+] Your Key :\n{}".format(key.decode()))
# 	print(" \n [+] Your Plain Text : {}".format(plainText.decode()))	

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		os.system("cls")
		print("\n\n\t\t [!] EXIT-ing SOFTWARE")
		sys.exit()