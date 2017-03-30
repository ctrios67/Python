#! /usr/bin/env python3
#! strongPass.py
import re
import sys
'''
at least 8 chars
contains both uppercase and lowercase chars
contains at least one digit
'''
while True:
    countUp = 0
    countLow = 0
    countNum = 0
    print('Please enter your password. (Enter 1 to exit.)')
    password = str(input())
    if(password=='1'):
        sys.exit()
    if(len(password)<8):
        print('Password must be at least 8 characters. NOT valid.\n')
        continue
    else:
        for i in range(len(password)):
            if(password[i].isupper()==True):
                countUp += 1
            elif(password[i].islower()==True):
                countLow +=1
            elif(password[i].isnumeric()==True):
                countNum +=1
            else:
                print('Password either does not have a lowercase, uppercase, \
                      or digit')
        print(countUp)
        print(countLow)
        print(countNum)
        if((countUp>0) & (countLow>0) & (countNum>0)):
            print('Password is valid, great job.\n')
        else:
            print('Password is NOT valid, try again.\n')
            
                    
