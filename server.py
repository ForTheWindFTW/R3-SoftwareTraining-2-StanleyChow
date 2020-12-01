"""
Simple code to serve TCP
"""

import socket
import datetime
import threading

HEADER_SIZE = 4  # Maximum number of characters in a message is 9999
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
command_history = ['\tMove history:']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(2)
print('SERVER: Bound and listening to {ip}:{port}'.format(ip=TCP_IP, port=TCP_PORT))


def message_received(msg_len, msg, header_size=HEADER_SIZE):
    return len(msg) - header_size == msg_len


while True:
    clientsocket, address = s.accept()
    print('SERVER: Established connection with {}'.format(address))

    full_msg = ''
    msg_len = -1
    new_msg = True

    while True:
        msg = clientsocket.recv(HEADER_SIZE)

        if new_msg:  # Get the header (length of message)
            msg_len = int(msg)
            new_msg = False

        full_msg += msg.decode('utf-8')  # Append current data of HEADER_SIZE bytes/characters

        if message_received(msg_len, full_msg):  # Detect end of current message
            command_history.append('Received {:%y/%m/%d %I:%M:%S %p}: {}'.format(datetime.datetime.now(), full_msg[HEADER_SIZE:]))
            print('\t{}'.format(command_history[-1]))

            if full_msg[HEADER_SIZE:] == 'DONE':  # Detect end of all messages
                print('SERVER: Full message with {} receievd'.format(address))
                # print(*command_history, sep='\n\t')  # Echos the command_history list which contains all of the moves
                break

            # Prepare for new message
            full_msg = ''
            new_msg = True

    # Comment out break statement below to keep server listening
    if full_msg[HEADER_SIZE:] == 'DONE':
        break
s.close()
