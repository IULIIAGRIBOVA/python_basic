def my_func(my_list):
    my_sum = 0
    have_stop_word = False
    for item in my_list:
        if item == "stop":
            have_stop_word = True
        if item.isdigit():
            my_sum += int(item)

    return have_stop_word, my_sum


my_sum1 = 0
while True:
    user_string = input("введите числа через пробел: ")
    my_list = user_string.split()
    have_stop_word, list_sum = my_func(my_list)
    my_sum1 += list_sum
    print(my_sum1)
    if have_stop_word:
        break