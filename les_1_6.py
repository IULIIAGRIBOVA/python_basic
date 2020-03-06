revenue = int(input("введите значение выручки фирмы: "))
cost = int(input("введите значение издержек фирмы: "))
if (revenue>cost):
    print("прибыль составила: ", revenue-cost)
    print("рентабельность: ", (revenue-cost)/revenue )
    employee_count = int(input("введите число сотрудников фирмы: "))
    print("прибыль на одного сотрудника составила: ", (revenue-cost)/employee_count)
elif (revenue<cost):
        print("убыток — издержки больше выручки")
else:
    print("фирма работает в 0")