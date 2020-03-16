from itertools import cycle
с = 0
my_list = [1,2,3,4,7,34,2]
for el in cycle( my_list ):
    if с > 20:
        break
    print(el)
    с += 1