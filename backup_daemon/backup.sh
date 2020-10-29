#!/bin/bash

##################################
#######   Backup Script   ########
##################################
address="/usr/bin"

if [ -s "$address"/backup_const.sh ]; then
	echo "Find.. backup_const"
	source "$address"/./backup_const.sh
	echo "Success"
else
	echo "Error. Missing File backup_const.sh"
	exit 1
fi

# File Backup
backup_to_make="/home /etc /root /opt /boot"
# destiny to save backup
destiny="/mnt/backup"
# backup's name
day=$(date +%F)
file_name="backup_file_$day.tgz"

while true; do
	times=$(date +%R)
	if [ "$times" == "$TIME_BACKUP1" ]; then
		# Begin Start Backup
		echo "Make backup for day: $day"
		# Compress Backup Files
		tar czf $destiny/$file_name $backup_to_make

		# Finished Backup
		echo "Backup Finished $day"
		sleep 60
	else
		echo "I'm sleep to $TIME_BACKUP1"
	fi
done
