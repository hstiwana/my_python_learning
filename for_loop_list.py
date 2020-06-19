# a simple for loop to calculate total from a list
# e.g. if we need to total expense over a couple of months 
expense=[1000,5000,2350,5500,3400,4500,2300,2500,3789,3421,2312,3300]
total=0
# for expX in expense:
#     total = total + expX
# print(total)
for exp2 in range(len(expense)):
    print(f'Month: {exp2+1}, Expense {expense[exp2]}')
    # print('Month:',exp2+1,'Expense',expense[exp2])
    total = total + expense[exp2]
print('Total Yearly Expense is:',total)