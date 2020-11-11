#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import os

CHANGES = 'Changes with nginx'
SECURITY = 'Security:'
source = requests.get('http://nginx.org/en/CHANGES').text
soup = BeautifulSoup(source, 'html5lib')
logs = soup.find('body')


with open('/tmp/test.txt', 'w') as file:
    file.write(logs.prettify())

with open('test.txt', 'r') as file:
    for line in file:
        if CHANGES in line:
            line = line.split()
            nversion = line[3]
            ndate = line[4] + ' ' + line[5] + ' ' + line[6]
            print(nversion + ' ' + ndate)
        
        if SECURITY in line:
            print(nversion + ' had a security update')

os.remove("/tmp/test.txt")
