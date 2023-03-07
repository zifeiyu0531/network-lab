from socket import *

server_name = '127.0.0.1'
server_port = 2333
sentence = input('Input lowercase sentence:')

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
client_socket.send(sentence.encode())
modified_sentence = client_socket.recv(1024)

print('From server: ', modified_sentence.decode())
client_socket.close()
