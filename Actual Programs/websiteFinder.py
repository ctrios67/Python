#! /usr/env/bin python3
#! websiteFinder.py
import re
import pyperclip

webRE = re.compile(r'''(
    (http:// | https://)? # hyper text transfer protocol
    ([a-zA-Z]{3}\.)* # world wide web
    ([a-zA-Z0-9_-])+ # the web domain
    (\.[a-zA-Z]{2,4}) # ending here only covers the root url...
    ([/?a-zA-Z0-9_/-])* # deeper in the url
    )''', re.VERBOSE | re.IGNORECASE)

text = str(pyperclip.paste())
matches = []
for groups in webRE.findall(text):
    matches.append(groups[0])

if(len(matches)>0):
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No websites found. Exiting...')
'''
stackoverflow.com/questions/1643772/forward-slash-in-a-python-regex
^I definitely used that link
https://web.groupme.com/chats
http://automatetheboringstuff.com/chapter7/
www.google.com
'''
