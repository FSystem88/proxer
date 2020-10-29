#!/usr/bin/python3
import requests as r
from colorama import Fore,Style
url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http"
req = r.get(url)
ip = r.post("http://v4.ident.me/").text
array = req.text.split()
for prox in array:
	try:
		ipx = r.get("http://v4.ident.me/", proxies={'http':prox, 'https':prox}, verify=False, timeout=10).text
	except:
		ipx = ip
	if ip != ipx:
		print(Fore.GREEN+"{} good!".format(prox))
		f = open("TESTPROX.txt", "a+")
		f.write("{}\n".format(prox))
		f.close()
	else:
		print(Fore.RED+"{} bad".format(prox))
