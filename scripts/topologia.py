#!/usr/bin/python3

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
import sys, time

def myNetwork(option='origin'):

    net = Mininet(controller=RemoteController)

    info( '*** Adding controller\n' )
    c0 = net.addController('c0', ip = '127.0.0.1' , port=6633)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='standalone')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone')
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch, failMode='standalone')

    ASR1 = net.addSwitch('ASR1', cls=OVSKernelSwitch)
    ASR2 = net.addSwitch('ASR2', cls=OVSKernelSwitch)
    ASR3 = net.addSwitch('ASR3', cls=OVSKernelSwitch)
    ASR4 = net.addSwitch('ASR4', cls=OVSKernelSwitch)

    CR10 = net.addSwitch('CR10', cls=OVSKernelSwitch)
    CR20 = net.addSwitch('CR20', cls=OVSKernelSwitch)
    CR30 = net.addSwitch('CR30', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    Pbot1 = net.addHost('Pbot1', cls=Host, ip='10.1.1.11/24', defaultRoute='via 10.1.1.1')
    Pbot2 = net.addHost('Pbot2', cls=Host, ip='10.1.1.13/24', defaultRoute='via 10.1.1.1')
    Pbot3 = net.addHost('Pbot3', cls=Host, ip='10.1.1.14/24', defaultRoute='via 10.1.1.1')
    Pbot4 = net.addHost('Pbot4', cls=Host, ip='10.1.1.16/24', defaultRoute='via 10.1.1.1')

    Pbot5 = net.addHost('Pbot5', cls=Host, ip='10.1.2.11/24', defaultRoute='via 10.1.2.1')
    Pbot6 = net.addHost('Pbot6', cls=Host, ip='10.1.2.13/24', defaultRoute='via 10.1.2.1')
    Pbot7 = net.addHost('Pbot7', cls=Host, ip='10.1.2.14/24', defaultRoute='via 10.1.2.1')
    Pbot8 = net.addHost('Pbot8', cls=Host, ip='10.1.2.15/24', defaultRoute='via 10.1.2.1')
    hacker = net.addHost('hacker', cls=Host, ip='10.1.2.16/24', defaultRoute='via 10.1.2.1')

    Tbot1 = net.addHost('Tbot1', cls=Host, ip='10.1.3.11/24', defaultRoute='via 10.1.3.1')
    user = net.addHost('user', cls=Host, ip='10.1.3.12/24', defaultRoute='via 10.1.3.1')
    Tbot2 = net.addHost('Tbot2', cls=Host, ip='10.1.3.13/24', defaultRoute='via 10.1.3.1')
    Tbot3 = net.addHost('Tbot3', cls=Host, ip='10.1.3.14/24', defaultRoute='via 10.1.3.1')
    Tbot4 = net.addHost('Tbot4', cls=Host, ip='10.1.3.16/24', defaultRoute='via 10.1.3.1')

    Tbot5 = net.addHost('Tbot5', cls=Host, ip='10.1.4.11/24', defaultRoute='via 10.1.4.1')
    Tbot6 = net.addHost('Tbot6', cls=Host, ip='10.1.4.13/24', defaultRoute='via 10.1.4.1')
    Tbot7 = net.addHost('Tbot7', cls=Host, ip='10.1.4.14/24', defaultRoute='via 10.1.4.1')
    Tbot8 = net.addHost('Tbot8', cls=Host, ip='10.1.4.16/24', defaultRoute='via 10.1.4.1')

    DNS0 = net.addHost('DNS0', cls=Host, ip='10.10.15.2/30', defaultRoute='via 10.10.15.1')
    DNS1 = net.addHost('DNS1', cls=Host, ip='10.10.25.2/30', defaultRoute='via 10.10.25.1')
    DNS2 = net.addHost('DNS2', cls=Host, ip='10.10.35.2/30', defaultRoute='via 10.10.35.1')
    DNS3 = net.addHost('DNS3', cls=Host, ip='10.10.45.2/30', defaultRoute='via 10.10.45.1')
    
    UAB = net.addHost('UAB', cls=Host, ip='10.10.10.2/29', defaultRoute='via 10.10.10.1')

    

    info( '*** Add links\n')
    net.addLink(Pbot1, s1, cls=TCLink, bw=100)
    net.addLink(Pbot2, s1, cls=TCLink, bw=100)
    net.addLink(Pbot3, s2, cls=TCLink, bw=100)
    net.addLink(Pbot4, s2, cls=TCLink, bw=100)
    net.addLink(Pbot5, s3, cls=TCLink, bw=100)
    net.addLink(Pbot6, s3, cls=TCLink, bw=100)
    net.addLink(Pbot7, s4, cls=TCLink, bw=100)
    net.addLink(Pbot8, s4, cls=TCLink, bw=100)
    net.addLink(hacker, s4, cls=TCLink, bw=100)
    net.addLink(Tbot1, s5, cls=TCLink, bw=100)
    net.addLink(user, s5, cls=TCLink, bw=100)
    net.addLink(Tbot2, s5, cls=TCLink, bw=100)
    net.addLink(Tbot3, s6, cls=TCLink, bw=100)
    net.addLink(Tbot4, s6, cls=TCLink, bw=100)
    net.addLink(Tbot5, s7, cls=TCLink, bw=100)
    net.addLink(Tbot6, s7, cls=TCLink, bw=100)
    net.addLink(Tbot7, s8, cls=TCLink, bw=100)
    net.addLink(Tbot8, s8, cls=TCLink, bw=100)

    net.addLink(s1, ASR1, cls=TCLink, bw=150)
    net.addLink(s2, ASR1, cls=TCLink, bw=150)
    net.addLink(s3, ASR2, cls=TCLink, bw=150)
    net.addLink(s4, ASR2, cls=TCLink, bw=150)
    net.addLink(s5, ASR3, cls=TCLink, bw=150)
    net.addLink(s6, ASR3, cls=TCLink, bw=150)
    net.addLink(s7, ASR4, cls=TCLink, bw=150)
    net.addLink(s8, ASR4, cls=TCLink, bw=150)

    net.addLink(ASR1, CR20, cls=TCLink, bw=1000)
    net.addLink(ASR2, CR20, cls=TCLink, bw=1000)
    net.addLink(ASR3, CR30, cls=TCLink, bw=1000)
    net.addLink(ASR4, CR30, cls=TCLink, bw=1000)

    net.addLink(CR10, CR30, cls=TCLink, bw=1000)
    net.addLink(CR20, CR10, cls=TCLink, bw=1000)

    if (option == 'attack'):
        net.addLink(UAB, CR10, cls=TCLink, bw=0.01)
    else:
        net.addLink(UAB, CR10, cls=TCLink, bw=1000)
    


    net.addLink(DNS0, ASR1, cls=TCLink, bw=1000)
    net.addLink(DNS1, ASR2, cls=TCLink, bw=1000)
    net.addLink(DNS2, ASR3, cls=TCLink, bw=1000)
    net.addLink(DNS3, ASR4, cls=TCLink, bw=1000)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([])
    net.get('s2').start([])
    net.get('s3').start([])
    net.get('s4').start([])
    net.get('s5').start([])
    net.get('s6').start([])
    net.get('s7').start([])
    net.get('s8').start([])

    net.get('ASR1').start([c0])
    net.get('ASR2').start([c0])
    net.get('ASR3').start([c0])
    net.get('ASR4').start([c0])

    net.get('CR10').start([c0])
    net.get('CR20').start([c0])
    net.get('CR30').start([c0])
    
    input("*** Press Return once net_conf.sh has been executed correctly to launch the requests ...")
    
    info('*** Starting flask at victim\n')
    net.get('UAB').cmdPrint('sudo python3 victima_flask.py &')

    
    info('*** Starting POPDNS Servers\n')
    net.get('DNS0').cmdPrint('sudo python3 DNS0.py 0 &')
    net.get('DNS1').cmdPrint('sudo python3 DNS1.py 1 &')
    net.get('DNS2').cmdPrint('sudo python3 DNS2.py 2 &')
    net.get('DNS3').cmdPrint('sudo python3 DNS3.py 3 &')
    
    info('*** bots running virus\n')
    net.get('Pbot1').cmdPrint('python3 virus.py &')
    net.get('Pbot2').cmdPrint('python3 virus.py &')
    net.get('Pbot3').cmdPrint('python3 virus.py &')
    net.get('Pbot4').cmdPrint('python3 virus.py &')
    net.get('Pbot5').cmdPrint('python3 virus.py &')
    net.get('Pbot6').cmdPrint('python3 virus.py &')    
    net.get('Pbot7').cmdPrint('python3 virus.py &')
    net.get('Pbot8').cmdPrint('python3 virus.py &')    
    net.get('Tbot1').cmdPrint('python3 virus.py &')
    net.get('Tbot2').cmdPrint('python3 virus.py &')    
    net.get('Tbot3').cmdPrint('python3 virus.py &')
    net.get('Tbot4').cmdPrint('python3 virus.py &')
    net.get('Tbot5').cmdPrint('python3 virus.py &')
    net.get('Tbot6').cmdPrint('python3 virus.py &')
    net.get('Tbot7').cmdPrint('python3 virus.py &')
    net.get('Tbot8').cmdPrint('python3 virus.py &')
    
    info('*** Waiting a safe period of time\n')
    time.sleep(8)
    
    #info('*** PingAll\n')
    #net.pingAll()
    
    info('*** Starting hacker\n')
    net.get('hacker').cmdPrint('xterm &')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    if len(sys.argv) == 2:
        option = sys.argv[1]
        print(option)
    else:
        print ('Warning:  Correct options are (normal and attack)\n ')
        print ('Warning:  Set by default normal\n ')
        option = 'normal'
    myNetwork(option)
