#!/usr/bin/python2

import socket,time

x= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 3>2:
	msg= raw_input("Enter message to send")
	x.sendto(msg,("192.168.10.197",8881)
	
