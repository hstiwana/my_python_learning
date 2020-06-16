#!/usr/local/opt/python/libexec/bin/python
first_name = input('Please entre first name: ')
last_name = input('Please enter last name: ')
age = input('Please enter your age: ')
output = f'Hello! {first_name} {last_name}'
output1=('Hello1' + ' ' + first_name +' '+ last_name)
output2=('Hello2, {0} {1}'.format(first_name,last_name).capitalize())
output3=('Hello3, {} {}'.format(first_name,last_name).upper())
print(output)
print(output1)
print(output2)
print(output3)
print(output3 + ' Your age in 1 year will be ' + str(int(age)+1))

if int(age) < 5:
    print('Hello baby')
else:
    print('Look at you!, you are grown up now')