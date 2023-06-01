#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    modulus = number % (-10)
else:
    modulus = number % 10

if modulus > 5:
    print(f"Last digit of {number} is {mudulus} and is greater than 5")
elif modulus == 0:
    print(f"Last digit of {number} is {modulus} and is 0")
else:
    print(f"Last digit of {number} is {modulus} and is less than 6 and not 0")
