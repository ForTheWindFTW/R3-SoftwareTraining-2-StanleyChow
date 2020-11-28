# """
# Simple code to send and receive data by TCP
# """
#
# import socket
#
# HEADER_SIZE = 4  # Maximum number of characters in a message is 9999
#
# TCP_IP = '127.0.0.1'
# TCP_PORT = 5005
# BUFFER_SIZE = 4
# MESSAGE = "Hello, World!"
#
# def init(request):
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # s.connect((TCP_IP, TCP_PORT))
# s.connect((socket.gethostname(), TCP_PORT))
# # s.send(MESSAGE.encode('utf-8'))
# full_msg = ''
# while True:
#     data = s.recv(BUFFER_SIZE)
#     # print(data.decode('utf-8'))
#     full_msg += data.decode()
#     if not data:
#         break
# print(full_msg)
# s.close()
#
# # print("received data:", data)
