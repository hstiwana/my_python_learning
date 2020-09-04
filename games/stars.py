#!/usr/bin/env python
# Program printing starts as shown below
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 

#### this works
# s='*'
# print(s) # print first star
# for i in range(1,6): #lets make a list of 6 stars
#     k='* '
#     for j in range(i): #go one item at a time and add stars, it will start with 2 stars
#         k+='* '
#     print(k)

#### this works better :) 
# for i in range(1,6): 
#     s = ''
#     for j in range(i): 
#         s += '* '
#     print(s)

### see it look even better with less lines and few vars 
for i in range(1,7):
    for j in range(1,i+1):
        print("*", end=" ")
    print()#to give line break after each iteration 
