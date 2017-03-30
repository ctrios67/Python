#! /usr/bin/env python3

# pw.py - An insecure password locker program.

passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvAJHNUIWHnuivnaUHG8234msam',
             'luggage': '12345'}
import sys
import pyperclip

if(len(sys.argv) < 2):
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    print('Would you like to update the database with ' + account + '?(y/n)')
    confirm = str(input())
    if(confirm.lower()=='y'):
        print('Please enter ' + account + ' \'s password for storage.')
        newpass = str(input())
        passwords.setdefault(account, newpass)
        print(passwords) # I'm just verifying this updated correctly before termination
    else:
        sys.exit()
