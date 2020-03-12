def devision(arg1, arg2):
    if arg2 == 0:
        return "делить на 0 можно, но не сейчас, введите другой делитель"
    else:
        return arg1 / arg2


user_number1 = int(input("введите делимое: "))
user_number2 = int(input("введите делитель: "))
print(devision(user_number1, user_number2))