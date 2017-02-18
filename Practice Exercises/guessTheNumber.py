import random
secretNumber = random.randint(1, 20)
print("I am thinking of a number 1 and 20.")

for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is TOO DAMN HIGH.")
    else:
        break

if guess==secretNumber:
    print("Con-GRAT-ULATIONS! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
