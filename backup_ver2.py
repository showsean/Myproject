import os
import time
#1. The files and directories to be backup are specified in a list.
#Example on Windows:
source = ['"C:\\My Documents"','C:\\Code']
#Example on Mac OS X and Linux:
#source = ['Users/swa/notes']
#Notice we had to use double quotes inside the string for names with spaces in it.
#
#2. The backup must be stored in a main backup directory
#Example on Windows :
target_dir = 'E:\\Backup'
#Example on Mac OS X and Linux:
#target_dir = '/Users/swa/backup'
#Remember to chang this to which folder you will be using
#Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)#make directory
#3. The files are backed up into a zip file.
#4. The current day is the name of the subdirectory in the main directory.
today = target_dir +os.sep + time.strftime('%Y%m%d')
#The current time is th name of the zip archive.
now = time.strftime('%H%M%S')
#The name of zip file
target = today +os.sep+now + '.7z'
#Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory',today
#5. We use the zip command to put the files in a zip archive
zip_command = "7z a {0} {1}".format(target,' '.join(source))
#Run the backup
print 'Zip command is:'
print zip_command
print "Running:"
if os.system(zip_command) == 0:
    print 'Successfull backup to',target
else:
    print 'Backup Failed'