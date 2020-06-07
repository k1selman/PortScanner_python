import socket
import subprocess
import sys
from datetime import datetime

#clear the screen
subprocess.call('clear', shell=True)

#input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#banner with info
print ("-" * 60)
print ("Scanning remote host...", remoteServerIP)
print ("-" * 60)

#check when the scan started
t1 = datetime.now()

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port{}:     Open".format(port))
        sock.close()

#exception handling
except KeyboardInterrupt:
    print ("CTRL + C has been pressed...")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Leaving...")
    sys.exit()

except socket.error:
    print ("Could not connect to the server")
    sys.exit()

#time now
t2 = datetime.now()
#create a variable that stores complete scan time
t = t2 - t1

print ("Scanning completed in: ",t)





