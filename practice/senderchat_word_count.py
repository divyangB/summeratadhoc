#! /usr/bin/python2
import socket,time



#initialising hi_count,hello_count from zero



s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg=[]
while 1:
	
	msg=raw_input("Enter the message to send: ")
	a.append(msg)
	s.sendto(msg,("127.0.0.1",8888))
	s.recvfrom
	#print a
	count(a)
	
#taking only 5 elements at a time
	#if len(a)==5:
	#	break

	


#iterating to find the new count



print "no. of times hi is repeated: ",hi_count
print "no. of times hello is repeated: ",hello_count
	

