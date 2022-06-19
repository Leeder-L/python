import subprocess as sp
network = input ("enter first 3 octects of IP ")
print ("network address:" + network + ".0/24")

for host in range (1, 255):
    ip = network + "." +str (host)
    status, result = sp.getstatusoutput ("ping" + ip)

    if ("TTL" in result):
    
    
        print (ip +"is used")