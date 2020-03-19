out_f = open("lesson5_1.txt", "w")
user_string="start"
while user_string != "":
   user_string = input("Введите строку: ")
   print(user_string , file = out_f)

out_f.close()