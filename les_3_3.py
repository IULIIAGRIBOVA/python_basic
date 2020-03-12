def my_func(number1, number2, number3):
    my_list = [number1, number2, number3]
    my_list = sorted(my_list, reverse=True)
    return my_list[0] + my_list[1]


print(my_func(1, 2, 60))