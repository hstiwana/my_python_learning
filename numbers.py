#!/usr/local/opt/python/libexec/bin/python
first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num / second_num)
print(first_num - second_num)
print(first_num * second_num)
print(first_num ** second_num)

days_in_feb = 28
# Next line is expected to fail because of INT to STR addition is not possible
# print(days_in_feb + ' Days in Feb')
# Convert to STR and use it like this 
print(str(days_in_feb) + ' Days in Feb')

first_num = input('please enter first number: ')
second_num = input('please enter second number: ')
print (first_num + second_num)
print (int(first_num)+int(second_num))
print (float(first_num)+float(second_num))
