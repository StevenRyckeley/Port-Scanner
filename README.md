# Port Scanner

A lightweight Python TCP port scanner for identifying open services on a target host. Built as part of a cybersecurity portfolio to demonstrate network fundamentals, socket programming, and reconnaissance concepts.

---

## Features

- Scans 11 common well-known ports (IANA-defined range 0–1023)
- Identifies associated service names (SSH, HTTP, RDP, etc.)
- Accepts an optional target host via command-line argument
- Displays a clean open/closed summary with a final count
- No external dependencies — standard library only

---

## Ports Scanned

| Port | Service | Notes |
|------|---------|-------|
| 21   | FTP     | Unencrypted file transfer |
| 22   | SSH     | Encrypted remote login |
| 23   | Telnet  | Legacy unencrypted remote login |
| 25   | SMTP    | Outgoing email |
| 53   | DNS     | Hostname resolution |
| 80   | HTTP    | Unencrypted web traffic |
| 110  | POP3    | Incoming email retrieval |
| 143  | IMAP    | Email management |
| 443  | HTTPS   | Encrypted web traffic (TLS) |
| 445  | SMB     | Windows file/printer sharing |
| 3389 | RDP     | Windows remote desktop |

---

## Usage

```bash
# Scan localhost (default)
python port_scanner.py

# Scan a specific host
python port_scanner.py 192.168.1.1
python port_scanner.py example.com
```

### Example Output

```
Scanning target: localhost
----------------------------------------
  [OPEN]   Port 22    (SSH)
  [CLOSED] Port 80    (HTTP)
  [OPEN]   Port 443   (HTTPS)
  ...
----------------------------------------
Scan complete: 2/11 ports open on localhost
```

---

## How It Works

The scanner uses Python's built-in `socket` module to attempt a **TCP connection** (`SOCK_STREAM`) on each port via `connect_ex()`. Unlike `connect()`, `connect_ex()` returns an error code instead of raising an exception — `0` means the port accepted the connection (open), any non-zero value means it was refused or timed out (closed/filtered).

A 1-second timeout prevents the scanner from stalling on firewalled ports that silently drop packets.

---

## Concepts Demonstrated

- **TCP/IP fundamentals** — understanding connection-oriented vs. connectionless protocols
- **Socket programming** — using `AF_INET` / `SOCK_STREAM` for IPv4 TCP sockets
- **Network reconnaissance** — port scanning as the first phase of enumeration
- **Resource management** — explicitly closing sockets to release OS file descriptors
- **IANA well-known ports** — awareness of standardized service-to-port mappings

---

## Disclaimer

This tool is intended for **educational use and authorized testing only**. Always obtain explicit permission before scanning any host you do not own. Unauthorized port scanning may violate local laws and network policies.

---

## Future Improvements

- [ ] Multi-threading for faster scans across large port ranges
- [ ] Full port range scanning (1–65535) with `-p` flag
- [ ] UDP port scanning support
- [ ] Export results to CSV or JSON
- [ ] Banner grabbing to fingerprint service versions
- [ ] Integration with MITRE ATT&CK — map open ports to relevant techniques (e.g., T1046 Network Service Discovery)
