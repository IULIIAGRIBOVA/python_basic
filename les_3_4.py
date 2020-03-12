def my_func(x, y):
    result = 1
    for i in range(1, abs(y) + 1):
        result /= x
    return result


x = float(input("введите x: "))
y = int(input("введите y: "))
print(my_func(x, y))