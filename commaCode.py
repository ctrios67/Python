def commaCode(someList):
    out = ""
    for index in range(len(someList)):
        if(someList[index]==someList[-1]):
            out += ("and " + someList[-1])
        else:
            out += (someList[index]+', ')
    return out

spam = ['apples', 'bananas', 'tofu', 'cats','a','b','c','d','e']
print(commaCode(spam))

# This program takes in a list as a param and outputs
# a comma separated list with the final element being "and list[last]"
