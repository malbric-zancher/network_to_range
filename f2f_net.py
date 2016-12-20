#!/bin/python
from netaddr import IPNetwork, IPAddress
import sys

source_filename = sys.argv[1] # takes 1 argument = a filename preferably txt
reading = open(source_filename, 'r').readlines() # opens it for reading line by line
source_ip_list = [] # create empty list to store ranges in it

# loop over file, strip newlines, append to list
for i in reading:
        i = i.strip('\n')
        source_ip_list.append(i)

for net_range in source_ip_list: # loop over networks list
        net_network_addr = IPNetwork(net_range).network # use network address as 1st
        net_broadcast_addr = IPNetwork(net_range).broadcast # use broadcast address as last

        def pretty_range():
                return 'IP range for %s = %s-%s\n' % (
                        net_range, net_network_addr, net_broadcast_addr
                )

        results = pretty_range()
        output_filename = 'output_range.txt'

        f = open(output_filename, 'a') # 'w' will overwrite leaving only last value
        f.write(str(results))
        f.close()
