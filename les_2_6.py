my_list = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]

result_list_name = [];
result_list_price = [];
result_list_count = [];
result_list_unit = [];

result_dict = {}
for item in my_list:
    print(item[1]["название"])
    result_list_name.append(item[1]["название"])
    result_list_price.append(item[1]["цена"])
    result_list_count.append(item[1]["количество"])
    result_list_unit.append(item[1]["eд"])


result_dict.update({"название": list(set(result_list_name))})
result_dict.update({"цена": list(set(result_list_price))})
result_dict.update({"количество": list(set(result_list_count))})
result_dict.update({"количество": list(set(result_list_unit))})
print(result_dict)