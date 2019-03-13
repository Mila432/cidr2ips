import binascii
import io
import socket
import struct
import sys

def save(d,f):
	with io.open(f, 'a', encoding='utf8') as the_file:
		the_file.write('%s'%(unicode(d)))

def ip2hex(ip='127.0.0.1'):
	return int(binascii.hexlify(socket.inet_aton(ip)).upper(),16)

def hex2ip(hex_ip):
    return socket.inet_ntoa(struct.pack(">L", hex_ip))

def getmax(n2):
	return 2**(32-int(n2))

with open(sys.argv[1]) as f:
	content = f.readlines()
	content = [x.strip() for x in content]
for cidr in content:
	ips=set([])
	max=getmax(cidr.split('/')[-1])
	ip=ip2hex(cidr.split('/')[0])
	while(len(ips)<max):
		ips.add(ip+len(ips))
	save('\n'.join([hex2ip(x) for x in ips]),'ips.txt')