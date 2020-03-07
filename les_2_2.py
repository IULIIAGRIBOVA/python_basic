user_str = input("введите элементы списка через пробел: ")
user_list = user_str.split()
list_len = len(user_list)
if list_len % 2 == 0:
    max_index = list_len-1
else:
    max_index = list_len-2

current_index = -2
while current_index<max_index-1:
    current_index += 2
    tmp = user_list[current_index]
    user_list[current_index] = user_list[current_index+1]
    user_list[current_index + 1] = tmp

print(user_list)
