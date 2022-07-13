#!/usr/bin/env python3

import argparse
import os
import sys
import re
from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup
from termcolor import colored
from colored import fg, bg, attr

#ascii banner for the CLI news app tool
ret=os.system('toilet --filter metal --filter border:metal -w 100 -f slant CyberSecNewsApp')
print('\n \033[1m\033[3m' + 'Created by Nrchy' +  '\033[0m \n')

#system information while running the program
if sys.version_info[0] < 3:
print("Python3 is needed to run NewsApp, Try \"python3 project2.py\" instead\n")
sys.exit(2)

#message for the tool
def msg(name=None):
return''' -> python3 file.py -n
[This option is used for displaying the urls and links.]
[It doesn't require any arguments.]
'''

#examples for reference
example = "\nEXAMPLES: \n"
example += "----------------------------------------------------------------------------------------------> \n"
example += "root@kali:~/# python3 file.py -n  #Display the titles and the URLs related to the search query \n"
example += "----------------------------------------------------------------------------------------------> \n"

#description about the tool
parser = argparse.ArgumentParser(description='Cyber Security News App CLI Tool for Latest News', epilog=example, formatter_class=argparse.RawDescriptionHelpFormatter, usage=msg())

#mutually exclusive group title for query option
group1 = parser.add_argument_group('Query option (no arguments required)')
#query to search
group1.add_argument('-n', help='The query to start news search', required=True, action='store_true')

args = parser.parse_args()

'''
#Error message for when the option is not provided
if (args.n == False):
parser.error(colored('%sYou have to provide some option!', 'red') % (attr('bold')))
print("Try these:")
print(parser.epilog)
'''

if (args.n):
print(colored('%sLatest news about vulnerabilities and attacks: \n', 'green') % (attr('bold')))

#bleepingcomputer
req = urllib.request.Request(
        "https://www.bleepingcomputer.com/news/security/",
        data=None,
       
headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
)

html_page = urllib.request.urlopen(req)
soup = BeautifulSoup(html_page, "html.parser")
links = set(soup.findAll('a', class_='nmic', attrs={'href': re.compile("^https://www.bleepingcomputer.com/news/.*[^0-9]/$")}))
i = 1
for l in links:
    if l.img:
        print(str(i) + '. ' + l.img['alt'])
    print(l.get('href'))
    i+=1
    print()
