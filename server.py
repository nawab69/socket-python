import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from client: {message}")
        except:
            break  # Client disconnected
    client_socket.close()
    print("Client disconnected")

def server_p() :
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    client_socket, address = s.accept()
    print(f"Connected by {address}")

    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

    while True:
        reply = input(" -> ")
        client_socket.sendall(reply.encode('utf-8'))

if __name__ == '__main__' : 
    server_p()
