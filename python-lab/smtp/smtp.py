from socket import *
import base64

HOST = 'smtp.163.com'
PORT = 25
BUFSIZE = 1024
ADDR = (HOST, PORT)
user = base64.b64encode(b'zifeiyu990531@163.com').decode() + '\r\n'
password = base64.b64encode(b'XSMLGQKVZFJBBFHW').decode() + '\r\n'

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
recv = tcpCliSock.recv(BUFSIZE)
print(recv)
if recv[:3] != b'220':
    print('220 reply not received from server.')

heloCommand = 'HELO Alice\r\n'
tcpCliSock.send(heloCommand.encode())
recv = tcpCliSock.recv(BUFSIZE)
print('hello: ', recv)
if recv[:3] != b'250':
    print('250 reply not received from server.')

login = 'AUTH LOGIN\r\n'
tcpCliSock.send(login.encode())
recv = tcpCliSock.recv(BUFSIZE)
print('login:', recv)
tcpCliSock.send(user.encode())
recv = tcpCliSock.recv(BUFSIZE)
print('user:', recv)
tcpCliSock.send(password.encode())
recv = tcpCliSock.recv(BUFSIZE)
print('password: ', recv)

mailFrom = 'MAIL FROM: <zifeiyu990531@163.com>\r\n'
tcpCliSock.send(mailFrom.encode())
recv = tcpCliSock.recv(BUFSIZE)
print('mail from: ', recv)

reptTo = 'RCPT TO: <1186352914@qq.com>\r\n'
tcpCliSock.send(reptTo.encode())
recv = tcpCliSock.recv(BUFSIZE)
print('rcpt to: ', recv)

data = b'DATA\r\n'
tcpCliSock.send(data)
recv = tcpCliSock.recv(BUFSIZE)
print('data: ', recv)

who = 'zifeiyu990531@163.com'
from_ = who
to = ['1186352914@qq.com']
headers = [
    'From: %s' % from_,
    'To: %s' % ','.join(to),
    'Subject: send SMTP',
]

body = [
    'Hello',
    'World!',
]
msg = '\r\n\r\n'.join(('\r\n'.join(headers), '\r\n'.join(body)))
tcpCliSock.send(msg.encode())
endmsg = b'\r\n.\r\n'
tcpCliSock.send(endmsg)
recv = tcpCliSock.recv(BUFSIZE)
print('msg: ', recv)

quit = 'QUIT\r\n'
tcpCliSock.send(quit.encode())
recv = tcpCliSock.recv(BUFSIZE)
print('quit: ', recv)

tcpCliSock.close()
