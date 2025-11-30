import socket #Allows connections between computers

def start_server(): #Defines a function that will run/start the server
    host = 'localhost' #Sets the server to listen in your computer (local machine) and on port 4444
    port = 4444

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port)) #Binds the created socket to the specified address (host and port), allowing it to listen for incoming connections
    server.listen(1) #Server into listening mode.1 specifies that the server can queue one incoming connection request
    print(f"[+] Server listening on {host}:{port}") #Indicates that the server is ready and listening for connections

    conn, addr = server.accept() #waits for a client to connect
    print(f"[+] Connected to client: {addr}") #Prints the IP address of the connected client

    try:
        while True: #Starts an infinite loop to continuously receive messages from the client until broken.
            data = conn.recv(1024).decode()
            if not data: #Checks if there is no data received (which typically indicates that the client has disconnected) and breaks out of the loop if so
                break
            print(f"[Client]: {data}")
            if data.lower() == "quit":
                break
            msg = input("[You(Server)]: ") #Prompts the server user for input to send a message back to the connected client
            conn.send(msg.encode()) 
            
            if msg.lower() == "quit": #Checks if the server's message is "quit". If so, it breaks out of the loop to terminate the connection
                break
    finally:
        conn.close() #Closes the connection socket to the client.
        server.close() #Closes the server socket itself, releasing any resources associated with it
        print("[+] Connection closed.")
if __name__ == "__main__":
    start_server()

           



