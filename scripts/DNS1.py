#!/usr/bin/env python

# Importar las bibliotecas de Scapy
from scapy.all import *

# Establecer la interfaz para escuchar y responder
net_interface = "DNS1-eth0"

# Filtro de paquetes de Berkeley Packet Filter para capturar únicamente paquetes DNS específicos
packet_filter = " y ".join([
    "udp puerto destino 53",         # Filtrar el puerto UDP 53
    "udp[10] & 0x80 = 0",            # Solo consultas DNS
    ])

# Función que responde a las consultas DNS
def dns_reply(packet):

    # Construir el paquete DNS
    # Construir la cabecera Ethernet mirando el paquete capturado
    eth = Ether(
        src=packet[Ether].dst,
        dst=packet[Ether].src
        )

    # Construir la cabecera IP mirando el paquete capturado
    ip = IP(
        src=packet[IP].dst,
        dst=packet[IP].src
        )

    # Construir la cabecera UDP mirando el paquete capturado
    udp = UDP(
        puerto_destino=packet[UDP].puerto_origen,
        puerto_origen=packet[UDP].puerto_destino
        )

    # Construir la respuesta DNS mirando el paquete capturado y dependiendo manualmente del campo qtype. 0 -> CUALQUIERA. 1 -> A
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

    # Ensamblar el paquete completo
    response_packet = eth / ip / udp / dns

    # Enviar la respuesta DNS
    sendp(response_packet, iface=net_interface)

# Capturar una consulta DNS que coincida con el 'packet_filter' y enviar una respuesta especialmente diseñada
while True:
    sniff(filter=packet_filter, prn=dns_reply, store=1, iface=net_interface, count=1)
