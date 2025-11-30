import socket #Creates network connections

def main(): #Defines the function that will run in your client
    host = 'localhost' #Server address you want to connect to
    port = 4444 #The port number the client should connect to. It should match the server's port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a TCP client socket
    
    result = s.connect_ex((host, port)) #Attemps to connect to the server. Connect_ex() returns an error code instead of crashing
    print("Result is", result) #Display the result/error code of the connection attempt

    if result != 0: #Checks if the connection did not succeed
        print(f"[!] Connection failed. Error code: {result}") #If failed, print the specific error number.
        s.close() #closes the socket when connection failed
        return #stops the program because it cannot connect
    
    print(f"[+] Connected to server at {host}:{port}")  #If the connection succeed, print connected to server.

    try: #Starts a try block for options
        while True:
            msg = input("[You(Client)]: ") #Ask the user to type a message in the terminal
            s.send(msg.encode())  #Sends the message to the server

            if msg.lower() == "quit":   #If the user types quit, stop the loop
                print("[+] You ended the chat.") #Tells the user they closed the chat
                break #break out the chat loop

            data = s.recv(1024).decode() #Waits to receieve data from the server up to 1024bytes
            print(f"[Server]: {data}") #Prints the server message

            if data.lower() == "quit":  #If the server sends "quit", the client will exit chat
                break
    finally:
        s.close() #Closes the socket connection safely
        print("[+] Client closed.") #Prints a message that the client has shut down

if __name__ == "__main__":
    main() #Run the client program

   
