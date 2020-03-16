from sys import argv

script_name, rate, hours, bonus = argv
print("Зарплата составила: ", int(rate)*int(hours)+int(bonus))