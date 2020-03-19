my_f = open("lesson5_3.txt", "r")
content = my_f.readlines()
print(content)
my_f.close()

my_list = []
my_sum = 0;
count = 0;
for el in content:
    count += 1
    temp_employe = el.split()
    if float(temp_employe[1]) < 20000:
        my_list.append(temp_employe[0])
    my_sum += float(temp_employe[1])

print("Получают менее 20000: ", my_list)
print("Средняя з/п: ", my_sum / count)