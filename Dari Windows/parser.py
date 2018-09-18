import time
import os


os.system('cls')
input = input("\n\tMasukkan list : ")


######################### Variabel
inputSplit = input.split()
																					# split inputan user berupa string ke array
indexBNumber = {}																							# variabel untuk string sebelum '-'
getIndex = {}																								# menyimpan variabel '-'
indexANumber = {}
indexDict = 1																							# menyimpang variabel string sesudah '-'

indexSingleNumber = {}
indexSingle = 1

indexNotNumber = {}
indexNot = 1
############################

print(inputSplit)																	# DEBUG
for i in range(len(inputSplit)):
	if("-" == inputSplit[i]):																				# jika di index split ada string '-', maka:
		indexBNumber[indexDict] = int(inputSplit[i-1])														# mencari nilai sebelum '-', dengan -1
		getIndex[indexDict] = inputSplit[i]																	# get index = string '-'
		indexANumber[indexDict] = int(inputSplit[i+1])														# mencari nilai sesudah '-', dengan +1

		print(indexBNumber[indexDict],getIndex[indexDict],indexANumber[indexDict])
		indexDict += 1
	if("@" == inputSplit[i]):
		indexSingleNumber[indexSingle] = int(inputSplit[i+1])
		print(indexSingleNumber[indexSingle])
		indexSingle += 1
	if("!" == inputSplit[i]):
		indexNotNumber[indexNot] = int(inputSplit[i+1])
		print(indexNotNumber[indexNot])
		indexNot += 1
	else:
		pass

print("\n")
print(len(indexNotNumber))
print(indexNotNumber)
print("\n")

###############variabel
counterCore = 1
counterRange = 1
counterNot = 1
###############
while counterCore <= len(indexANumber):																	# ini untuk menampikan hasil dari 3 variabel penting diatas
	while indexBNumber[counterRange] <= indexANumber[counterRange]:

		if(len(indexNotNumber) >= 1):
			if(indexBNumber[counterRange] == indexNotNumber[counterNot]):
				# continue
				indexBNumber[counterRange] += 1
				# continue
				print('PASS {}'.format(counterNot))
				if counterNot <= len(indexNotNumber):
					counterNot += 1	
				# continue

		print(indexBNumber[counterRange],indexANumber[counterRange])
		indexBNumber[counterRange] += 1


