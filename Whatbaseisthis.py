#!/usr/bin/env python3
import re
from pwn import *
p = remote("2018shell.picoctf.com",1225)
'''
  pwntools 공식 문서 : 설치법
  $sudo -i
  #apt-get update
  #apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
  #python3 -m pip install --upgrade pip
  #python3 -m pip install --upgrade pwntools
'''


temp = p.recv().decode()
print(temp)
regexrule = re.compile(r"\d{8}")
matchobj = regexrule.findall(temp)

answer = ''
for i in range(len(matchobj)): #0b 덧붙이고 2진수를 10진수로 변환, 그 후 문자로 변환
	if len(matchobj[i]) == 8:
		answer += chr(int('0b'+matchobj[i], 2))
print(answer)
p.send(answer+"\n")
#엔터키도 같이	#답안 보내기




temp = (p.recv().decode())
print(temp) #문제 읽어오기
regexrule = re.compile('the [0-9a-f]+')
matchobj = regexrule.findall(temp)
asciiq = matchobj[0][4:]

answer = ''
for i in range(len(asciiq)//2):
	answer +=chr(int('0x'+asciiq[2*i : 2+2*i], 16))
print(answer)
p.send(answer+'\n')




temp = p.recv().decode()
print(temp)# 
regexrule = re.compile(r"\d{3}")
matchobj = regexrule.findall(temp) # 숫자 3개가 연속해서 붙은 것들을 찾아냅니다.

answer = ''
for i in range(len(matchobj)):
	answer += chr(int('0o'+matchobj[i], 8))
print(answer)
p.send(answer+'\n')


temp = p.recv().decode()
print(temp)
