
# adding rules for H1 -> H2 other package path
ovs-ofctl add-flow S1 priority=100,in_port=1,actions=output:3
ovs-ofctl add-flow S3 priority=100,in_port=1,actions=output:2
ovs-ofctl add-flow S5 priority=100,in_port=1,actions=output:2
ovs-ofctl add-flow S4 priority=100,in_port=1,actions=output:4


# adding rules for H2 -> H1 other package path
ovs-ofctl add-flow S4 priority=100,in_port=4,actions=output:2
ovs-ofctl add-flow S2 priority=100,in_port=3,actions=output:2
ovs-ofctl add-flow S5 priority=100,in_port=3,actions=output:1
ovs-ofctl add-flow S3 priority=100,in_port=2,actions=output:1
ovs-ofctl add-flow S1 priority=100,in_port=3,actions=output:1
