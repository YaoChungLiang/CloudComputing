# adding rules for H1 -> H2  HTTP TCP path
ovs-ofctl add-flow S1 in_port=1,dl_type=0x0800,nw_proto=6,tcp_dst=80,actions=output:2
ovs-ofctl add-flow S2 in_port=1,dl_type=0x0800,nw_proto=6,tcp_dst=80,actions=output:3
ovs-ofctl add-flow S4 in_port=2,dl_type=0x0800,nw_proto=6,tcp_dst=80,actions=output:4


# adding rules for H2 -> H1 HTTP TCP path
ovs-ofctl add-flow S4 in_port=4,dl_type=0x0800,nw_proto=6,tcp_dst=80,actions=output:3
ovs-ofctl add-flow S3 in_port=3,dl_type=0x0800,nw_proto=6,tcp_dst=80,actions=output:1
ovs-ofctl add-flow S1 in_port=3,dl_type=0x0800,nw_proto=6,tcp_dst=80,actions=output:1

