from socket import *

server_port = 2333

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print('Server is ready to receive.')

while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper()
    server_socket.sendto(modified_message.encode(), client_address)
