#!/bin/python
from netaddr import IPNetwork, IPAddress
import sys
'''
TODO
# add file as a source for ip list
# append to said list
# iterate on the list with ip_range()
# append the output to file
# get ipv6 to work too
'''
ip = sys.argv[1]
network = IPNetwork(ip)
ip_list = list(network)

'''
print 'For address/mask of %s\nbroadcast: %s\nnetmask: %s\nhostmask: %s\nsize: %s\nusable: %s\n' % (
        ip, network.broadcast, network.netmask, network.hostmask, network.size, network.size - 2
)

print 'Network length: %s\nFirst IP:%s\nSecond IP:%s\n' % (
        len(ip_list), ip_list[0], ip_list[-1]
)
'''
def ip_range():
        return 'IP range for %s: %s-%s\n' % (
                ip, ip_list[0], ip_list[-1]
        )

x = ip_range()

f = open('ip_range.txt', 'a')
f.write(str(x))
f.close()
'''
print 'Excluding broadcast and network address: %s-%s' % (
        ip_list[1], ip_list[-2]
)
'''
