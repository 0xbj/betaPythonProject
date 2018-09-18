import os as s
import urllib.request
import progressbar
import time
from bs4 import BeautifulSoup as soup
import downloader as dwn
import sys

buffer_nama_recitator = {}																	# global variabel untuk menampung list nama recitator
buffer_nama_surat = {}																		# global variabel untuk menampung list nama surat dari recitator yang dipilih

def downlaoadHTML():

	s.system("cls")

	print("\n\t\t == Surah Downloader ==")
	print("\t\t    == 3 Serangkai ==\n\n")

	url = "https://quranicaudio.com/"														# parent URL

	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'	# kalau ga pake ini, biasanya server tidak mau respon

	headers={'User-Agent':user_agent,} 

	request = urllib.request.Request(url,None,headers)										# mulai request ke server, ambil file htmlnya
	download_the_index = urllib.request.urlopen(request)									# buka file htmlnya
	the_index = download_the_index.read()													# read file htmlnya

	begin_parsing = soup(the_index,"lxml")													# memulai parsing, jadikan file html diatas ke format lxml agar bisa diparsing, diperlukan modul lxml

	counter = 1																				# counter untuk key directory buffer_nama_recitator
	global buffer_nama_recitator															# gunakan variabel global, agar bisa diakses dari luar fungsi

	print("\n\n\t\t++ LIST RECITATOR YANG BISA DI DOWNLOAD ++\n")

	for link in begin_parsing.find_all('a', attrs = {'class':'ttnuIA4M9MIsH3LR7pTUN'}):		# cari tag a dengan attribut class ....

		href = link.get('href')																# dari tag a, ambil href / linknya
		title = link.get_text()																# ambil text string di tag a, ini berisi judul

		print("{0} - {1}".format(counter,title))											# print ke user terminal
		buffer_nama_recitator[counter] = [title,href]										# masukkan ke dictionary buffer_nama_recitator dengan array 2 dimensi, berisi title dan link href yang didapat
		counter += 1

def sub_directory(url):

	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

	headers={'User-Agent':user_agent,} 

	request = urllib.request.Request(url,None,headers)
	download_the_index = urllib.request.urlopen(request)
	the_index = download_the_index.read()

	begin_parsing = soup(the_index,"lxml")	

	print("\n\n\t\t++ LIST SURAT YANG BISA DI DOWNLOAD ++\n")
	counter = 1

	local_nama_surat = {}
	for link in begin_parsing.find_all('div', attrs = {'class':'col-md-9 col-xs-9'}):
													
			title = link.get_text()														# ini untuk nama list suratnya

			print("{0} - {1}".format(counter,title))									
			local_nama_surat[counter] = title
			counter += 1

	counter = 1
	counter_index = 1
	local_link_surat = {}
	for link in begin_parsing.find_all('a', attrs = {'class':'_1SVM-0tZyIzXklpVqixa6j _3SAGkAUWsBI8dgW73iv0rH _18jCXzG3xrUhu4K2ZWmmml','target':'_blank'}): # looping untuk link href setiap nama suratnya

		href = link.get('href')														
		if(counter % 2 == 0):																									# setiap angka genap, akan di masukkan ke var surat
			local_link_surat[counter_index] = href																				# kalau angka ganjil isinya cuman spam ga jelas
			counter_index += 1
		else:
			pass
		counter += 1

	global buffer_nama_surat
	for i in local_link_surat.keys():

		buffer_nama_surat[i] = [local_nama_surat[i],local_link_surat[i]]														# masukkan hasil dari 2 looping diatas ke akhir variabel global ini

def main():
	
	downlaoadHTML()

	pilihan_recitator_user = int(input("\n\t[?] Masukkan 1 Angka Recitator : "))												# masukkan angka recitator
	print("\n\n")
	sub_directory("https://quranicaudio.com{0}".format(buffer_nama_recitator[pilihan_recitator_user][1]))						# assign value pilihan user ke fungsi sub directory untuk mencari list surat dari recitator tersebut

	print("\n\t")
	_input = input("\n\t[?] Masukkan list Surat (eg: 100 - 101)(110) : ")														# tampilkan form input ke user

	inputSplit = _input.split()																									# split input jadi array agar bisa di parsing sendiri
	indexBNumber = {}
	getIndex = {}
	indexANumber = {}
	indexNotNumber = []

	indexDict = 1
	# indexNot = 1
	for i in range(len(inputSplit)):
		if("-" == inputSplit[i]):																								# parsing untuk range

			indexBNumber[indexDict] = int(inputSplit[i-1])
			getIndex[indexDict] = inputSplit[i]
			indexANumber[indexDict] = int(inputSplit[i+1])

			indexDict += 1
		if(len(inputSplit) == 1):
			indexBNumber[indexDict] = int(inputSplit[i])																		# parsing untuk satu nilai yang mau di download
			indexANumber[indexDict] = int(inputSplit[i])
		# if("!" == inputSplit[i]):
		# 	indexNotNumber[indexNot] = int(inputSplit[i + 1])
		# 	indexNot += 1
		else:
			pass

	print("\n\n\n\n\t\t ++ PROSES DOWNLOAD DI MULAI ++\n")


	haha = dwn._3_Sekawan()																										# membuat objek dari class file downloader.py
	counterArray = 1
	while counterArray <= len(indexBNumber):																					# membuat parent looping
		while indexBNumber[counterArray] <= indexANumber[counterArray]:															# child looping untuk mendownload file yang sudah di tentukan
			# if(indexBNumber[counterArray] == indexNotNumber[counterArray]):
			# 	continue
			haha._request(buffer_nama_surat[indexBNumber[counterArray]][1],indexBNumber[counterArray],buffer_nama_surat[indexBNumber[counterArray]][0],buffer_nama_recitator[pilihan_recitator_user][0])
			indexBNumber[counterArray] += 1
		print("\n")
		counterArray += 1


	print("\n\n\t[-] Program Selesai, Terima Kasih Telah Menggunakan Software Kami :D")
	time.sleep(3)
	sys.exit()



while True:
	try:
		main()

	except KeyboardInterrupt:
		print("\n\n\n\t[!] Program Akan Keluar Secara Paksa")
		time.sleep(3)
		sys.exit()
	except ValueError:
		print("\n\n\n\t[!] Nilai Yang Diberikan Tidak Benar, Program Akan Keluar")
		time.sleep(3)
		sys.exit()
	except TypeError:
		print("\n\n\n\t[!] Nilai Yang Diberikan Tidak Benar, Program Akan Keluar")
		time.sleep(3)
		sys.exit()
	except KeyError:
		print("\n\n\n\t[!] Nilai Yang Diberikan Tidak Benar, Program Akan Keluar")
		time.sleep(3)
		sys.exit()