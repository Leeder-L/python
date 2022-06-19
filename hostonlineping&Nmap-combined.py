import socket
import subprocess as sp
network = input ("enter first 3 octects of IP ")
print (network)

for host in range (1, 255):
    ip = network + "." +str (host)
    status, result = sp.getstatusoutput("ping" + ip)

if ("TIL" in result):
    
    
    print (ip +"is used")
    
    
    #scand
    for port in range (1,1025):
    scan = socket.socket()
    scanresult = scan.connect_ex((ip,port))
    
    
    if (scanresult == 0):
        print(ip + ":" + str(port) + " is open")
        
        scan.close()