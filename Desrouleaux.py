#!/usr/bin/env python
import re
#import math
import socket                                              
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('2018shell.picoctf.com', 14079)
sock.connect(server_address)

import json
with open('incidents.json', 'r') as f:
	json_data = json.load(f)
	stri = json.dumps(json_data)
	file = json.loads(stri)

def Q1(file):
        recvdata = sock.recv(4096).decode()
        #print(recvdata)
        ips = list()
        for i in range(len(file["tickets"])):
                ips.append((file["tickets"][i]["src_ip"].encode('ascii'), file["tickets"][i]["dst_ip"].encode('ascii')))

        tmp ={}
        for i in range(len(ips)):
                ip = ips[i][0]
                try:
                        tmp[ip] += 1
                except:
                        tmp[ip] = 1

        keys = list(tmp.keys())
        best = 0
        best_loc = -1
        for i in range(len(tmp.keys())):
                if(tmp[keys[i]] > best):
                        best = tmp[keys[i]]
                        best_loc = i
                        
        sock.sendall(keys[best_loc] + '\n'.encode())
        #print(keys[best_loc].decode())
        # without '\n', the code wouldn't work.
        return ips
        
def Q2(ips):
	ips_s = []
	for i in range(len(file["tickets"])):
                ips_s.append((file["tickets"][i]["src_ip"], file["tickets"][i]["dst_ip"]))
     # ips_s.encode('ascii')  -> ips
                
	recvdata = sock.recv(4096).decode()
	#print(recvdata)
	serarch_rule = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
	findall_ed = serarch_rule.findall(recvdata)
	##print(findall_ed)
	srcIP = findall_ed[0]
	
	tmp = []
	ans=0
	##print(ips_s)
	for i in range(len(ips_s)):
		if(ips_s[i][0] != srcIP):
			continue
		else:
			if ips_s[i][1] in tmp:
				continue
			else:
				tmp.append(ips_s[i][1])
				ans += 1
	
	#print(str(ans))
	sock.sendall((str(ans) + '\n').encode())
	return ips_s
	
def Q3(ips):
	recvdata = sock.recv(4096).decode()
	#print(recvdata)
	
	tmp = {}#dict
	##print(type(ips[0][1]))	str
	for i in range(len(ips)):
		k = ips[i][1] 
		if ips[i][1] in tmp:
			tmp[k] += 1
		else:
			tmp[k] = 1
	
	keys = list(tmp.keys())
	##print(type(keys))		list
	sum = 0.0
	for i in range(len(keys)):
		sum += tmp[keys[i]]
	out = (sum / len(keys))
	#print(out)
	sock.sendall((str(out) + '\n').encode())
	
	
t = Q1(file)
ts = Q2(t)
Q3(ts)
recvdata = sock.recv(4096).decode()

#print(recvdata)
search_rule = re.compile("picoCTF{.+}")
print(search_rule.findall(recvdata)[0])
sock.close()
