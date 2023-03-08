import time
from socket import *

server_name = '127.0.0.1'
server_port = 2333
ping_message = "PING"

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)
time_list = []
total_req = 10
lose_req = 0
total_time = 0

for i in range(total_req):
    start_time = time.time()
    try:
        client_socket.sendto(ping_message.encode(), (server_name, server_port))
        response_message, server_address = client_socket.recvfrom(1024)
        RTT = time.time() - start_time
        time_list.append(RTT)
        total_time += RTT
        print('Request sequence %d: RTT = %.5fs' % (i + 1, RTT))
    except Exception as e:
        RTT = time.time() - start_time
        time_list.append(RTT)
        lose_req += 1
        total_time += RTT
        print('Request sequence %d: Request timed out, RTT = %.5fs' % (i + 1, RTT))

print('\n min_RTT: %.5fs\t max_RTT: %.5fs\t avg_RTT: %.5fs' % (
    min(time_list), max(time_list), total_time / len(time_list)))
print('\n packet lost percent: {:.2%}'.format(lose_req / total_req))
