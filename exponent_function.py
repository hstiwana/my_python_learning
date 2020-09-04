#!/usr/bin/env python
# its easy to do "2 ** 4" and get 16 but we are doing it with for loop
# 
# This is a function to show exponent
# it takes 2 arguments, base number and power number
# it will raise the base number to the power of pow number

def raise_to_power(base_num, pow_num):
    result = 1 #start multiplication with 1 (range starts from 0)
    for index in range(pow_num):
        result = result * base_num
    return result

#lets try to use the function to get results
print(raise_to_power(2,4))
