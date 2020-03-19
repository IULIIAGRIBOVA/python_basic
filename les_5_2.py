my_f = open( "lesson5_2.txt" , "r" )
content = my_f.readlines()
print(content)
my_f.close()

string_count = 0

for el in content:
    string_count += 1
    num = len(el.split())
    print(f"Строка содержит {num} слов")

print(f"Количество строк в файле: {string_count}")