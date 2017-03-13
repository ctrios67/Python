#! /usr/bin/env python3
# productivity.py

import time
from datetime import datetime as dt
# '/etc/hosts'
# r'C:\Windows\System32\drivers\etc'
# 'C:\\Windows\\System32\\drivers\\etc'

hosts_path = '/etc/hosts/'
redirect = '127.0.0.1'
website_list = ['www.facebook.com','facebook.com',
             'www.twitter.com', 'twitter.com',
             'www.reddit.com', 'reddit.com',
             'www.instagram.com', 'instagram.com']

while True:
    if(dt(dt.now().year, dt.now().month, dt.now().day, 8) < (dt(dt.now().year, dt.now().month, dt.now().day, 16))):
        print('Working Hours...')
    else:
        print('Fun hours...')
    time.sleep(5)
