#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
else:
    last_digit = ((number * -1) % 10) * -1
less_than = 'and is less than 6 and not 0'
greater_than = 'and is greater than 5'
if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} " +
          f"{greater_than}")
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} " +
          f"and is 0")
else:
    if number > 0:
        print(f"Last digit of {number:d} is {last_digit} " +
              f"{less_than}")
    else:
        print(f"Last digit of {number:d} is {last_digit:d} " +
              f"{less_than}")
