def num(m_list):
    sum = 0
    for el in m_list:
        if el.isdigit():
            sum+=int(el)
    return sum


my_dict={}
with open("lesson_5_6.txt") as f_obj:
    for el in f_obj:
       temp_list = [(((x.replace(":", "")).replace("(l)", "")) .replace("(pr)", "")).replace("(lab)", "") for x in el.split()]
       my_dict[temp_list[0]]=num(temp_list)

print(my_dict)