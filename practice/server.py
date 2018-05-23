#! /usr/bin/python2

import socket, time

x= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

x.bind(("127.0.0.1",9999)
while 3>2:
	data=x.recvfrom(1000)
	print "data from client: ",data[0]
	reply= raw_input("Please type your reply: ")
	x.sendto(reply,data[1])

