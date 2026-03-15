## Packet Sniffer (Python)

## Project Overview
This project is a basic network packet sniffer built with Python and Scapy.  
The tool captures network packets and displays important information, such as the source and destination IP addresses and the protocol type.

Packet sniffers are widely used in **network monitoring, troubleshooting, and cybersecurity analysis**.

---

## Features
- Captures live network packets
- Displays **Source IP Address**
- Displays **Destination IP Address**
- Identifies **Protocol Type (TCP / UDP / Other)**
- Beginner-friendly implementation using Python

---

## Technologies Used
- Python
- Scapy Library

---

## How It Works
1. The script listens to live network traffic.
2. When a packet is captured, the callback function processes it.
3. The script extracts:
   - Source IP
   - Destination IP
   - Protocol type
4. The information is printed in the terminal.

---
