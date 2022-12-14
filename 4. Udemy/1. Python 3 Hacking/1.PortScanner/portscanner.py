import socket
from IPy import IP

class PortScan():
    
    def __init__(self, target, port_number):
        self.target = target
        self.port_number = port_number
    
    def scan(self):
        for port in range(1, 100):
            self.scan_port(port)

    def check_ip(self):
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self, port):    
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
            except:
                print('[+] Open Port ' + str(port))
        except:
            pass




