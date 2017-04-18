#! /usr/bin/env python3
# socialMedia.py - Launches directly to a social media page of choosing.

import webbrowser
import sys

def socialMedia():
    sites = ['twitter', 'facebook', 'instagram', 'linkedin', 'github']
    #Get social media site from command line.
    if(len(sys.argv) > 1):
        social = sys.argv[1]
    print('Which social media site do you want to go to? Choose from the following list.')
    for i in range(len(sites)):
        print(sites[i])
    social = str(input()).lower()
    if(social in sites):
        webbrowser.open('https://www.' + social + '.com/')
    else:
        print('Entry was not part of the list. Exiting.')
        sys.exit()

socialMedia()
