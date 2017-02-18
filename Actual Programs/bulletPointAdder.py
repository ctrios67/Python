#! /usr/bin/env python3
# bulletPointAdder.py - Adds Wikipedia style bullet points to the start of
# each line of text on the clipboard.
import pyperclip
import sys

text = pyperclip.paste()

# TODO: Separate lines and add stars.

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop through all the indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)    
pyperclip.copy(text)
