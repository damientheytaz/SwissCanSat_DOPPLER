import os
import adafruit_sdcard
import board
import busio
import digitalio
import storage
#import userlib.main


class SD :
	def __init__ (self,spi,SD_CS):
		cs = digitalio.DigitalInOut(SD_CS)
		self.sdcard = adafruit_sdcard.SDCard(spi, cs)
		self.vfs = storage.VfsFat(self.sdcard)
		storage.mount(self.vfs, "/sd")
	
	
	def print_directory(self,path,tabs=0):
		print("Files on filesystem:")
		print("====================")
		for file in os.listdir(path):
			stats = os.stat(path + "/" + file)
			filesize = stats[6]
			isdir = stats[0] & 0x4000
			
			if filesize < 1000:
				sizestr = str(filesize) + " by"
			elif filesize < 1000000:
				sizestr = "%0.1f KB" % (filesize / 1000)
			else:
				sizestr = "%0.1f MB" % (filesize / 1000000)
			prettyprintname = ""
			for _ in range(tabs):
				prettyprintname += "   "
			prettyprintname += file
			if isdir:
				prettyprintname += "/"
			print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))
			if isdir:
				self.print_directory(path + "/" + file, tabs + 1)


