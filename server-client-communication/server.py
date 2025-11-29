import socket

def start_server():
    host = 'localhost'
    port = 4444

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"[+] Server listening on {host}:{port}")

    conn, addr = server.accept()
    print(f"[+] Connected to client: {addr}")

    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"[Client]: {data}")
            if data.lower() == "quit":
                break
            msg = input("[You(Server)]: ")
            conn.send(msg.encode())
            
            if msg.lower() == "quit":
                break
    finally:
        conn.close()
        server.close()
        print("[+] Connection closed.")
if __name__ == "__main__":
    start_server()
           