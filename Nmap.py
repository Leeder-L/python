import socket
import subprocess

ip = input ("Enter an IP address, e.g 192.168.1.1: ")
print("IP address: " + ip + "/24" + "\n")

for port in range (1,26):
    scan = socket.socket()
    scanResult = scan.connect_ex((ip,port))
    
    
    if scanResult == 0:
        print(ip + ":" + str(port) + " is open")
        scan.close()