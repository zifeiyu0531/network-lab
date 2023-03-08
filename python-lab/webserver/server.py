from socket import *
import sys

server_port = 2333
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print('Server is ready.')

while True:
    connection_socket, addr = server_socket.accept()
    try:
        message = connection_socket.recv(2048).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        output_data = f.read()

        # Send one HTTP header line into socket
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (
            len(output_data))
        connection_socket.send(header.encode())
        # Send the content of the requested file to the client
        for i in range(0, len(output_data)):
            connection_socket.send(output_data[i].encode())
        connection_socket.send('\r\n'.encode())

        connection_socket.close()
    except IOError:
        # Send response message for file not found
        header = 'HTTP/1.1 404 Not Found'
        connection_socket.send(header.encode())
    finally:
        connection_socket.close()
        break

server_socket.close()
sys.exit()
