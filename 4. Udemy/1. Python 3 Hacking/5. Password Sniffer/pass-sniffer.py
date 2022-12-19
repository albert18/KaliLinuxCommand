from scapy.all import *
from urllib import parse
import re

iface = 'eth0'

def get_login_pass():
    
    user = None
    passwrd = None

def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        get_login_pass(body)
        
    

try:
    sniff(iface=iface, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print('Exiting')
    exit()
    