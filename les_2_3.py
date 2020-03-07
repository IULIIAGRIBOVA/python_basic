seasons_dict = {"1": "winter", "2": "winter", "12": "winter", "3": "spring", "4": "spring", "5": "spring", "6": "summer","7": "summer", "8": "summer", "9": "outumn", "10": "outumn", "11": "outumn"}
seasons_list = ["winter", "winter", "spring", "spring", "spring", "summer","summer","summer","outumn", "outumn", "outumn", "winter"]
user_month = input("введите месяц числом: ")
print(seasons_dict.get(user_month))
print(seasons_list[int(user_month)-1])
