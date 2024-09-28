import socket


def identify_os(ip, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection attempt

        # Attempt to connect to the device
        result = s.connect_ex((ip, port))

        if result == 0:
            # Successful connection, now read the response
            banner = s.recv(1024).decode().lower()

            if "windows" in banner:
                return "Windows"
            elif "android" in banner:
                return "Android"
            else:
                return "Unknown"
        else:
            return "Closed"

    except socket.error:
        return "Error"
    finally:
        s.close()


def scan_local_network(subnet, port):
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        operating_system = identify_os(ip, port)
        if operating_system != "Closed" and operating_system != "Error" and operating_system != "Unknown":
            print(f"IP: {ip}, OS: {operating_system}")


if __name__ == "__main__":
    local_subnet = "192.168.30"
    # You can try different ports like 22 (SSH), 80 (HTTP), etc.
    target_port = 22

    scan_local_network(local_subnet, target_port)
