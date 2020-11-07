#!/usr/bin/python

from mininet.topo import Topo

class Topology(Topo):
    def __init__(self):
        Topo.__init__(self)

        H1 =self.addHost('H1', ip='10.0.0.1/24', mac = '10:00:00:00:00:01')
        H2 =self.addHost('H2', ip='10.0.0.2/24', mac = '10:00:00:00:00:02')

        S1 = self.addSwitch('S1')
        S2 = self.addSwitch('S2')
        S3 = self.addSwitch('S3')
        S4 = self.addSwitch('S4')
        S5 = self.addSwitch('S5')

        self.addLink(H1,S1,1,1)
        self.addLink(S1,S3,3,1)
        self.addLink(S1,S2,2,1)
        self.addLink(S2,S5,2,3)
        self.addLink(S2,S4,3,2)
        self.addLink(S3,S5,2,1)
        self.addLink(S3,S4,3,3)
        self.addLink(S5,S4,2,1)
        self.addLink(S4,H2,4,1)

topos = {'mytopo':(lambda:Topology())}
