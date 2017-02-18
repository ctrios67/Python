#! /usr/env/bin python3
#! ssnHider.py
import re
import pyperclip

'''
Hey whats up everybody
SSNs look like: 10 digits long
000-000-0000
000.000.0000
000/000/0000
0000000000
Which look like telephone numbers...I can use a similar regex for that.

CCs look like: 16 digits long
1234-5678-9012-3456
'''

ssnRE = re.compile(r'''(
    (\d{3}) # first 3 digits
    ([\s\./-]?) # separator
    (\d{3}) # next 3
    ([\s\./-]?) # separator
    (\d{4}) # last 4
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in ssnRE.findall(text):
    matches.append(groups[0])
    print(groups)

#TODO: Hide the numbaz
num1 = re.compile(r'(\d{3})/')
num1.sub('\1****',text)
hello = []
for sup in ssnRE.findall(text):
    hello.append(sup[0])
    print(sup)

if(len(matches)>0):
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No Social Security Numbers found, Exiting...')
