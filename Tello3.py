#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018
import math
import threading 
import socket
import sys
import time

host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print('\r\n\r\nTello Python3 Demo.\r\n')

print('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print('end -- quit demo.\r\n')


# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

R = 30  # 半径 单位cm
theta = 45
dis = int(math.tan(theta) * R)

command1 = ["command", "takeoff", "forward 30"]
command2 = ["cw 45", "left 30"]
# 手动输入模式:
while True:
    try:
        msg = input("")
        if not msg:
            break

        if 'end' in msg:
            print('...')
            sock.close()
            break

        # Send data
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)

    except KeyboardInterrupt:
        print('\n . . .\n')
        sock.close()
        break

for j in range(360 // theta):
    for i in command2:
        try:
            msg = input("")
            if msg == "":
                msg = i
                print(msg)
            if not msg:
                break

            if 'end' in msg:
                print('...')
                sock.close()
                break

            # Send data
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
        except KeyboardInterrupt:
            print('\n . . .\n')
            sock.close()
            break