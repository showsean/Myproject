poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!'''
#open for 'w'riting
f = open('poem.txt','w')
#write text to file
f.write(poem)
#close the file
f.close()
#if no mode is specified,'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    #Zero length indicates EOF
    if len(line) == 0:
        break
    #The 'line' already has a new line
    #at the end of each line
    #since it is reading from a file.
    print line
#close the file
f.close()