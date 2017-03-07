import os
import time
#1.The files and directories to be backed up are
#specified in alist
#Example on Windows:
source = ['"C:\My Documents"','C:\\Code']
#Example on Mac OS X and Linux:
#source = ['/Users/swa/notes']
#Notice we had to use double quates inside the string
#for names with space in it.
#2.The backup must be stored ina
#main backup directory
#Examaple on Windows:
target_dir = 'E:\\Backup'
#Example on Mac OS X and Linux
#target_dir = '/Users/swa/backup'
#Remember to change this to which folder you will be using
#3.the file s are backed up into a zip file.
#4.the name of the zip archive is the current date and time
target = target_dir + os.sep + \
time.strftime('%Y%m%d%H%M%S') + '.7z'
#create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)#make directory
#5 we use the zip command to put the files in a zip archive
zip_command = "7z a {0} {1}".format(target,
                                    '  '.join(source))
#Run the backup
print "zip command is:"
print zip_command
print "Running:"
if os.system(zip_command) == 0:
     print 'Successful backup to',target
else:
     print 'Backup FAILED'