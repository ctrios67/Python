#! /usr/env/bin python3
#! typeCorrecter.py
import re
import pyperclip

'''
Find   common   typos   such   as   multiple   spaces  between  words,
accidentally accidentally repeated repeated words words,
or multiple exclamation marks at the end of sentences!!!
Those are annoying!!!
'''

typoRE = re.compile(r'''(
    ([a-zA-Z0-9._/-]*)  # RE for a random word in text.
    ((\s | ! | .)+)
    )''', re.VERBOSE)

#TODO: Substitute typo for correct shiz.
multispace = re.compile('(\s+)') # Good
repeats = re.compile(r'\b(\w+)\s+\1\b') # Good, but had to research
exclaim = re.compile(r'(!)+') # Good

text = str(pyperclip.paste())
original = text
text = multispace.sub(r' ', text)
text = repeats.sub(r'\1', text)
text = exclaim.sub(r'!', text)

matches = []
for groups in typoRE.findall(text):
    matches.append(groups[0])
    print(groups)

if(len(matches)>0):
    pyperclip.copy('\n'.join(matches))
    print('After fixes, the following was copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No typos found. Exiting...')
