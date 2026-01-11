from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import AsyncMacLookup
import asyncio

# Initialize the lookup
vendor_lookup = AsyncMacLookup()

async def scan_network(ip_range):
    print(f"[*] Starting ARP scan on {ip_range}...")
    
    arp_request = ARP(pdst=ip_range)
    broadcast_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast_frame / arp_request
    
    # Scapy's srp is a blocking call, which is fine here
    answered_list = srp(packet, timeout=2, verbose=False)[0]

    discovered_devices = []

    for sent, received in answered_list:
        mac_addr = received.hwsrc
        
        try:
            # THIS IS THE CRITICAL LINE
            vendor = await vendor_lookup.lookup(mac_addr)
        except Exception:
            vendor = "Unknown"

        device_info = {
            "ip": received.psrc,
            "mac": mac_addr,
            "vendor": vendor
        }
        discovered_devices.append(device_info)

    print(f"[*] Found {len(discovered_devices)} devices.")
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