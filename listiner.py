from scapy.all import *
import storage
import logger


def evalDhcpPkt(packet):
    returnData = []
    ip = None
    vendor = None
    hostname = None

    if packet.haslayer(DHCP):
        dhcp_options = packet[DHCP].options
        if packet.haslayer(Ether):
            target_mac = packet.getlayer(Ether).src

        for item in dhcp_options:
            try:
                label, value = item

            except:
                continue

            if label == "requested_addr":
                ip = value

            elif label == "vendor_class_id":
                vendor = value.decode()

            elif label == "hostname":
                hostname = value.decode()

        returnData = [ip, vendor, hostname,
                      storage.GetManufacture(target_mac),
                      time.time(), target_mac]
        logger.LOGGER_OBJ.debug("dhcp response found %s", str(ip))

    return returnData


def all_time_listiner(packet):
    if ARP in packet and packet[ARP].op == 2:
        logger.LOGGER_OBJ.debug(
            "ICMP response found %s", str(packet[ARP].psrc))
        ip = packet[ARP].psrc
        if packet.haslayer(Ether):
            mac = packet.getlayer(Ether).src
            storage.Global_storage_icmp_update(mac, ip)

    if packet.haslayer(DHCP):
        evaluate_dhcp_packets = evalDhcpPkt(packet)
        storage.Global_storage_dhcp_update(
            evaluate_dhcp_packets[-1], evaluate_dhcp_packets)


def start_all_time_listiner():
    sniff(filter="arp or (udp and (port 67 or port 68))",
          prn=all_time_listiner, iface="Wi-Fi")
