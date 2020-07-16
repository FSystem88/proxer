#!/usr/bin/python3
import proxyscrape, urllib3, requests, os
from sys import argv
from os import system as terminal
from colorama import Fore,Style

URL = "http://google.com"
TIMEOUT = (3.05,27)

def check_proxy(proxy):
	try:
		session = requests.Session()
		session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
		session.max_redirects = 300
		print(Fore.LIGHTYELLOW_EX + 'Checking ' + proxy)
		session.get(URL, proxies={'https':'https://' + proxy}, timeout=TIMEOUT,allow_redirects=True)
	except requests.exceptions.ConnectionError as e:
		print(Fore.LIGHTRED_EX + 'Error!')
		return e
	except requests.exceptions.ConnectTimeout as e:
		print(Fore.LIGHTRED_EX + 'Error,Timeout!')
		return e
	except requests.exceptions.HTTPError as e:
		print(Fore.LIGHTRED_EX + 'HTTP ERROR!')
		return e
	except requests.exceptions.Timeout as e:
		print(Fore.LIGHTRED_EX + 'Error! Connection Timeout!')
		return e
	except urllib3.exceptions.ProxySchemeUnknown as e:
		print(Fore.LIGHTRED_EX + 'ERROR unkown Proxy Scheme!')
		return e
	except requests.exceptions.TooManyRedirects as e:
		print(Fore.LIGHTRED_EX + 'ERROR! Too many redirects!')
		return e
os.system('cls' if os.name=='nt' else 'clear')
print(Fore.GREEN+"Enter params:\n • code (ru, us, ...)\n • anonymous (True / False)\n • type (http, https)"+Style.RESET_ALL)
_code=input("code > ")
_anonymous=input("anonymous > ")
_type=input("type > ")
params={}
if _code != "":
	params['code']=_code
if _type != "":
	params['type']=_type
if _anonymous == "":
	pass
elif _anonymous == "True":
	params['anonymous']=True
elif _anonymous == "False":
	params['anonymous']=False
else:
	pass

collector = proxyscrape.create_collector('default', 'http')
print("Ваши параметры: "+params)
while True:
	proxy = collector.get_proxy(params)
	prox='{}:{}'.format(proxy[0],proxy[1])
	if check_proxy(prox):
		print(Fore.LIGHTRED_EX + 'BAD PROXY ' + prox)
	else:
		print(Fore.LIGHTGREEN_EX + 'GOOD PROXY ' + prox)
		file="proxies.txt"
		f=open(file)
		array=f.read().splitlines()
		if prox in array:
			print("{} already exist in proxies.txt".format(prox))
		else:
			f=open(file, "a+")
			f.write(prox+"\n")
			f.close
