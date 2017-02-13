#! /usr/bin/env python3
#! printTable.py

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
longest = []
for i in range(len(tableData)):
    for j in range(len(tableData[i])):
        longest.append(len(tableData[i][j]))

big = max(longest)
print(longest)
