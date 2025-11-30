import socket

ERROR_CODES = {
    0: "OPEN",
    10035: "CLOSED",
}
def get_error_description(code):
    """Return description for a socket error code."""
    return ERROR_CODES.get(code, "CLOSED - Unknown error")
def scan_port(ip, port):
    """
    Scan a single port and return the connect_ex result.
    0= open port
    non-zero = closed/error
    """

    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # 1 second timeout

    result = s.connect_ex((ip, port)) # 0 = success (open port)
    description = get_error_description(result)

    print(f"Port {port}: {result} ({description})")

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