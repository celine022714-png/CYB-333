import socket #Creates network connections

ERROR_CODES = {  #Creates Error code description dictionary
    0: "OPEN",  #0 means the port is open
    10035: "CLOSED"
}
def get_error_description(code):  #Defines a function that takes a number. Looks it up in the ERROR_CODE dictionary. If it does not exist, return "CLOSE" or unknown error
    """Return description for a socket error code."""
    return ERROR_CODES.get(code, "CLOSED - Unknown error")

def scan_port(ip, port):   #Scans a single port
    """
    Scan a single port and return the connect_ex result.
    0= open port
    non-zero = closed/error
    """
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Creates a TCP socket
    s.settimeout(1) # 1 second timeout    #The socket will timed out after 1 second if no connection
    result = s.connect_ex((ip, port))
    description = get_error_description(result)  #Convert results into readable text

    print(f"Port {port}: {result} ({description})")  #Print results

    s.close()  #Close socket
    return result   #Allows other functions to use the result open or closed

def scan_selected_ports(ip, ports):   #Scan selected ports
    """Scan specific list of ports (e.g., 21, 22, 80, 443)."""
    print(f"\nScanning selected ports on {ip}: {ports}\n")  #Shows the list of ports being scanned
    
    open_ports = []   #Create list for open ports
    
    for port in ports: #Loop through each port
        try:
            result = scan_port(ip, port)
            if result == 0: #open port
                open_ports.append(port)
        except Exception as e:  #Catch errors
            print (f"Error scanning port {port}: {e}")
    print("\nOpen selected ports:", open_ports)   #Print open ports

def scan_range(ip, start_port, end_port):
    """Scan a continuous range of ports."""
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    
    open_ports = []
    
    for port in range (start_port, end_port + 1):  #Loops through each port in the range
        try:
            result = scan_port(ip, port)
            if result == 0: #open port
                open_ports.append(port)

        except Exception as e:
            print(f"Error scanning port {port}: {e}")  #Handle errors

    print("\nOpen ports found:", open_ports)


if __name__ == "__main__":  #This makes sure your code runs only when executing the file directly, not when imported
    target_ip = "scanme.nmap.org"  # Example target
    common_ports = [21, 22, 80, 443]  #Common ports
    scan_selected_ports(target_ip, common_ports)  #Run selected scan


