import time


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    start_time = 0

    def __init__(self):
        print("светофор создан")

    def running(self):
        i = 0
        while i != 20:
            print(TrafficLight.__color[i % 3])
            if i % 3 == 0:
                time.sleep(7)
            elif i % 3 == 1:
                time.sleep(2)
            elif i % 3 == 2:
                time.sleep(6)
            i += 1


t = TrafficLight()
t.running()

