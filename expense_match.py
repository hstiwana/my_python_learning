#program takes month number as argument and returns expense for that month, otherwise shows a nice message
month_list = ["January","February","March","April","May"]
expense_list=[2340,2500,2100,3100,2980]
print(f'Please input value from these numbers: {expense_list}')
expInput = int(input("Please enter expense value: "))
month = -1
for val in range(len(expense_list)):
    if expInput==expense_list[val]:
        month = val
        break
if month != -1:
    print (f'You spent {expense_list[val]} in the month of {month_list[month]}')
else:
        print(f'Couldn\'t find month for expense {expense_list[val]}')
