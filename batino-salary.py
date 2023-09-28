yearsOfService = int(input("Enter years of service: "))
salary = float(input("Enter salary: "))
n = 0
if 5 <= yearsOfService < 10:
    n = 1
    bonus_amount = salary * 0.05

elif 10 <= yearsOfService < 15:
    n = 2
    bonus_amount = salary * 1.0

elif 15 <= yearsOfService < 20:
    n = 3
    bonus_amount = salary * 1.5

elif 20 <= yearsOfService:
    n = 4
    bonus_amount = salary * 2.0

else:
    n = 0
    bonus_amount = salary * 0

print(f"Your salary is {salary + bonus_amount}")
print(f"The running time is: {n}(n)")
