#!/usr/bin/python

from mininet.topo import Topo

class Topology(Topo):
    def __init__(self):
        Topo.__init__(self)

        H1 =self.addHost('H1', ip='10.0.0.1/24', mac = '10:00:00:00:00:01')
        H2 =self.addHost('H2', ip='10.0.0.2/24', mac = '10:00:00:00:00:02')
        H3 =self.addHost('H3', ip='10.0.0.3/24', mac = '10:00:00:00:00:03')
        H4 =self.addHost('H4', ip='10.0.0.4/24', mac = '10:00:00:00:00:04')
            
        S1 = self.addSwitch('S1')
        S2 = self.addSwitch('S2')
        S3 = self.addSwitch('S3')
        S4 = self.addSwitch('S4')

        self.addLink(H1,S1,1,1)
        self.addLink(H2,S2,1,1)
        self.addLink(H3,S3,1,1)
        self.addLink(H4,S4,1,1)
        
        self.addLink(S1,S2,2,3)
        self.addLink(S2,S3,2,3)
        self.addLink(S3,S4,2,3)
        self.addLink(S4,S1,2,3)
topos = {'mytopo':(lambda:Topology())}
