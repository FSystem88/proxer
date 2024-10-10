#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dev: FSystem88

import requests as r, os, threading, random
from threading import Thread
from colorama import Fore,Style,Back

def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def logo():
	colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
	color1 = random.choice(colors)
	colors.remove(color1)
	color2 = random.choice(colors)
	print(color1+"████████████████████████████████████\n█▄─▄▄─█▄─▄▄▀█─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█\n██─▄▄▄██─▄─▄█─██─██▀─▀███─▄█▀██─▄─▄█\n█▄▄▄███▄▄█▄▄█▄▄▄▄█▄▄█▄▄█▄▄▄▄▄█▄▄█▄▄█\n███████████"+color2+" by FSystem88 "+color1+"███████████\n████████████████████████████████████\n"+Style.RESET_ALL)

def check(ip, prox, qtime):
	try:
		ipx = r.get("https://ident.me", proxies={'http':'http://{}'.format(prox), 'https':'http://{}'.format(prox)}, timeout=qtime).text
	except:
		ipx = ip
	if ip != ipx:
		print(Fore.GREEN+"{} good!".format(prox))
		f = open("proxies.txt", "a+")
		f.write("{}\n".format(prox))
		f.close()
	else:
		print(Fore.RED+"{} bad".format(prox))

clear()
logo()
try:
	qtime = int(input("Timeout proxy [seconds] (0 - all): "))
	if qtime == 0:
		qtime = None
except:
	print(Fore.RED+"\nIncorrect timeout proxy\n")
	exit()
req = r.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http")
array = req.text.split()
ip = r.post("https://ident.me").text
print(Back.GREEN+"Your ip: {}\n".format(ip)+Style.RESET_ALL)
open("proxies.txt", "w+").close()
for prox in array:
	thread_list = []
	t = threading.Thread (target=check, args=(ip, prox, qtime))
	thread_list.append(t)
	t.start()
