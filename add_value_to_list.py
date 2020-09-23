#!/usr/bin/env python3
def add_and_before_end(var_list, var_to_add):
   #spam = ['apples', 'bananas', 'tofu', 'cats']
   var_list = input('Please input a list of values : ')
   var_to_add = input('Value to append before last item in string ? : ')
   if var_list:
         spam = var_list.split()
         print(f'\nOriginal list: {spam}\n')
         try:
            last_n = str(var_to_add) + ' ' + spam[-1]
         except ValueError:
            print('input error: try again')
            quit()
         spam.pop()
         spam.append(last_n)
         print(f"Final outcome: {', '.join(spam)}\n")
   else:
      print('input error: try again')
      quit()          
if __name__ == '__main__':
       var_list=[]
       var_to_add=""
       add_and_before_end(var_list,var_to_add)
# spam = ['apples', 'bananas', 'tofu', 'cats']
# print(f'{spam}')
# str1=', '.join(spam)
# str2=' '.join(str1.split(' ')[:-1]) + ' and ' + str1.split()[-1]
# str3=' '.join(str1.split(' ')[:-1]) + ' and ' + spam[-1]
# print(f'STR1 = {str1}')
# print(f'STR2 = {str2}')
# print(f'STR3 = {str3}')


# spam = ['apples', 'bananas', 'tofu', 'cats']
# str1=', '.join(spam)
# print(str1)
# print(type(str1))

# spam = ['apples', 'bananas', 'tofu', 'cats']
# print(', '.join(spam))
