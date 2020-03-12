def int_func(word):
    return word.capitalize()


user_strung = input("через пробел введите слова с маленькой буквы: ")
words_list = user_strung.split()
for word in words_list:
    print(int_func(word))
