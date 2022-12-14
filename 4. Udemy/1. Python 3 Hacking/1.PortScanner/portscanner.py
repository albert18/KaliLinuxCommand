import socket
from IPy import IP

ipaddress = input('[+] Enter Target To Scan: ')

def scan_port(ipaddress, port):    
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print('[+] Port' + str(port) + 'is Open')
    except:
        print('[+] Port' + str(port) + 'is Closed')

for port in range(1, 10):
    scan_port(ipaddress, port)

