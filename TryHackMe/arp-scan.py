# coding=utf-8

from scapy.all import * # importing everything from scapy.all

interface = "eth0"
ip_range = "10.10.X.X/24" #change this
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range)

ans, unans = srp(paclet, timeout = 2, iface=interface, inter=0.1)

for send, recive in ans:
    print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))

