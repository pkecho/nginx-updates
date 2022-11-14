#!/usr/bin/env python

__author__ = 'pkecho'
__version__ = '1.0.1'
__maintainer__ = 'pkecho'
__status__ = 'Development'

from bs4 import BeautifulSoup
from datetime import date
import requests
import os

changes = 'Changes with nginx'
security = 'Security:'
source = requests.get('http://nginx.org/en/CHANGES').text
soup = BeautifulSoup(source, 'lxml')
logs = soup.body.p.text
year = date.today().year


def write_log():
    with open('/tmp/test.txt', 'w') as file:
        file.write(logs)

def version_changes():
    with open('/tmp/test.txt', 'r') as file:
        for line in file:
            if changes in line:
                line = line.split()
                if int(line[6]) == int(year):
                    nversion = line[3]
                    ndate = line[4] + ' ' + line[5] + ' ' + line[6]
                    print(nversion + ' ' + ndate)
            if security in line:
                print(nversion + ' had a security update')

def main():
    write_log()
    version_changes()
    # Remove if you want to keep the logs
    os.remove("/tmp/test.txt")

if __name__ == '__main__':
    main()