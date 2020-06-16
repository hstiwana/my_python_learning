""" a simple for loop to print from 1 to 10, we use range to start loop from 1 explicitly
    start with 1, go up-to 11 and step by 1, if we step by 2, output will be just odd numbers
"""
for num in range(1,11,1):
    # check the remainder with %
    if num % 2 == 0:
        # if return value is 0, number is even
        print(f'Number {num} is even')
    else:
        # if return value is not 0 number is odd
        print(f'Number {num} is odd')