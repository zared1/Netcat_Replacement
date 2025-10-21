import sys
import socket
import time

host = sys.argv[1]
port = int(sys.argv[2])

def nc(host_ip, pnum):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_ip, pnum))
    while True:
        msg = input()
        if msg == "":
            break
        s.sendall(msg.encode())
    time.sleep(3)

    while True:
        receiver = s.recv(1024)
        if not receiver:
            break
        print(receiver.decode())

    s.close()

nc(host, port)
