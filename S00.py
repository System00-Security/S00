#!/usr/bin/env python3
__author__      = "Joy Ghosh"
__Ver__         = "V 1.0"
__copyright__   = "Copyright 2021, SYSTEM00 SECURITY"
#############################################[ API KEY ]
api_key="Your_Shodan_API_KEY"
############################################
from colorama import Fore, Back, Style
import requests
import json
import socket
import argparse
def logo():
    print(Fore.RED,"""

    █▀ █▀█ █▀█
    ▄█ █▄█ █▄█   [DEV : JOY GHOSH]
---------------------
Shodan Based scanner
    """,Fore.WHITE)


def shodan_result(ip):
    shodan='https://api.shodan.io/shodan/host/'+ip+'?key='+api_key
    req=requests.get(shodan)
    reqs=req.text
    lod=json.loads(reqs)
    # OS Detect
    print(Fore.GREEN+"[+] OS Detect"+Fore.WHITE)
    print(" ")
    os=lod["os"]
    print('OS :',ip,Fore.RED,'[',os,']',Fore.WHITE)
    print(" ")
    #Port_Scan
    ports=lod["ports"]
    print(Fore.GREEN+"[+] Open Ports"+Fore.WHITE)
    print(" ")
    for port in ports:
        print(ip,":",Fore.RED,port,Fore.WHITE)
    print(" ")
    try:
        vulns=lod["vuln"]
        print(Fore.GREEN+"[+] Vulnerability"+Fore.WHITE)
        print(" ")
        for vuln in vulns:
            print(ip,":",Fore.RED,vuln,Fore.WHITE)
    except KeyError:
        print(" ")
        print(Fore.GREEN+"[+] Vulnerability"+Fore.WHITE)
        print(" ")
        print(Fore.RED+"No CVE Found"+Fore.WHITE)
        print(" ")
    except:
        exit()
logo()
try:
  parser = argparse.ArgumentParser()
  parser.add_argument("-l", "--list", help="Your Subdomain list Exp: -l subdomains.txt ", type=str)
  args = parser.parse_args()
  with open(args.list, "r") as hosts:
      for host in hosts:
          ip=socket.gethostbyname(host.strip())
          print(Fore.GREEN+"[+] SCANING: "+host+Fore.WHITE)
          shodan_result(ip)
          print(Fore.RED+"--------------------------"+Fore.WHITE)
except TypeError:
  print("No File Detected type -h to see all flags")
except:
  exit()
