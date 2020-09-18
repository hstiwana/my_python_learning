#!/usr/bin/env python
# This program shows use of function that takes to parameters to compute the area
# of a triangle: formula is "area = .5 * base * height"
# Output looks like:
### The area of Triangle of base 3 and height 5 is 7.5 ###

#define a function to take input from user and validate it
def take_input():
    
    #lets handle user input and throw an error if invalid input is given
    try:
        take_input.base = int(input('Please input value for base: '))
    except ValueError as e:
        print(f'ERROR: Invalid input, try again\n\n\nError Details are given below:\n\n {e}')
        #Show error and line shown above and exit 
        quit()

    #lets handle user input and throw an error if invalid input is given
    try:
        take_input.height = int(input('Please input value for height: '))
    except ValueError as e:
        print(f'ERROR: Invalid input, try again\n\n\nError Details are given below:\n\n {e}')
        #Show error and line shown above and exit 
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
