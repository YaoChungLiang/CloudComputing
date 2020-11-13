from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.ofproto import ether
from ryu.ofproto import inet
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import arp
from ryu.lib.packet import ipv4
from ryu.lib.packet import tcp
from ryu.lib.packet import udp
from ryu.lib.packet import icmp
from ryu.lib.packet import ether_types


class MySwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    
    def __init__(self, *args, **kwargs):
        super(MySwitch, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
    
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        
        # need to change my mach here
        match = parser.OFPMatch()
        # need to change actions here
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)]
        
        self.add_flow(datapath, 0, match, action)
    
    
    # not sure if I need to change something in the add-flow
    def add_flow(self, datapath, priority, match, actions, buffer_id=None):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        
        # instruction need to take a look
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
        if buffer_id:
            mod = parser.OFPFlowMod(datapath = datapath, buffer_id=buffer_id,
                                    priority = priority, match = match,
                                    instructions = inst)
        else:
            mod = parser.OFPFlowMod(datapath = datapath,
                                    priority = priority, match = match,
                                    instructions = inst)
        datapath.send_msg(mod)
        
        
    def _send_packet(self, datapath, port, pkt):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        pkt.serialize()
        self.logger.info(f'packet-out {pkt}')
        data = pkt.data
        actions = [parser.OFPActionOutput(port = port)]
        out = parser.OFPPacketOut(datapath = datapath,
                                  buffer_id = msg.buffer_id,
                                  in_port = ofproto.OFPP_CONTROLLER,
                                  actions = actions,
                                  data = data)
        datapath.send_msg(out)
        
    
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        if ev.msg.msg_len < ev.msg.total_len:
            self.logger.debug(f'packet truncated: only {ev.msg.msg_len} of {ev.msg.total_len} bytes')
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']
        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]
        
        # check if it is ARP
        '''
        pk_arp = pkt.getprotocol(arp.arp)
        if pk_arp:
            if src not in self.net.nodes:
                self.AddHosts(src, datapath.id, in_port)
            print(f'[ARP] arrive aat {datapth.id} {dst}')
            if dst in self.net.nodes:
                pass
        '''
        
        # check if it's TCP from S2 and S4
        '''
        if pkt_tcp:
           print(f'[TCP] arrive at {datapath.id} {dst}')
           src_host_list = [n for n in self.net.neighbors(src)]
           src_sw_id = src_host_list[0]
           if (src_sw_id == 2 or src_sw_id== 4) and (pkt_tcp.dst_port == 80):
               mypkt = packet.Packet()
               mypkt.add_protocol(ethernet.ethernet(ethertype = eth.ethertype, 
                                                    src = dst, 
                                                    dst = src))
               mypkt.add_protocol(ipv4.ipv4(src = pkt_ipv4.dst,
                                            dst = pkt_ipv4.src, 
                                            proto = 6))
               mypkt.add_protocol(tcp.tcp(src_port = pkt_tcp.dst_port,
                                          dst_port = pkt_tcp.src_port,
                                          sck = pkt_tcp.seq+1,
                                          bits = 0b010100))
               self.send_packet(datapath, in_port, mypkt)
               print('TCP: Reject connection')
        '''
        
        # ignore, drop lldp packet
        if eth.ethertype == ether_types.ETH_TYPE_LLDP:
            return
            
        dst = eth.dst
        src = eth.src
        
        dpid = format(datapath.id, "d").zfill(16)
        self.mac_to_port.setdefault(dpid, {})
        
        self.logger.info(f'packet in {dpid}, {src}, {dst}, {in_port}')
        
        # learn a mac address to avoid FLOOD next time
        self.mac_to_port[dpid][src] = in_port
        
        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]
        else:
            # if no dst position, just flooding
            out_port = ofproto.OFPP_FLOOD
            
        actions = [parser.OFPActionOutput(out_port)]
        
        # install a flow to avoid packet_in next time
        if out_port != ofproto.OFPP_FLOOD:
            match = parser.OFPMatch(in_port = in_port,
                                    est_dst = dst,
                                    eth_src = src)
            if msg.buffer_id != ofproto.OFP_NO_BUFFER:
                self.add_flow(datapath, 1, match, actions, msg.buffer_id)
                return
            else:
                self.add_flow(datapath, 1, match, actions)
        
        data = None
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data
            
        out = parser.OFPPacketOut(datapath = datapath,
                                  buffer_id = msg.buffer_id,
                                  in_port = in_port,
                                  actions = actions,
                                  data = data)
        datapath.send_msg(out)    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
                          
        
        
        
        
