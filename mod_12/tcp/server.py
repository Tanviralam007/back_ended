import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECTED = "!DISCONNECTED"

# creating a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding the socket
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} is connected!")
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len.strip())
            msg = conn.recv(msg_len).decode(FORMAT)
            print(f"[{addr}] {msg}")
            if msg == DISCONNECTED:
                connected = False
    
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is running...")

if __name__ == "__main__":
    start()