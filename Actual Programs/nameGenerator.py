#! /usr/bin/env python3
# nameGenerator.py

import random
import string

def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3
    return name

print(generator())
