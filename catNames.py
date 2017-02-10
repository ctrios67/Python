catNames = []
while True:
    print("What up bro, enter the name of cat # " + str(len(catNames)) + " (Or enter nothing to stop)")
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print("The cat names: ")
for name in catNames:
    print(' ' + name)
