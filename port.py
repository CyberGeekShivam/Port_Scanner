from socket import *
from sys import *

host = argv[1]

s=socket(AF_INET,SOCK_STREAM)
for port in range(1,30):
 if(s.connect_ex((host,port))==0):
  print("port %d is open" % port)
  s.close()
  s=socket(AF_INET,SOCK_STREAM)
 else:
  print("port %d is closed" % port)
  s=socket(AF_INET,SOCK_STREAM)
