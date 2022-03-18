expenses = []
total = 0
num_expenses = int(input("Enter # of expenses:"))
#sum = 0

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))
#for x in expenses:
#    sum = sum + x

total = sum(expenses)
#print("You spent $", sum, " on lunch this week.", sep='')
#print("You spent $", total, " on lunch this week.", sep='')
print("You spent $", total, sep='')