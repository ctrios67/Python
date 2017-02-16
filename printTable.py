#! /usr/bin/env python3
#! printTable.py
import copy
# The assumption is tableData will always have equal elements in their lists.
tableData = [['apples', 'oranges', 'cherries', 'banana', 'fasifaiso'],
             ['Alice', 'Bob', 'Carol', 'David', 'fhasfasf'],
             ['dogs', 'cats', 'moose', 'goose', 'sndsaiufba']]
def printTable(listz):
    length = len(listz)
    width = len(listz[0])
    biggest = 0
    colWidths = [0] * length
    for i in range(length):
        for j in range(width):
            temp = [0] * len(listz[i])
            temp[j] = len(listz[i][j]) # I originally had a for loop here
                                        # because of stupidity. Programming
                                        # while sick is not a good idea
            biggest = max(temp)
        colWidths[i] = biggest
    hello = ''
    for i in range(width):
        for j in range(length):
            if(listz[j][i]==listz[-1][i]):
                hello += ' ' + listz[j][i].rjust(colWidths[j])+'\n'
            else:
                hello += ' ' + listz[j][i].rjust(colWidths[j])
    print(hello)
printTable(tableData)
