user_string = input("введите слова, разделеннвые пробелами: ")
user_list = user_string.split()
for idx, item in enumerate(user_list):
    print(idx, " ", item[:10])