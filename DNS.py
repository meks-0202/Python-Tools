#!bin/bash/python3

import requests
from pyfiglet import  Figlet
import argparse
import sys

#parser = argparse.ArgumentParser()
#parser.add_argument("-h","--help", help="Know how to use the tool")
#parser.add_argument("-d","--domain", help="Enter the domain name to be scanned", required=True)
#parser.add_argument("-p","--payload", help="Input payload", required=True)
#args = parser.parse_args()

banner = Figlet(font='standard')
print(banner.renderText('Domain Scan'))

def domainscan(domain,subdomain):
	banner2 = Figlet(font='digital')
	print(banner2.renderText('Starting Scan'))
	#banner3 = Figlet(font='future')
	print("----URLs Found----")
	#print("URLs found: ")
	for sub in subdomain:
		url1 = f"http://{sub}.{domain}"
		url2 = f"https://{sub}.{domain}"
		try:
			requests.get(url1)
			print(f'[+] {url1}')
			requests.get(url2)
			print(f'[+] {url2}')
		except requests.ConnectionError:
			pass
	banner4 = Figlet(font='digital')
	print(banner4.renderText('Thankyou for using the tool :)'))
	
if __name__ == '__main__':		
	dom_name= input("Enter domain name for scanning: ")
	with open('Python-Tools/subdomain100.txt','r') as file:
		name=file.read()
		sub_dom=name.splitlines()
	
	domainscan(dom_name,sub_dom)

