user_seconds = int(input("введите число секунд: "))
houers = user_seconds//3600
minutes  =(user_seconds -  houers*3600)//60
seconds = user_seconds - houers*3600 - minutes*60
print(f'{houers:>02}:{minutes:>02}:{seconds:>02}')