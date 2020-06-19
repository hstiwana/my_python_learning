# Program printing starts as shown below
# *
# **
# ***
# ****
# *****
# ******
#### this also works
# s='*'
# print(s) # print first star
# for i in range(1,6): #lets make a list of 6 stars
#     k='*'
#     for j in range(i): #go one item at a time and add stars, it will start with 2 stars
#         k+='*'
#     print(k)
#### this works better :) 
for i in range(1,6): 
    s = ''
    for j in range(i): 
        s += '*'
    print(s)