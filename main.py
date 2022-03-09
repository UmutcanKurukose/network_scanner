import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-ip","--ip_address",dest="ip_address",help="Enter Ip Adress Range!")

    (user_inputs,argument) = parse_object.parse_args()

    if not user_inputs.ip_address:
        print(" Please Enter ip address")

    return user_inputs

def scaner_my_netwrok(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    answered_list.summary()
user_ip_address = get_user_input()
scaner_my_netwrok(user_ip_address.ip_address)