def collatz(number):
    if (number % 2)==0:
        return (number // 2)
    else:
        return (3*number)+1

print("Wassup bro, pls enter an integer.")
try:
    number = int(input())
except ValueError:
    print("Bro, kindly enter an integer, and nothing else pls.")
while collatz(number)!=1:
    number=collatz(number)
    print(collatz(number))
