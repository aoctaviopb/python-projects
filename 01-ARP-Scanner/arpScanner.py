'''
This python script will make an ARP request to all the host in the given network to identify the active hosts.
'''

import sys
import scapy.all as scapy


def arpscan(net_ip):
    scapy.arping(net_ip)

def main():
    if len(sys.argv) == 2:
        arpscan(sys.argv[1])
    else:
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        print("Usage in Windows: python arpScan.py network_address")
        print("Usage in Windows: python arpScan.py 192.168.1.0/24 \n")
        print("Usage in Linux: sudo python3 arpScan.py network_address")
        print("Usage in Linux: sudo python3 arpScan.py 192.168.1.0/24")
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")


if __name__ == "__main__":
    main()
