#! /usr/bin/env python3
# productivity.py

import time
from datetime import datetime as dt
# '/etc/hosts'
# r'C:\Windows\System32\drivers\etc'
# 'C:\\Windows\\System32\\drivers\\etc'

hosts_path = '/etc/hosts/'
hosts_temp = 'hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com','facebook.com',
             'www.twitter.com', 'twitter.com',
             'www.reddit.com', 'reddit.com',
             'www.instagram.com', 'instagram.com']

while True:
    if(dt(dt.now().year, dt.now().month, dt.now().day, 8) < (dt(dt.now().year, dt.now().month, dt.now().day, 16))):
        print('Working Hours...')
        with open(hosts_temp,'r+') as file:
            content = file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    file.write(redirect + ' ' + website+'\n')
            print(content)
    else:
        print('Fun hours...')
    time.sleep(5)
