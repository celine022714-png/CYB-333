import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 4444

    s.connect((host, port))
    print(f"Connected to {host} pn port {port}")

    message = s.recv(1024)
    print("Message from server:", message.decode())

    s.close()

if __name__ == "__main__":
    main()