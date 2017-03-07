import os
import time
source = ['"C:\\My Documents"','C:\\Code']
target_dir = "E:\\Backup"
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today = target_dir + os.sep +time.strftime("%Y%m%d")
now = time.strftime('%H%M%S')
comment = raw_input("Enter a comment -->")
if len(comment) == 0:
    target = today + os.sep +now + '.7z'
else:
    target = today +os.sep + now  + '_' + comment.replace(" ",'_') +'.7z'
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory',today
zip_command = '7z a {0} {1}'.format(target,' '.join(source))
print 'zip command is:'
print zip_command
print 'Running:'
if os.system(zip_command) == 0:
    print 'Successfully backup to ',target
else :
    print 'Backup Failed'