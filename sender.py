#!/usr/bin/python2


import socket
recv_ip="127.0.0.1"
recv_port=4444  #0 - 1024 not be used-- you can check free udp port netstat -nulp

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)




while 4>2:
	message=raw_input("Enter a message to send  :")
	s.sendto(message,(recv_ip,recv_port))
	print(s.recvfrom(10))
