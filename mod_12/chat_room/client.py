import socket
import sys

def connect_to_server(HOST=socket.gethostbyname(socket.gethostname()), PORT=5050):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ADDR = (HOST, PORT)
        client_socket.connect(ADDR)
        print(f"{HOST}: {PORT}")
        
        return client_socket
    
    except socket.error as e:
        print(f"ERROR CONNECTING TO SERVER: {e}")
        return None
    
def main():
    print("____  CHAT_APP_PHASE: CLIENT ____")

    client_socket = connect_to_server()
    if not client_socket:
        sys.exit(1)

    try:
        # receive welcome message
        BUFFER_SIZE = 1024
        welcome_msg = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        print(f"{welcome_msg}")

        # main chat loop
        while True:
            message = input("YOU: ").strip()
            if message.lower() == "!quit":
                print("!DISCONNECTED")
                break
            if message:
                # send message to server
                client_socket.send(message.encode("utf-8"))
                #receive from server
                response = client_socket.recv(BUFFER_SIZE).decode("utf-8")
                print(f"SERVER: {response}")
    except KeyboardInterrupt:
        print("\nCLIENT SHUTTING DOWN...")
    except Exception as e:
        print(f"CLIENT ERROR: {e}")
    finally:
        client_socket.close()
        print("[CLIENT DISCONNECTED FROM SERVER]")

if __name__ == "__main__":
    main()