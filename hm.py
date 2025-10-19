
salary = float(input("enter salary: "))

cash = 0
if salary > 1000:
    cash = 0.2

print("on hand:",salary * (1 - cash))
print("budget:",salary * cash)







