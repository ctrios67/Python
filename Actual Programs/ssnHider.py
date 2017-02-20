#! /usr/env/bin python3
#! ssnHider.py
import re
import pyperclip

'''
Hey whats up everybody
SSNs look like: 9 digits long
000-00-0000
000.00.0000
000/00/0000
123456789
Which look like telephone numbers...I can use a similar regex for that.

CCs look like: 16 digits long
1234-5678-9012-3456
'''

ssnRE = re.compile(r'''(
    (\d{3}) # first 3 digits
    ([\s\./-]?) # separator
    (\d{2}) # next 3
    ([\s\./-]?) # separator
    (\d{4}) # last 4
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in ssnRE.findall(text):
    matches.append(groups[0])
    print(groups)

#TODO: Hide the numbaz
num1 = re.compile(r'\d')
redacted = num1.sub(r'*',text) 
print(redacted)

if(len(matches)>0):
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No Social Security Numbers found, Exiting...')
