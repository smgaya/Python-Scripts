#!/usr/bin/env python

import crypt, sys


def printer(thing):
	sys.stdout.write(thing+"                         \r")
	sys.stdout.flush()
	return True


def cracker(passcrypt, dicfile):
	count=1
	lines = len(open(dicfile).readlines())
	dicfile = open(dicfile, 'r')
	for word in dicfile:
		printer("["+str(count)+"/"+str(lines)+"]")
		count+=1
		password = word.strip('\n')
		cryptword = crypt.crypt(password, passcrypt)
		if cryptword == passcrypt:
			print("\n[+]Password Found: "+word)
			return True

	print("[-]Not Found!")

try:
	filepass = sys.argv[1]
	dictfile = sys.argv[2]
except:
	print('#Usage:\n\tpython linuxcracker.py passfile.txt dictfile.txt')
	exit(0)

readpass = open(filepass, 'r')

for line in readpass:
	user = line.split(':')[0]
	cryptpass = line.split(':')[1].strip(' ')
	print("[*] Cracking | User: "+user)
	cracker(cryptpass, dictfile)

