"""
Simple code to serve TCP
"""

import socket
import time
import datetime

time.sleep(10)

HEADER_SIZE = 4  # Maximum number of characters in a message is 9999
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
command_history = ['\tMove history:']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(2)
print('SERVER: Bound and listening to {ip}:{port}'.format(ip=TCP_IP, port=TCP_PORT))

while True:
    clientsocket, address = s.accept()
    print('SERVER: Established connection with {}'.format(address))

    full_msg = ''
    msg_len = -1
    new_msg = True

    while True:
        msg = clientsocket.recv(HEADER_SIZE)

        if new_msg:
            msg_len = int(msg)
            new_msg = False

        full_msg += msg.decode('utf-8')

        if len(full_msg) - HEADER_SIZE == msg_len:
            if full_msg[HEADER_SIZE:] == '[0][255][0][255]':
                move = 'forward'
            elif full_msg[HEADER_SIZE:] == '[0][255][255][0]':
                move = 'right'
            elif full_msg[HEADER_SIZE:] == '[255][0][0][255]':
                move = 'left'
            elif full_msg[HEADER_SIZE:] == '[0][0][0][0]':
                move = 'stop'
            else:
                move = 'UNKNOWN'
            print('\tRECIEVED {}: "{}" ({})'.format(address, full_msg, move))
            command_history.append('Received {:%y/%m/%d %I:%M:%S %p}: {}'.format(datetime.datetime.now(), full_msg[HEADER_SIZE:]))

            if full_msg[HEADER_SIZE:] == 'DONE':
                clientsocket.close()
                print('SERVER: Closed connection with {}'.format(address))
                print(*command_history, sep='\n\t')
                break

            full_msg = ''
            new_msg = True
