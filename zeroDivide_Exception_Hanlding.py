#!/usr/bin/env python
# This is a small program showing Exception handling
# instead of throwing error, we are using "try" "except" to handle ZeroDivisionError

# create spam function that takes 1 argument
def spam(divideBy):
    try: #try to divide number 42 by divideBy value
        return 42 / divideBy
    except ZeroDivisionError: #if you hit ZeroDivisionError, print line shown below
        print('Error: Invalid argument.')

# call the function
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
