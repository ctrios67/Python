#! /usr/bin/env python3
# madLibs.py
import os
import sys

print('Please enter the path of your Mad Lib text file.')
print('Example: /Users/UserName/Documents/Python/ if on Mac OS X')
filePath = str(input())
pathExists = os.path.exists(filePath)
print('Please enter the file name.')
fileName = str(input())
fileExists = os.path.isfile(filePath+fileName)
if(pathExists and fileExists):
    os.chdir(filePath)
    madLib = open(fileName)
else:
    print('File does not exist. Exiting program...\n')
    sys.exit()

text = madLib.read()
print(text)
textList = []
adjective = []
noun = []
adverb = []
verb = []
# This grabs the parts of speech the user wants to substitute.
# But strings are immutable...
for partsOfSpeech in text.split():
    textList.append(partsOfSpeech)
    if(partsOfSpeech=='ADJECTIVE' or partsOfSpeech=='ADJECTIVE.' or partsOfSpeech=='ADJECTIVE.'):
        print('Enter an adjective:')
        adjective.append(str(input()))
    elif(partsOfSpeech=='NOUN' or partsOfSpeech=='NOUN.' or partsOfSpeech=='NOUN,'):
        print('Enter a noun:')
        noun.append(str(input()))
    elif(partsOfSpeech=='ADVERB' or partsOfSpeech=='ADVERB.' or partsOfSpeech=='ADVERB,'):
        print('Enter an adverb:')
        adverb.append(str(input()))
    elif(partsOfSpeech=='VERB' or partsOfSpeech=='VERB.' or partsOfSpeech=='VERB,'):
        print('Enter a verb:')
        verb.append(str(input()))
madLib.close()

adjCount = 0
nounCount = 0
adverbCount = 0
verbCount = 0
# I will eventually consider using a format specifier for this
newMadLib = open('madLibInsertions.txt', 'w')
# I really hate how I wrote this but it covers most general cases.
for a in range(len(textList)):
    if(textList[a]=='ADJECTIVE'):
        textList[a]=adjective[adjCount]
        adjCount=+1
    elif(textList[a]=='ADJECTIVE,'):
        textList[a]=adjective[adjCount]+','
        adjCount=+1
    elif(textList[a]=='ADJECTIVE.'):
        textList[a]=adjective[adjCount]+'.'
        adjCount=+1
    elif(textList[a]=='NOUN'):
        textList[a]=noun[nounCount]
        nounCount+=1
    elif(textList[a]=='NOUN,'):
        textList[a]=noun[nounCount]+','
        nounCount+=1
    elif(textList[a]=='NOUN.'):
        textList[a]=noun[nounCount]+'.'
        nounCount+=1
    elif(textList[a]=='ADVERB'):
        textList[a]=adverb[adverbCount]
        adverbCount+=1
    elif(textList[a]=='ADVERB,'):
        textList[a]=adverb[adverbCount]+','
        adverbCount+=1
    elif(textList[a]=='ADVERB.'):
        textList[a]=adverb[adverbCount]+'.'
        adverbCount+=1
    elif(textList[a]=='VERB'):
        textList[a]=verb[verbCount]
        verbCount+=1
    elif(textList[a]=='VERB,'):
        textList[a]=verb[verbCount]+','
        verbCount+=1
    elif(textList[a]=='VERB.'):
        textList[a]=verb[verbCount]+'.'
        verbCount+=1
    else:
        continue

# Create new string to write to the newly created file.
madLibText = ''
for a in range(len(textList)):
    if(a==0):
        madLibText+=textList[a]
    else:
        madLibText+=' '
        madLibText+=textList[a]
newMadLib.write(madLibText)
newMadLib.close()
print(madLibText)
print('MadLib created under the name "madLibInsertions.txt", exiting program.')
