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
    print(f"CONNECTION APPENDED FOR {client_addr}")
    
    try:
        init_msg = "___ WELCOME TO HELL ROOM! TYPE YOUR MESSAGE THEN PRESS ENTER ___\n"
        client_socket.send(init_msg.encode('utf-8'))
        
        # announce new client to all existing clients
        join_msg = f"CLIENT {client_addr} HAS JOINED THE CHAT!\n"
        broadcast(join_msg, client_socket)

        while True:
            BUFFER_SIZE = 1024
            message = client_socket.recv(BUFFER_SIZE)

            if not message:
                print(f"CLIENT {client_addr} IS DISCONNECTED!")
                break

            decode_message = message.decode('utf-8').strip()
            print(f"[MESSAGE] {client_addr}: {decode_message}")

            #check the special command to quit
            if decode_message.lower() == "!quit":
                print(f"CLIENT {client_addr} HAS LEFT THE CHAT!")
                break
            elif decode_message.lower() == "!clients":
                user_list = f"CURRENT CLIENTS: {', '.join(str(addr) for addr in clients_addresses.values())}\n"
                client_socket.send(user_list.encode('utf-8'))
                continue

            broadcast_message = f"{client_addr}: {decode_message}\n"
            broadcast_message(broadcast_message, client_socket)
    except socket.error as e:
        print(f"ERROR HANDLING CLIENT {client_addr}: {e}")
    finally:
        # remove client from the list and close the socket
        print(f"REMOVING CLIENT {client_addr} FROM THE CHAT")
        remove_client(client_socket)
        client_socket.close()
        try:
            client_socket.close()
        except:
            pass

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

        server_socket.listen(10) # upto 10 connections
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
            print(f"\nWAITING FOR CLIENT CLIENTS. {len(clients)} CLIENTS CONNECTED.")

            # accept incoming connection
            client_socket, client_addr = server_socket.accept()

            # add client to the global list
            add_client(client_socket, client_addr)

            # create and start a new thread for the client
            client_thread = threading.Thread(
                target=handle_client, 
                args=(client_socket, client_addr),
                daemon=True
            )
            client_thread.start()

    except KeyboardInterrupt: 
        print("\nSERVER SHUTTING DOWN...")
    except Exception as e:
        print(f"SERVER ERROR: {e}")
    finally:
        with clients_lock:
            for client_socket in clients:
                try:
                    client_socket.close()
                except:
                    pass
        server_socket.close()
        print("[SERVER DISCONNECTED]")

if __name__ == "__main__":
    main()