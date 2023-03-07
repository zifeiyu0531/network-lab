from socket import *

server_name = '127.0.0.1'
server_port = 2333
message = input('Input lowercase sentence:')

client_socket = socket(AF_INET, SOCK_DGRAM)  # AF_INET表示IPv4、SOCK_DGRAM表示UDP
client_socket.sendto(message.encode(), (server_name, server_port))
modified_message, server_address = client_socket.recvfrom(2048)
client_socket.close()

print(modified_message.decode())
