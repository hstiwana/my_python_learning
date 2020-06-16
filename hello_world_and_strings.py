#!/usr/local/opt/python/libexec/bin/python
# First comment
# shortcut to comment CMD + k + c
# shortcut to uncomment CMD + k + u
# print('hello world')
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('Hello, ' + first_name.capitalize() + ' ' + last_name.capitalize())
output = 'Hello, {} {}'.format(first_name,last_name)
print (output)
output = 'Hello, {1}, {0}'.format(first_name,last_name)
print (output)
output = f'Hello, {first_name} {last_name}'
print (output)
