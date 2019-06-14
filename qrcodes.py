#!/usr/bin/pyhton3

import pyqrcode
from pyqrcode import QRCode


qcode=["www.linkedin.com/in/harsh-mangal-1108","https://www.instagram.com/_harsh_mangal_/"]
for i in range(len(qcode)):

	url=pyqrcode.create(qcode[i])
	url.svg("qcode"+str(i)+".svg" ,scale =8)

