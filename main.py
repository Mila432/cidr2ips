import binascii
import io
import socket
import struct
import sys

def save(d,f):
	with io.open(f, 'w', encoding='utf8') as the_file:
		the_file.write('%s'%(unicode(d)))

def ip2hex(ip='127.0.0.1'):
	return int(binascii.hexlify(socket.inet_aton(ip)).upper(),16)

def hex2ip(hex_ip):
    return socket.inet_ntoa(struct.pack(">L", hex_ip))

def getmax(n2):
	return 2**(32-int(n2))

max=getmax(sys.argv[1].split('/')[-1])

ips=set([])

ip=ip2hex(sys.argv[1].split('/')[0])
while(len(ips)<max):
	ips.add(ip+len(ips))
save('\n'.join([hex2ip(x) for x in ips]),'ips.txt')