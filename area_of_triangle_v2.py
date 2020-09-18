#!/usr/bin/env python
# This program shows use of function that takes to parameters to compute the area
# of a triangle: formula is "area = .5 * base * height"
# Output looks like:
### The area of Triangle of base 3 and height 5 is 7.5 ###

# Check if input value is float
def is_float(s):
    #set result to false if below given test fail
    result = False
    # Check if we have only 1 dot
    if s.count(".") == 1:
        # remove the dot and se if it is a digit
        if s.replace(".", "").isdigit():
            #retrun true to confirm string is a valid float
            result = True
    return result

#define a function to take input from user and validate it
def take_input():
    
    #lets handle user input and throw an error if invalid input is given
    b = input('Please input value for base: ')
    # check if "b" has a value
    if b:
        #check if it is a digit
        if b.isdigit():
            take_input.base = int(b)
        # use is_float function to check if input value is float
        elif is_float(b):
            take_input.base = float(b)
        else:
            print('Must enter a number. Bye!')
            quit()
    else:
        print('Must enter a number. Bye!')
        quit()


    # check if "h" has a value
    h = input('Please input value for height: ')
    if h:
        #check if it is a digit
        if h.isdigit():
            take_input.height = int(h)
        # use is_float function to check if input value is float
        elif is_float(h):
            take_input.height = float(h)
        else:
            print('Must enter a number. Bye!')
            quit()
    else:
        print('Must enter a number. Bye!')
        quit()

# define another function to calculate area of triangle
def area_of_triangle(base,height):
     # Calculate the area now
     area = .5 * base * height
     print(f'The area of triangle of base {base} and height {height} is {area}')

if __name__ == '__main__':
    #call function and validate input using function 
    take_input()
    #Use variables from take_input function as arguments in calculate function
    area_of_triangle(take_input.base,take_input.height)
