#!/usr/bin/python3
#-*- coding: utf-8 -*-
from ftplib import FTP
import os

# capture file data to connection FTP server
file=open("/usr/bin/ip_addr_ftsrvr.conf","r")
data_host=file.readlines()[0].split(':')

# get data host, user, port and passwd
host=data_host[0]
user=data_host[1]
passwd=data_host[2].replace('\n','')

# address folder to upload client
address_ftp="/home/bryan/Documents/ftp_files"

# Begin instance connection to FTP server
try:
	ftp = FTP(host, user, passwd)
	print("connection Stablished")
	print("I'm here: "+ftp.pwd())
	# redirect to Documents/ftp_files/ folder
	ftp.cwd("Documents")
	ftp.cwd("ftp_files")
	# get list old directoies
	contains_old=os.listdir(address_ftp)
	while 1:
		# get list new directories
		contains_new=os.listdir(address_ftp)
		# compare old list directory with new list directory updated
		if len(contains_old)<len(contains_new):
			# it's has new files in directory local client
			print("I find a new files for upload to ftp server")
			# verify new files and upload in array file_new
			for file_test in contains_new:
				if file_test not in contains_old:
					# open file to send and upload to ftp server
					if ftp.storbinary('STOR '+str(file_test), open(address_ftp+'/'+file_test,'rb')):
						print('File: '+str(file_test)+' uploaded SUCCESSFULLY')
					else:
						 print('Error in send File: '+str(file_test))
		else:
			# doesn't exists last changes in directory
			contains_old=contains_new
except Exception as e:
	print ("Connection failure or I have a problems to process daemon... "+str(e))