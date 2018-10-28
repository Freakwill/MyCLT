#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

wifi = "http://192.168.100.2"

parser = argparse.ArgumentParser(description='Login zjc_wifi')
parser.add_argument('-u', dest='url', action='store', default=wifi, metavar='URL')
parser.add_argument('-l', dest='headless', action='store_true', default=True, help='set headless or not (default is True)')
parser.add_argument('-p', dest='password', action='store', default="050050", metavar='PASSWORD')
parser.add_argument('-n', dest='username', action='store', default="800052", metavar='USERNAME')
args = parser.parse_args()

options = Options()
if args.headless:
    options.set_headless(headless=True)
driver = webdriver.Chrome(executable_path='/usr/local/Caskroom/chromedriver/2.41/chromedriver', chrome_options=options)

driver.get(args.url)

try:
    # change the names according to the .html file
    username = driver.find_element_by_name('DDDDD')
    password = driver.find_element_by_name('upass')
    button = driver.find_element_by_name('0MKKey')

    username.send_keys(args.username)
    password.send_keys(args.password)
    button.click()
except Exception as e:
    print(e)
    print('Wifi may have been connected.')
finally:
    driver.quit()
