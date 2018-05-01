#-*-coding = utf-8-*-

"""
   Version : 0.1
   eample of use : python ftp_bf.py -t ftp.server.com -u username -p password
"""

import sys, os
from ftplib import FTP
import argparse

 
def login(hostname, username, password):
    try:
        ftp = FTP(hostname)
        ftp.login(username, password)
        ftp.retrlines('list')
        ftp.quit()
        print("\n We did it !")
        print("Target : ", hostname)
        print("User : ", username)
        print("Password : ", password)
    except Exception as e:
        print('WTF: ', e) 
    except KeyboardInterrupt: 
        print("\nExiting ...\n")
        sys.exit(1)
 
def anon_login(hostname):
    try:
        print("\n[!] Checking for anonymous login.\n")
        ftp = FTP(hostname)
        ftp.login()
        ftp.retrlines('LIST')
        print("\n[!] Anonymous login successfuly!\n")
        ftp.quit()
    except Exception as e:
        print("\n[-] Anonymous login failed...\n")


parser = argparse.ArgumentParser(description='Get Wifi')
parser.add_argument('-t', action='store', dest='hostname', default='ftp.server.com', metavar='HOSTNAME')
# parser.add_argument('-t', action='store', dest='target', default='', metavar='TARGET')
parser.add_argument('-u', action='store', dest='username', default='', metavar='USERNAME')
parser.add_argument('-p', action='store', dest='password', default='', metavar='PASSWORD')

args = parser.parse_args()

if args.username:
    login(args.hostname, args.username, args.password)
else:
    anon_login()
