import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print("\n" + message + "\n> ", end="")
            else:
                break
        except:
            break
    client_socket.close()

def start_client():
    username = input("Enter your username: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))
    client_socket.send(username.encode('utf-8'))

    print("""
 _   _  ____   _    _  _    _  _   _ 
| \ | ||  _ \ | |  | || |  | || \ | |
|  \| || |_) || |  | || |  | ||  \| |
| . ` ||  _ < | |  | || |  | || . ` |
| |\  || |_) || |__| || |__| || |\  |
|_| \_||____/  \____/  \____/  |_| \_|
                                      
    """)
    print("> ", end="")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))
        print("> ", end="")

    client_socket.close()

if __name__ == "__main__":
    start_client()
