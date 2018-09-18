import time

input = input("\n\tMasukkan list : ")

inputSplit = input.split()																					# split inputan user berupa string ke array
indexBNumber = {}																							# variabel untuk string sebelum '-'
getIndex = {}																								# menyimpan variabel '-'
indexANumber = {}																							# menyimpang variabel string sesudah '-'

print(inputSplit)																	# DEBUG
indexDict = 1
for i in range(len(inputSplit)):
	if("-" == inputSplit[i]):																				# jika di index split ada string '-', maka:

		indexBNumber[indexDict] = int(inputSplit[i-1])														# mencari nilai sebelum '-', dengan -1
		getIndex[indexDict] = inputSplit[i]																	# get index = string '-'
		indexANumber[indexDict] = int(inputSplit[i+1])														# mencari nilai sesudah '-', dengan +1

		print(indexBNumber[indexDict],getIndex[indexDict],indexANumber[indexDict])
		indexDict += 1

	else:
		pass

print("\n\n")
# print(len(getIndex))

counterArray = 1
while counterArray <= len(getIndex):																	# ini untuk menampikan hasil dari 3 variabel penting diatas
	while indexBNumber[counterArray] <= indexANumber[counterArray]:										# jika string sebelum '-' <= string sesudah '-'
		print(indexBNumber[counterArray],indexANumber[counterArray])
		indexBNumber[counterArray] += 1
	print("\n")
	counterArray += 1
	# print(counterArray)
	# time.sleep(2)
	