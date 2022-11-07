import os

ip = os.popen('hostname -I').readline()
print(ip)
print(type(ip))