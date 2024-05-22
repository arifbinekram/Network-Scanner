#!/usr/bin/python3

import scapy.all as scapy
import argparse

def get_ip():
    parser = argparse.ArgumentParser()	
    parser.add_argument("-t", "--target", dest="ipaddr", help="Specify an IP Address or a range of IP Address")
    options = parser.parse_args()

    if not options.ipaddr:
        parser.error("[-] Specify an IP Address or a range of IP Address --help for more details")

    return options

def scan(ip):
    arp_header = scapy.ARP(pdst=ip)
    ether_header = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_packet = ether_header/arp_header
    answered_list = scapy.srp(arp_request_packet, timeout=1, verbose=False)[0]
    
    clients_list = []
    
    for elements in answered_list:
        client_dict = {"ip": elements[1].psrc, "mac": elements[1].hwsrc}
        clients_list.append(client_dict)
    
    return clients_list

def print_result(result_list):
    print("IpAdrr\t\t\tMacAddr")
    print("------------------------------------------")
    for client in result_list:
        print(client['ip'], "\t\t", client['mac'])

ip = get_ip()
scan_result = scan(ip.ipaddr)
print_result(scan_result)
