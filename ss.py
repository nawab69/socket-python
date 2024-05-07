import socket
import threading

HOST = '127.0.0.1'
PORT = 34567

def handleClient(socket):
	while True:
		try:
			message = socket.recv(1024).decode()
			print(message)
		except:
			break
	print("Client Disconnected")
	socket.close()

def server_p():
	s = socket.socket()
	s.bind((HOST,PORT))
	
	s.listen()
	print(f"Listening on {PORT}")

	client_socket, address = s.accept()
	print(f"Client connected {address}")

	thread =threading.Thread(target=handleClient, args=(client_socket,))
	thread.start()

	while True:
		message = input("->")
		client_socket.send(message.encode())


if __name__ == '__main__' :
	server_p()
	
