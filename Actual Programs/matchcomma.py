#! /usr/env/bin python3
#! matchcomma.py

import re
import pyperclip
import sys
'''
1
42
1,234
6,368,745
12,34,567
1234
'''
# This shit is stupid and I literally do not know why.
commaz = re.compile(r'^\d{1,3}(,\d{3})*$')

text = str(pyperclip.paste())
print(text+'\n---------------------------------')

matches = []
try:
    for groups in commaz.findall(text):
        matches.append(groups[0])
        print(groups)
except(IndexError):
    print("Your regex is wrong and didn't match anything.")
    sys.exit()

if(len(matches)>0):
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("Nothing was found.")
