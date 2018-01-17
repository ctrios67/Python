################################################################################
## text_qualifier.py
## Written: 2017-12-01
## This script should encapsulate text found between a given delimiter
## and appropiately wrap it in double quotes to qualify as a "Text Qualifer".
################################################################################

import os

fileToList = []


# This file has 6 columns.
with open('VehicleService.txt', 'r') as uglyFile:
    data = uglyFile.readlines()
    print(data[0].split(';'))
    for i in range(len(data)):
        tempStr = data[i].split(';')
        for j in range(len(tempStr)):
            tempStr[j] = tempStr[j].replace('\n', '')
        fileToList.append(tempStr)

print('Level 1: ' + str(fileToList[0]))
print('Level 2: ' + str(fileToList[0][0]))
print('Level 3: ' + str(fileToList[0][0][0]))

for i in range(len(fileToList)):
    for j in range(len(fileToList[i])):
        fileToList[i][j] = '"' + fileToList[i][j] + '"'

# This is because I know EXACTLY how this file is, therefore this isn't generic.
for i in range(len(fileToList)):
    fileToList[i][5] = fileToList[i][5] + '\n'

print('Level 1: ' + str(fileToList[0]))
print('Level 2: ' + str(fileToList[0][0]))
print('Level 3: ' + str(fileToList[0][0][0]))

with open('20171203_Qualifier_VehicleService.txt', 'w') as fixedFile:
    for i in range(len(fileToList)):
        delimStr = ';'.join(fileToList[i])
        fixedFile.write(delimStr)

print('Done!')
