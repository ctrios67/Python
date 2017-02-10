import sys

fatso = ['a','b','c','d']
print("Given a list as: [a,b,c,d]")
print("What is the result of int(int('3'*2) // 11)?")
try:
    spam = int(input())
except ValueError:
    print("Bro, that's not an integer. Assuming it is -1")
    spam = -1;
if(spam==0):
    print("Haha I thought so too, but really look at the inside parens.")
elif(spam==3):
    print("Correctomundo! 3 is a string, and *2 means repeat twice," \
              + " therefore, 33 instead of 6, integer division by 11.")
else:
    print("Nah you wrong bro. Try again if you want, by running the program again")
