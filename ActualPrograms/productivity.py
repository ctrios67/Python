#! /usr/bin/env python3
# productivity.py

import time
from datetime import datetime as dt
import os
# '/etc/hosts'
# r'C:\Windows\System32\drivers\etc'
# 'C:\\Windows\\System32\\drivers\\etc'

hosts_path = '/etc/hosts'
hosts_temp = 'hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com','facebook.com',
             'www.twitter.com', 'twitter.com',
             'www.reddit.com', 'reddit.com',
             'www.instagram.com', 'instagram.com']
beginWorkShift = dt(dt.now().year, dt.now().month, dt.now().day, 9)
endWorkShift = dt(dt.now().year, dt.now().month, dt.now().day, 17)

while True:
    currentTime = dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour)
    isWeekday = (currentTime.isoweekday()==6 or currentTime.isoweekday()==7)
    if( (currentTime > beginWorkShift) and (currentTime < endWorkShift) and (not isWeekday)):
        print('Working Hours...')
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    file.write(redirect + ' ' + website+'\n')
            print(content)
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if(not any(website in line for website in website_list)):
                    file.write(line)
            file.truncate()
        print('Fun hours...')
    time.sleep(5)
