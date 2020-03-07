my_list = [7, 5, 3, 3, 2]
user_number = int(input ("введите целое натуральное число: "))
position = 0
while user_number<=my_list[position] and position<len(my_list)-1:
    position +=1

if my_list[position] >= user_number :
    position += 1

my_list.insert(position, user_number)
print(my_list)