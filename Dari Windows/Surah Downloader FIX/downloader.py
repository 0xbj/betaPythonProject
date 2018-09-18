import os as s
import progressbar
import time
import urllib.request

class _3_Sekawan:
	
	pbar = None
	def show_progress(self,block_num, block_size, total_size):
	    widgets=[																									# widgets untuk show progress object
	    ' [', progressbar.AdaptiveTransferSpeed(), '] ',
	    progressbar.Bar(),
	    ' (', progressbar.DataSize(), ') ',"(",progressbar.Percentage(),")",
		]

	    global pbar
	    if (self.pbar is None):																						# kalau pbar tidak ada, init default = none
	        self.pbar = progressbar.ProgressBar(maxval=total_size,widgets=widgets)									# membuat object pbar, dengan maxvalue = totalsize di argument show progress

	    downloaded = block_num * block_size																			# ini untuk mencari file yang sudah terdownload,
	    if downloaded < total_size:																					# jika file download kurang dari total file download
	        self.pbar.update(downloaded)																			# pbar akan di update
	    else:
	        self.pbar.finish()																						# kalau tidak maka akan selesai tampilan dari progress bar
	        self.pbar = None 																						# set global value pbar ke None lagi, agar bisa di gunakan lagi
	
	def _request(self,url,nomor_surat,nama_surat,path):

			print("\n\n\t [+] Downloading Surat {} - {}\n".format(nomor_surat,nama_surat))
			urllib.request.urlretrieve(url,'{0} - {1}.mp3'.format(path,nama_surat),self.show_progress)						# pemanggilan request oleh url retrieve dengan argument penyimpanan berupa path dan nama surat, 
																															# dan juga ada funsgi show program yang akan memanggil fungsi show progress diatas 
