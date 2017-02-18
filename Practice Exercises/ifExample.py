import sys
print("Please enter an integer.\n")
spam = int(input())
if spam == 1:
    print("Hello.\n")
elif spam == 2:
    print("Howdy\n")
else:
    print("Greetings.\n")
    sys.exit()
