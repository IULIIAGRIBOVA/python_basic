user_num = int(input("введите целое положительное число: "))
max_figure = -1
while user_num > 0:
    figure = user_num % 10
    user_num = user_num // 10
    if (figure > max_figure):
        max_figure = figure
print(max_figure)
