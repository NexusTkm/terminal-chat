import socket
import threading

def handle_client(client_socket, client_address):
    username = client_socket.recv(1024).decode('utf-8')
    print(f"{username} ({client_address}) has joined the chat.")
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            full_message = f"{username}: {message}"
            print(full_message)
            for client in clients:
                if client != client_socket:
                    client.send(full_message.encode('utf-8'))
        except:
            break
    client_socket.close()
    clients.remove(client_socket)
    print(f"{username} has left the chat.")

def start_server():
    global clients
    clients = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)
    
    print("""
 _   _  ______  __     __  ____   _    _ 
| \ | ||  ____| \ \   / / / __ \ | |  | |
|  \| || |__     \ \_/ / | |  | || |  | |
| . ` ||  __|     \   /  | |  | || |  | |
| |\  || |____     | |   | |__| || |__| |
|_| \_||______|    |_|    \____/  \____/ 
                                        
    """)
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
