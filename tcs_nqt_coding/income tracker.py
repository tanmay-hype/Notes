income = int(input("Enter your income: "))

total_expense = 0
expense = {}

while True:
    material = input()

    if material == "done":
        break 

    amount = int(input())

    expense[material] = amount
    total_expense += amount

savings = income - total_expense

print("Total income", income)

if savings > income:
   print("Total savings", savings)

elif savings < income:
    print("total saving is 0")

for material in expense:
    print(material + ":", expense[material])