#! /usr/bin/env python3
# facebookNewsFeedScrape.py - Grabs one's news feed data for no apparent reason
# except to demonstrate that Python can do such a thing.
import webbrowser
import sys
import pyperclip
import requests
from bs4 import BeautifulSoup

def redditScrape():
    reddit = 'https://www.reddit.com'
    print('Grabbing Reddit\'s front page content...')
    res = requests.get(reddit)
    res.raise_for_status()
    print(res)
    c = res.content
    soup = BeautifulSoup(c, 'html.parser')
    postTitle = soup.find_all('a', {'class': 'title may-blank'})
    print(postTitle)
    #print(elements)
    #print(len(elements))

redditScrape()
