import socket
def scan_port(ip, port):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # 1 second timeout

    result = s.connect_ex((ip, port)) # 0 = success (open port)
    print(f"Port {port}: {result}")

    s.close()
    return result

def scan_range(ip,start_port, end_port):
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            result = scan_port(ip, port)
            if result == 0: #open port
                open_ports.append(port)

        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    print("\nOpen ports found:", open_ports)

if __name__ == "__main__":
    target_ip = "192.168.1.101"
    start = 20
    end = 80
    scan_range(target_ip, start, end)