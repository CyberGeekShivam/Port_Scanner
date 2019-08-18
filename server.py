from socket import *

host = '0.0.0.0'
port = 5

s=socket(AF_INET,SOCK_STREAM)

s.bind((host,port))

s.listen(5)

while(True):
 c,addr=s.accept()
 print("[+] Got connection from",str(addr))
 msg="this is the server"
 c.send(msg.encode('ascii'))
 c.close()