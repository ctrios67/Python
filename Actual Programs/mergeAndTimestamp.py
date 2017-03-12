#! /usr/bin/env python3
# mergeAndTimestamp.py

"""
The sequence goes:
Change directory to where files are located.
Open a new text file in write mode.
Have the name have the current timestamp down to the millisecond level.
Open the first file.
Save it's contents
Open the second file.
Save it's contents.
Open the third file.
Save it's contents.
Use the saved contents in a .write() for the original new file.
close everything.
"""

import os
import datetime
import glob2

def merger():
    os.chdir('/Users/Christian/Documents/Python/Sample-Files/')
    files = glob2.glob('file*.txt')
    now = datetime.datetime.now()
    newFile = open(now.strftime('%Y-%m-%d-%H-%M-%S-%f') +'.txt', 'w')
    #TODO: Parse file list and open them.
    for i in range(len(files)):
        with open(files[i]) as fileName:
            #TODO: Open new file in append mode.
            newFile.write(str(fileName.read()) + '\n')
    newFile.close()

merger()
