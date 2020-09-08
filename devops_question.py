#!/usr/bin/env python
# This code is to practice if / else
import sys
language = [ 'python', 'go', 'java' ]
user_resp = [ 'yes', 'no']
tech = [ 'yes']
print( "Lets see if you are eligible for Dev Ops role: ")
try:
    skill1 = input(f'What coding language you know, Options {language}: ').lower()
    while True: # loop to wait for right input from user
        if skill1 not in language:
            skill1 = input(f'What coding language you know, Options {language}: ').lower()
        else:
            break # lets get out of this loop if user input is one of the language
    skill2 = input('Do you know K8s? (yes/no): ').lower()
    while True: # loop to wait for correct input
        if skill2 not in user_resp:
            skill2 = input('Do you know K8s? (yes/no): ').lower()
        else:
            break # lets get out of this loop if user input is one of the user_resp
    skill3 = input('Do you know Azure? (yes/no): ').lower()
    while True: # loop to wait for correct input
        if skill3 not in user_resp:
            skill3 = input('Do you know Azure? (yes/no): ').lower()
        else:
            break # lets get out of this loop if user input is one of the user_resp
    skill4 = input('Number of years you have worked in cloud? : ')
    while True: # loop to wait for correct input
        if skill4.isdigit() == False:
            print('Invalid input: Please enter numbers only!')
            skill4 = input('Number of years you have worked in cloud? : ')
        else:
            break

    if skill1 in language and (skill2 == 'yes' and skill3 == 'yes') and int(skill4) >= 5:
        print('Congrats you have right skill set for this Role!!')
    elif int(skill4) < 5:
        print(f'Sorry, you are lacking expertise in clouds, your experience is "{skill4}" years but minimum requirement is 5')
    elif skill2 == 'no' or skill3 == 'no':
        print('Sorry, you are lacking expertise in some of the required skills e.g. Azure or K8s')
except KeyboardInterrupt:
    print('\n\nExiting out on keyboard interrupt')
    sys.exit()
