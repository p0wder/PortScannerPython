"""
Author: Scott C Gramig
Program: Simple port scanner in python
"""

import socket
import sys

# get IP from user
hostAddr = raw_input("Enter Host IP to scan (ex. 127.0.0.1): ")
hostIP = socket.gethostbyname(hostAddr)

print "\n ----------- Performing port scan on %s ------------" % hostAddr

# looping through port 1 - 10001
# change port range in the for loop to your pref
try:
	for port in range (1, 10001):
		# Create a TCP/IP socket and connect to it
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		openPort = sock.connect_ex((hostIP, port))
	
		if openPort == 0:
			print "Port %d is open" % port
		sock.close();

# error handling exceptions
except socket.error:
	print "Could not connect to IP"
	sys.exit()

except KeyboardInterrupt:
	print "Program exiting!"
	sys.exit()

except socket.error:
	print "Unable to resolve host"
	sys.exit()
