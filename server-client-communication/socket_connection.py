import socket #Creates network connection

def main(): #Starts the client program
    host = 'localhost' #The client will connect to a server on the same address and port number which is 4444
    port = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #Creates a TCP client socket
    s.connect((host, port)) #Connects to the server. If the server is not running, this line errors.
    print(f"[+] Connected to server at {host}:{port}") #Shows connection success

    try:
        while True: #Allows continious typing and receiving messages
            msg = input("[You(Client)]: ")  #Client type something and then gets sent to the server
            s.send(msg.encode())

            if msg.lower() == "quit":  #Ift he client type quit, it stops the loop and disconnects
                print("[+] You ended the chat.")
                break

            data = s.recv(1024).decode() #Receieves server reply and prints it
            print(f"[Server]: {data}")

            if data.lower() == "quit": #If server sent "quit" stop chatting
                break
    finally: #This section always closes the connection safely
        s.close()
        print("[+] Client closed.")

if __name__ == "__main__": #Runs the client 
    main()

   
