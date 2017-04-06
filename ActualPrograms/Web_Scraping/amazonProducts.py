#! /usr/bin/env python3
# amazonProducts.py - Launches new tabs for each product on the search page.
# search terms will be via command line or grabbed from clipboard of PC.
import webbrowser
import sys
import pyperclip
import requests
from bs4 import BeautifulSoup

def amazonSearch():
    confirm = input('This program opens up A LOT of browser tabs, are you okay with this? (y/n)')
    if(confirm.lower()=='y'):
        amazonBasis = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='
        if(len(sys.argv)>1):
            terms = ' '.join(sys.argv[1:])
            print('You searched for ' + terms + '.')
            terms = terms.replace(' ', '+')
        else:
            terms = pyperclip.paste()
            print('You searched for ' + terms + '.')
            terms = terms.replace(' ', '+')
        searches = amazonBasis+terms
        print('Getting Amazon product pages...')
        res = requests.get(searches)
        res.raise_for_status()
        #print(res)
        c = res.content
        soup = BeautifulSoup(c, 'html.parser')
        elements = soup.find_all('a', {'class': 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'})
        #for i in range(len(elements)):
        #    print(elements[i])
        #    print('\n\n')
        #print(elements)
        #print(len(elements))
        c = 0
        for i in range(len(elements)):
            try:
                links = elements[i]['href']
                webbrowser.open(links)
                c+=1
            except TypeError:
                continue
        print('There should have been ' + str(c) + ' different results.')
    else:
        print('I understand, no problem. Exiting...')
        sys.exit()

amazonSearch()
