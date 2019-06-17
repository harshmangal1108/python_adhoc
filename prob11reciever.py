#!/usr/bin/python2
#importing socket module
import socket 
#details of server
recv_ip="127.0.0.1" 
recv_port=4444 # 0 - 1024 not be used-- you can check free udp port netstat -nulp
 # creating udp socket(ip type v4(aF_INET) , uDp(SOCK_DGRAM))
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 # fitting ip and port with udp socket 

s.bind((recv_ip,recv_port))
 # recieve data from sender 
while 4>2:
	data=s.recvfrom(100) 
	print("Message from sender :",data[0])
	print("IP + PORT --> SOCKET of sender :",data[1])
	# reoly to sender
	reply=raw_input("type your reply :")
	s.sendto(reply,data[1])


s.close()
