import random
my_list = [random.randint(0, 5) for el in range(0, 10)]
print(my_list )
result_list = [el for el in my_list if my_list.count(el)==1]
print(result_list)