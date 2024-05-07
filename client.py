import socket
import threading

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 34567        # The port used by the server

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received from server: {data}")
        except:
            break  # Server closed connection
    print("Server disconnected")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(s,))
    receive_thread.start()

    while True:
        message = input("Enter message to send: ")
        s.sendall(message.encode('utf-8'))
