#!/bin/python
from netaddr import IPNetwork, IPAddress
import sys
'''
TODO
# get ipv6 to work too
'''
source_filename = sys.argv[1] # takes 1 argument = a filename preferably txt
reading = open(source_filename, 'r').readlines() # opens it for reading line by line
source_ip_list = [] # create empty list to store ranges in it

# loop over file, strip newlines, append to list
for i in reading:
        i = i.strip('\n')
        source_ip_list.append(i)

for net_element in source_ip_list: # loop over networks list
        network = IPNetwork(net_element) # translate networks to IP
        ip_list = list(network) # create list from IPs

        def ip_range(): # return pretty source network + 1st + last IP
                return 'IP range for %s: %s-%s\n' % (
                        net_element, ip_list[0], ip_list[-1]
                )

        results = ip_range()
        output_filename = 'output_range.txt'

        f = open(output_filename, 'a') # 'w' will print only last value
        f.write(str(results))
        f.close()
