import random
import time
from socket import *

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', 2333))
print('Server is ready to listen.')

while True:
    rand = random.randint(0, 10)
    message, address = server_socket.recvfrom(1024)
    response_message = 'PONG'
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    time.sleep(rand / 100)
    server_socket.sendto(response_message.encode(), address)
