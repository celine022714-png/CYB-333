import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 4444

    server.bind((host, port))
    server.listen(1)
    print(f"[+] Server listening on {host}:{port}")

    conn, addr = server.accept()
    print(f"[+] Connected to client: {addr}")
    
    conn.send(b"Welcome to the server!")
    conn.close()
    server.close()

if __name__ == "__main__":
    start_server()