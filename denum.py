import argparse
import dns.query
import dns.resolver
import dns.zone
from ipwhois import IPWhois
import jsondate as json
import os
import pythonwhois
from pprint import pprint
import re
import requests
import socket
import sys
from termcolor import colored
import time
import tqdm


print(colored('''




██████╗ ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██╔══██╗██╔════╝████╗  ██║██║   ██║████╗ ████║
██║  ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
██║  ██║██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
██████╔╝███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝


A Simple Domain Enumeration Script

''','green', attrs=['bold']))

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Input Target', required=True, dest='target')

args = parser.parse_args()


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error:
    print(colored('Failed to create socket. Error code: ' + str(msg[0]) + ' Error Message: ' + str(msg[1]), 'red'))
    sys.exit();

print('*' * 20)
print('\n')
print(colored('[*] Scanner Created', 'yellow', attrs=['bold']))
print('\n')

target = args.target

print(colored('[*] Grabbing Host IP and Checking DNS Records', 'yellow', attrs=['bold']))
print('\n')
try:
    host = socket.gethostbyname(target)
    resolver = dns.resolver.Resolver()
    a_record = resolver.query(target, 'A')
    mx_record = resolver.query(target, 'MX')
    ns_record = resolver.query(target, 'NS')
    txt_record = resolver.query(target, 'TXT')
    print('*' * 20)
    print('\n')
    print(colored('[*] DNS Lookup Results: ', 'yellow', attrs=['bold']))
    print('\n')
    for data in a_record:
        print(colored('A Record: ', 'yellow'))
        print(data)
    print('\n')
    for data in mx_record:
        print(colored('MX Record: ', 'yellow'))
        print(data)
    print('\n')
    for data in ns_record:
        print(colored('NS Record: ', 'yellow'))
        print(data)
    print('\n')
    for data in txt_record:
        print(colored('TXT Record: ', 'yellow'))
        print(data)
    print('\n')
    print(colored('[*] Getting Whois Information:', 'yellow', attrs=['bold']))
    print('\n')
    print(colored('Whois Information: ', 'yellow'))
    print('\n')
    info = pythonwhois.get_whois(target)
    pprint(info['raw'])
    print('\n')
    print(colored('IP Whois Information: ', 'yellow'))
    obj = IPWhois(host)
    results = obj.lookup_rdap(depth=1)
    print('\n')
    print('Name: ' + results['network']['name'])
    print('CIDR Range: ' + results['network']['cidr'])
    print('\n')
    print(colored('[*] Reverse DNS Search: ', 'yellow', attrs=['bold']))
    print('\n')
    request = 'https://api.hackertarget.com/reversedns/?q=' + target
    r = requests.get(request)
    print(r.text)
    print('\n')
    print(colored('[*] Checking For Sites On The Same IP', 'yellow', attrs=['bold']))
    print('\n')
    request2 = 'http://api.hackertarget.com/reverseiplookup/?q=' + host
    r2 = requests.get(request2)
    print(r2.text)
    print('\n')

except:
    print('Query Failed!')

print('\n')
print(colored('[*] Target resolves to ' + host + '\n', 'yellow', attrs=['bold']))
print('\n')
time.sleep(1)


print('*' * 20)
print('\n')
print(colored('[*] Domain Enumeration Complete!', 'yellow', attrs=['bold']))
print('\n')
print('*' * 20)
print('\n')
