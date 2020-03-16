from itertools import count
user_number = int(input("Введите число, с которого будет начинаться список: "))
for el in count(user_number ):
    print(el)
    if el > 20:
        break