#! /usr/bin/env python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser
import sys
import pyperclip

def mapIt():
    #Gets address from the command line.
    if(len(sys.argv) > 1):
        address = ' '.join(sys.argv[1:])
    else:
        #TODO: Get address from the clipboard.
        address = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/' + address)

mapIt()

'''programs = ['mapit', 'socialmedia', 'weather']
print('Type the name of the program you want to use.')
for i in range(len(programs)):
    print(programs[i])
program = str(input()).lower()
if(program==programs[0]):
    mapIt()
elif(program==programs[1]):
    socialMedia()
elif(program==programs[2]):
    weather()
else:
    print('Program not listed, exiting...')
    sys.exit()
'''
