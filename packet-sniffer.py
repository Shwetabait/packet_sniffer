from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):

    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        
        protocol = "other"
        
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        
        print(f"Source: {src} -> Destination{dst} | Protocol {protocol}")

sniff(prn=packet_callback)