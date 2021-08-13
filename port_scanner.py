#!/bin/python3

import sys
import socket
from datetime import datetime

#define our target
if len(sys.argv)==2:
	target= socket.gethostbyname(sys.argv[1]) #translate hostename to ipv4
else:
	print("Invalid argument...\nSyntax: python3 scanner.py <ip>")

#adding a banner
print("-"*50)
print("Scanning Target "+ target)
print("Time started: "+str(datetime.now()))
print("-"*50)

try:
	for port in range(1,8000):
		s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result= s.connect_ex((target,port)) #returns an error idicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print("Couldn't connect to server")
	sys.exit()