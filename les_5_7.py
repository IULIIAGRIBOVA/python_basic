import json

my_dict={}
aver = 0
num = 0
my_list=[]
with open("lesson_5_7.txt") as f_obj:
    for el in f_obj:
        num+=1
        temp_list = [x for x in el.split()]
        my_dict[temp_list[0]]= abs(int(temp_list[2])-int(temp_list[3]))
        aver+= int(temp_list[2]) - int(temp_list[3]) if int(temp_list[2])>int(temp_list[3]) else 0

my_list.append(my_dict)
my_list.append({"average_profit": aver/num})
print(my_list)

with open("my_file.json", "w") as write_f:
    json.dump(my_list, write_f)