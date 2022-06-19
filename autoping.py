# Script to ping all IP addresses in a /24 subnet
import subprocess
import os

network = input ("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
print(network)

# Iterate over all usable IPs in this subnet

for host in range (1, 254):
    print("\nPinging " + network + "." + str(host))
    result=subprocess("ping -n 2 " + network + "." + str(host))
