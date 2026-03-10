import socket
import sys

# Dictionary of commmon ports and their associated services
# These are well-known ports defines by IANA (ports 0-1023 are reserved/priveledged)
# Note: This is not an exhaustive list, this is just a sample of common ports
PORT_NAMES = {
    21 : "FTP",
    22 : "SSH",
    23 : "Telnet",
    25 : "SMTP",
    53 : "DNS",
    80 : "HTTP",
    110 : "POP3",
    143 : "IMAP",
    443 : "HTTPS",
    445 : "SMB",
    3389 : "RDP"
}

# Allow optional target via CDL argument, default to localhost
# Usage: python port_scanner.py [host]
target = sys.argv[1] if len(sys.argv) > 1 else "localhost"
print(f"Scanning target: {target}")
print("-" * 30)

open_count = 0

for port in PORT_NAMES:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4, SOCK_STREAM = TCP
    s.settimeout(1)

    status = s.connect_ex((target, port))

    if status == 0:
        print(f"Port {port} ({PORT_NAMES[port]}) is open.")
        open_count += 1
    else:
        print(f"Port {port} ({PORT_NAMES[port]}) is closed.")
    s.close()

print("-" * 30)
print(f"Scan complete: {open_count}/{len(PORT_NAMES)} ports on {target} are open.")