
# adding rules for S1
ovs-ofctl add-flow S1 in_port=1,actions=output:3
ovs-ofctl add-flow S1 in_port=2,actions=output:1
ovs-ofctl add-flow S1 in_port=1,actions=output:2
ovs-ofctl add-flow S1 in_port=2,actions=output:3
ovs-ofctl add-flow S1 in_port=3,actions=output:1
ovs-ofctl add-flow S1 in_port=3,actions=output:2

ovs-ofctl add-flow S2 in_port=1,actions=output:3
ovs-ofctl add-flow S2 in_port=3,actions=output:1
ovs-ofctl add-flow S2 in_port=2,actions=output:1
ovs-ofctl add-flow S2 in_port=2,actions=output:3
ovs-ofctl add-flow S2 in_port=1,actions=output:2
ovs-ofctl add-flow S2 in_port=3,actions=output:2

ovs-ofctl add-flow S3 in_port=1,actions=output:3
ovs-ofctl add-flow S3 in_port=1,actions=output:2
ovs-ofctl add-flow S3 in_port=2,actions=output:1
ovs-ofctl add-flow S3 in_port=2,actions=output:3
ovs-ofctl add-flow S3 in_port=3,actions=output:2
ovs-ofctl add-flow S3 in_port=3,actions=output:1

ovs-ofctl add-flow S4 in_port=3,actions=output:4
ovs-ofctl add-flow S4 in_port=4,actions=output:2
ovs-ofctl add-flow S4 in_port=1,actions=output:4
ovs-ofctl add-flow S4 in_port=2,actions=output:1
ovs-ofctl add-flow S4 in_port=2,actions=output:3
ovs-ofctl add-flow S4 in_port=2,actions=output:4
ovs-ofctl add-flow S4 in_port=3,actions=output:1
ovs-ofctl add-flow S4 in_port=3,actions=output:2
ovs-ofctl add-flow S4 in_port=1,actions=output:2
ovs-ofctl add-flow S4 in_port=4,actions=output:1
ovs-ofctl add-flow S4 in_port=1,actions=output:3
ovs-ofctl add-flow S4 in_port=4,actions=output:3

ovs-ofctl add-flow S5 in_port=1,actions=output:2
ovs-ofctl add-flow S5 in_port=1,actions=output:3
ovs-ofctl add-flow S5 in_port=2,actions=output:1
ovs-ofctl add-flow S5 in_port=2,actions=output:3
ovs-ofctl add-flow S5 in_port=3,actions=output:1
ovs-ofctl add-flow S5 in_port=3,actions=output:2
