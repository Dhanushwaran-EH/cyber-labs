# simple-port-scanner.py
import socket

target = input("Enter target IP (e.g., 127.0.0.1): ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # quick scan
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    sock.close()
