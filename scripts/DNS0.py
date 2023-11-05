#!/usr/bin/env python

# Import scapy libraries
from scapy.all import *

# Set the interface to listen and respond on
net_interface = "DNS0-eth0"

# Berkeley Packet Filter for sniffing specific DNS packet only
packet_filter = " and ".join([
    "udp dst port 53",          # Filter UDP port 53
    "udp[10] & 0x80 = 0",       # DNS queries only
    ])

# Function that replies to DNS query
def dns_reply(packet):

    # Construct the DNS packet
    # Construct the Ethernet header by looking at the sniffed packet
    eth = Ether(
        src=packet[Ether].dst,
        dst=packet[Ether].src
        )

    # Construct the IP header by looking at the sniffed packet
    ip = IP(
        src=packet[IP].dst,
        dst=packet[IP].src
        )

    # Construct the UDP header by looking at the sniffed packet
    udp = UDP(
        dport=packet[UDP].sport,
        sport=packet[UDP].dport
        )

    # Construct the DNS response by looking at the sniffed packet and manually depending on qtype field. 0 -> ANY. 1 -> A
    qtype = packet[DNS].qd.qtype
    if qtype == 0:
        dns = DNS(
        id=packet[DNS].id,
        qd=packet[DNS].qd,
        aa=1,
        rd=0,
        qr=1,
        ra=1,
        qdcount=1,
        ancount=18,
        nscount=0,
        arcount=0)
        an1 = DNSRR(rrname=packet[DNS].qd.qname, type='A', rclass='IN', ttl=600, rdata='1.2.3.4')
        an2 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an3 = DNSRR(rrname=packet[DNS].qd.qname, type='CNAME', rclass='IN', ttl=600, rdata='example.com')
        an4 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an5 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an6 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an7 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an8 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an9 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an10 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an11 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an12 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an13 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an14 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an15 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an16 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an17 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        an18 = DNSRR(rrname=packet[DNS].qd.qname, type='AAAA', rclass='IN', ttl=600, rdata='2001:db8::1')
        dns.an = an1/an2/an3/an4/an5/an6/an7/an8/an9/an10/an11/an12/an13/an14/an15/an16/an17/an18
    else:
        dns = DNS(
        id=packet[DNS].id,
        qd=packet[DNS].qd,
        aa=1,
        rd=0,
        qr=1,
        ra=1,
        qdcount=1,
        ancount=1,
        nscount=0,
        arcount=0,
        an=[DNSRR(rrname=packet[DNS].qd.qname, type='A', rclass='IN', ttl=600, rdata='1.2.3.4')]
        )

    # Put the full packet together
    response_packet = eth / ip / udp / dns

    # Send the DNS response
    sendp(response_packet, iface=net_interface)

# Sniff for a DNS query matching the 'packet_filter' and send a specially crafted reply
while True:
    sniff(filter=packet_filter, prn=dns_reply, store=1, iface=net_interface, count=1)


