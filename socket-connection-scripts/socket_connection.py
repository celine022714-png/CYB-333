import socket

def main():
    host = 'localhost'
    port = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    result = s.connect_ex((host, port))
    print("Result is", result)

    if result != 0:
        print(f"[!] Connection failed. Error code: {result}")
        s.close()
        return
    
    print(f"[+] Connected to server at {host}:{port}")

    try:
        while True:
            msg = input("[You(Client)]: ")
            s.send(msg.encode())

            if msg.lower() == "quit":
                print("[+] You ended the chat.")
                break

            data = s.recv(1024).decode()
            print(f"[Server]: {data}")

            if data.lower() == "quit":
                break
    finally:
        s.close()
        print("[+] Client closed.")

if __name__ == "__main__":
    main()
   