#! /usr/env/bin python3
#! dateFinder.py
import re
import pyperclip

'''
How dates look (generally, USA):
03/03/1991
03-03-1991
03/03/91
03-03-91
3/3/1991
3-3-1991
3/3/91
3-3-91
1991/03/12
1991-03-12
2017-2-17
17-2-17
03032017
20170303
'''

'''
I think the following regexes cover my use cases:
(\d{2}[\s\./-]?\d{2}[\s\./-]?\d\d) #mm/-. dd/-. yy
(\d{2}[\s\./-]?\d{2}[\s\./-]?\d{4}) #mm/-. dd/-. yyyy
(\d[\s\./-]?\d[\s\./-]?\d{4}) #m/-. d/-. yyyy
(\d[\s\./-]?\d[\s\./-]?\d{4}) #m/-. d/-. yyyy
(\d{4}[\s\./-]?\d{2}[\s\./-]?\d{2}) #yyyy/-. dd/-. mm
(\d{4}[\s\./-]?\d[\s\./-]?\d{2}) #yyyy/-. d/-. mm
(\d{4}[\s\./-]?\d[\s\./-]?\d) #yyyy/-. d/-. m
'''

dateRE = re.compile(r'''(
    (\d{4}|\d{2}|\d) # this should cover what I wrote at least
    ([\s\./-]?) # Cover separator (or none if not there)
    (\d{2} | \d) # Covers month under my above assumptions.
    ([\s\./-]?) # Cover separator (or none if not there)
    (\d{4}|\d{2}|\d) # Similar to first, can be day or year
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in dateRE.findall(text):
    matches.append(groups[0])
    print(groups)

#TODO: Find a way to convert the dates to a centralized format.
# I.E. 20170303->03/03/2017
""""
#This does not work as I had originally thought.
sep = re.compile(r'\d\d([\s\./-]?)')
sep.sub('\1HELLO',text)
hello = []
for sup in dateRE.findall(text):
    hello.append(sup[0])
    print(sup)
"""

if(len(matches)>0):
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates found. Exiting...')
