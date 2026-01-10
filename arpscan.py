from scapy.all import ARP, Ether, srp
import sys

def scan_network(ip_range):
    """
    Sends ARP requests to a range of IP addresses and returns 
    a list of discovered IP and MAC addresses.
    """
    print(f"[*] Starting ARP scan on {ip_range}...")

    # 1. Create an ARP request packet
    # pdst is the destination IP range
    arp_request = ARP(pdst=ip_range)

    # 2. Create an Ethernet frame to wrap the ARP request
    # dst="ff:ff:ff:ff:ff:ff" ensures this is a broadcast packet
    broadcast_frame = Ether(dst="ff:ff:ff:ff:ff:ff")

    # 3. Combine them into a single packet (Stacking layers)
    packet = broadcast_frame / arp_request

    # 4. Send the packet and catch the responses
    # timeout: how long to wait for a response
    # verbose: set to False to keep the output clean
    answered_list = srp(packet, timeout=2, verbose=False)[0]

    # 5. Parse the results
    discovered_devices = []
    for sent, received in answered_list:
        device_info = {
            "ip": received.psrc,
            "mac": received.hwsrc
        }
        discovered_devices.append(device_info)

    return discovered_devices

if __name__ == "__main__":
    # Example usage: python scanner.py 192.168.1.0/24
    if len(sys.argv) < 2:
        print("Usage: sudo python3 scanner.py <ip_range>")
        sys.exit(1)

    target_range = sys.argv[1]
    results = scan_network(target_range)

    print("\n[+] Discovered Devices:")
    print("IP Address\t\tMAC Address")
    print("-" * 40)
    for device in results:
        print(f"{device['ip']}\t\t{device['mac']}")