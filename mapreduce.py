# coding: utf8
import re
import sys

#Split the input into lines
def splitLines(mString):
    return mString.splitlines(False)

#Split a line into an array of word
def wordSplit(mString):
    # Regex we use to split a String in words, without ?! and stuff like that
    regex = ur"([^\W]+)"
    matches = re.finditer(regex, mString)
    wordList = []
    for matchNum, match in enumerate(matches):
        wordList.append(match.group())
    return wordList

#Sum an array of numbers
def sumNumbersArray(mNumbersArray):
    sum = 0
    for i in mNumbersArray:
        sum += i
    return sum

#Check if an argument is provided
if(len(sys.argv) < 2):
    print "usage: python main FILE\nWhere FILE will be the input of the word count"
    exit()

#Beginning of the program
#Open the file, and split it by lines
f = open(sys.argv[1], 'r+')
fileContent = f.read()
lines = splitLines(fileContent)

#MAP PHASE
#For each line, create a dictionary where the key is the word and the value is a list of 1.$
#Each 1 represents the presence of one word
mapList = []
for line in lines:
    words = wordSplit(line)
    map = dict()
    for word in words:
        if (word in map):
            map[word].append(1)
        else:
            map[word] = [1]
    mapList.append(map)

#SHUFFLE/SORT PHASE
#Do something

#REDUCE PHASE
#We create a new dictionary where the key is the word and the value is the number of occurrence of the word
finalDict = {}
for map in mapList:
    for key in map:
        if(key in finalDict):
            finalDict[key] = finalDict[key] + sumNumbersArray(map[key])
        else:
            finalDict[key] = sumNumbersArray(map[key])

#We print the result yay
for key in finalDict:
    print key + ': ' + str(finalDict[key])
