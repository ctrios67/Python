#! /usr/bin/env python3
#! strongPassRegex.py
import re
import sys
'''
at least 8 chars
contains both uppercase and lowercase chars
contains at least one digit

The below cases should break these rules.
'''
shortPass = '123Az'
allLower = '123abcefghijkl'
allUpper = '123ABCDEFGHIJKL'
noDigit = 'ABCDEFGhijklmnop'

#The following should be a correct password.
correctPass = '1234567Az'

while True:
    length = re.compile(r'[a-zA-Z0-9]{8,}')
    upper = re.compile(r'[A-Z]?')
    lower = re.compile(r'[a-z]?')
    digits = re.compile(r'[0-9]+')
    correct = 0
    print('Please enter a Password or enter 1 to exit.')
    password = str(input())
    if(password=='1'):
        sys.exit()
    else:
        if(length.findall(password)!=[]):
            correct += 1
        if(upper.findall(password)!=[]):
            correct += 1
        if(lower.findall(password)!=[]):
            correct += 1
        if(digits.findall(password)!=[]):
            correct += 1
    if(correct==4):
        print('Password is VALID, congrats.\n')
    else:
        print('Password is NOT valid. Please enter a valid password.')
        print('Password must be greater than 8 characters.')
        print('Password must have at least 1 upper case letter.')
        print('Password must have at least 1 lower case letter.')
        print('Password must have at least 1 digit.')
