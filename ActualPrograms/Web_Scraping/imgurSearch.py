#! /usr/bin/env python3
# imgurSearch.py - Launches new tabs for image searches.
import webbrowser
import sys
import pyperclip
import requests
from bs4 import BeautifulSoup

def imgurSearch():
    imgurBasis = 'http://imgur.com/search/score?q='
    if(len(sys.argv)>1):
        terms = ' '.join(sys.argv[1:])
        print('You searched for ' + terms + '.')
        terms = terms.replace(' ', '+')
    else:
        terms = pyperclip.paste()
        print('You searched for ' + terms + '.')
        terms = terms.replace(' ', '+')
    searches = imgurBasis+terms
    print('Getting imgur photo search page...')
    res = requests.get(searches)
    res.raise_for_status()
    #print(res)
    c = res.content
    soup = BeautifulSoup(c, 'html.parser')
    elements = soup.find_all('a', {'class': 'image-list-link'})
    #for i in range(len(elements)):
    #    print(elements[i])
    #    print('\n\n')
    #print(elements)
    #print(len(elements))
    c = 0
    for i in range(0,10):
        try:
            links = elements[i].find('img')['src']
            links = links[2:]
            webbrowser.open('https://' + links)
            c+=1
        except TypeError:
            continue
    print('There should have been ' + str(c) + ' different results.')

imgurSearch()
