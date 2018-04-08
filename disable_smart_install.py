#!/usr/bin/python
import telnetlib
import os
from IPy import IP
from multiprocessing.dummy import Pool as ThreadPool

password = "123456"
en_password = "654321"
##############################################################

def no_smart(host,password,en_password):
	rt =''
	try:
		tn = telnetlib.Telnet(host, port=23, timeout=3)
	except:
		print host + ' telnet connect error'
	tn.read_until('Password: ')
	tn.write(password + '\n')
	tn.read_until('>')
	tn.write('en\n')
	tn.read_until('Password: ')
	tn.write(en_password + '\n')
	tn.read_until('#')
	tn.write("conf t"+"\n")
	tn.read_until('#')
	tn.write('no vstack'+'\n')
	tn.write('do wr'+'\n')
	while True:
		t = tn.read_eager()
		rt = rt + t
		if '#' in t:
			break
	tn.close()

	return rt

def nmap_check(host):
	cmd = "nmap -p T:4786 " + host
	res = os.popen(cmd).readlines()
	if "4786/tcp open" in res[-3]:
		return True
	else:
		return False

def do(ip):
	host = str(ip)
	if nmap_check(host) == True:
		no_smart(host,password,en_password)
		print host + "smart install disabled"

if __name__=='__main__':
	ips = "192.168.0.0/24"
	pool = ThreadPool(32)
	pool.map(do,IP(ips))
	pool.close()
	pool.join()
