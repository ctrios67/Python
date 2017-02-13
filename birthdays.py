birthdays = {"Joffre": "Sept 8", "Joe":"Feb 4th", "Stephanie": "Feb 18",
             "Samantha": "Apr 6"}
while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have birthday information for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")

#   birthdays.values() prints the values of the keys.
#   birthdays.keys() prints the keys in the dictionary.
#   birthdays.items() prints the items in the dictionary.
