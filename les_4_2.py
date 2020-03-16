import random

my_list = [random.randint(0, 11) for el in range(0, 11)]
print(my_list)

result_list = [my_list[0]]

for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        result_list.append(my_list[i])

print(result_list)

