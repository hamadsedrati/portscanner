import sys
import socket
import threading
from datetime import datetime

# Function to scan a port


def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection attempt
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except socket.error as e:
        print(f"Error scanning port {port}: {e}")

    except Exception as e:
        print(f"An unexpected error occurred while scanning port {port}: {e}")


# Main function

def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("Usage: python portscanner.py <target>")
        sys.exit(1)

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Could not resolve hostname: {target}")
        sys.exit(1)

    print('-' * 50)
    print(f"Scanning target: {target_ip}")
    print(f"Time started: {datetime.now()}")
    print('-' * 50)

    try:
        threads = []
        for port in range(1, 65536):
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nPort scanning interrupted by user.")
        sys.exit(0)

    except Exception as e:
        print(f"An error occurred during port scanning: {e}")
        sys.exit(1)

    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit(1)

    print("\nPort scanning completed!")


if __name__ == "__main__":
    main()
