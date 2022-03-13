import sys
import socket

password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
pin = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 30002))
    
# Print welcome message
welcome_msg = s.recv(2048)
print(welcome_msg)

try:
	while pin < 10000:
		inp = "{0} {1}\n".format(password, str(pin).zfill(4))
		s.sendall(inp.encode())
		msg = s.recv(1024)
		if 'Wrong' not in msg:
			print(msg)
			break
		pin += 1
except:
	print("Errored out")
