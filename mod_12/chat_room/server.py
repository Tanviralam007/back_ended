import socket
import threading
import sys

# global set to handle clients
clients = []
clients_addresses = {} # dic mapping sockets :-> addresses
clients_lock = threading.Lock()

def add_client(client_socket, client_addr):
    with clients_lock:
        clients.append(client_socket)
        clients_addresses[client_socket] = client_addr
        print(f"CLIENT {clients_addresses[client_socket]} ADDED. TOTAL CLIENTS: {len(clients)}")

def remove_client(client_socket):
    with clients_lock:
        if client_socket in clients:
            clients.remove(client_socket)
            address = clients_addresses.pop(client_socket, "[UNKNOWN]")
            print(f"CLIENT {address} REMOVED. TOTAL CLIENTS: {len(clients)}")

def broadcast(message, sender_socket=None):
    with clients_lock:
        clients_copy = clients.copy()

        for client_socket in clients_copy:
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode('utf-8'))
                except socket.error as e:
                    print(f"ERROR SENDING MESSAGE TO {clients_addresses.get(client_socket, '[UNKNOWN]')}: {e}")
                    remove_client(client_socket)
                    try:
                        client_socket.close()
                    except socket.error as e:
                        pass

def handle_client(client_socket, client_addr):
    print(f"CONNECTION APPENDED FOR {client_socket}")
    
    try:
        init_msg = "WELCOME TO HELL ROOM! TYPE YOUR MESSAGE AND PRESS ENTER\n"
        client_socket.send(init_msg.encode('utf-8'))
        
        while True:
            BUFFER_SIZE = 1024
            message = client_socket.recv(BUFFER_SIZE)

            if not message:
                print(f"CLIENT {client_addr} IS DISCONNECTED!")
                break

            decode_message = message.decode('utf-8').strip()
            print(f"[MESSAGE] {client_addr}: {decode_message}")

            #echo the message back to the client
            echo_message = f"{decode_message}\n"
            client_socket.send(echo_message.encode('utf-8'))
    except socket.error as e:
        print(f"ERROR HANDLING CLINET {client_addr}: {e}")
    finally:
        client_socket.close()
        print(f"[CONNECTION CLOSED FOR {client_addr}]")

def create_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return server_socket
    except socket.error as e:
        print(f"ERROR CREATING SOCKET: {e}")
        return None
    
def bind_and_listen(server_socket, HOST=socket.gethostbyname(socket.gethostname()), PORT=5050):
    try:
        ADDR = (HOST, PORT)
        server_socket.bind(ADDR)
        print(f"{HOST}: {PORT}")

        server_socket.listen(5)
        print("[LISTENING] SERVER IS LISTENING FOR CONNECTIONS...")
        return True
    except socket.error as e:
        print(f"ERROR BINDING/LISTENING: {e}")
        return False
    
def main():
    print("____  CHAT_APP_PHASE: SERVER ____")

    # create server socket
    server_socket = create_server()
    if not server_socket:
        sys.exit(1)

    # bind and listen
    if not bind_and_listen(server_socket):
        server_socket.close()
        sys.exit(1)

    # main server loop to handle one client at a time
    try:
        while True:
            print("[WAITING] NEW CLIENT TO BE CONNECTED...")

            # accept incoming connection
            client_socket, client_addr = server_socket.accept()

            # handle the client
            handle_client(client_socket, client_addr)

    except KeyboardInterrupt: 
        print("\nSERVER SHUTTING DOWN...")
    except Exception as e:
        print(f"SERVER ERROR: {e}")
    finally:
        server_socket.close()
        print("SERVER SOCKET CLOSE")

if __name__ == "__main__":
    main()