import socket #Creates network connections

def start_server(): #Defines a function that will run the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a TCP socket using IPv4
    host = 'localhost' #This will set the server address on your own computer
    port = 4444 #Sets the port number the server will listen on

    server.bind((host, port))
    server.listen(1) #Put the server in listening mode for incoming connections. 1 means it allows a client waiting in a queue
    print(f"[+] Server listening on {host}:{port}") #Server is up

    conn, addr = server.accept() #This line pauses the program until a client connects.
    print(f"[+] Connected to client: {addr}") #shows the address of the client that is connected
    
    conn.send(b"Welcome to the server!") #Send a message to the client
    conn.close() #Closes the connection with the client
    server.close()

if __name__ == "__main__": #This prevents the server from starting automatically when someone imports a file into another script

    start_server() #Runs the server
