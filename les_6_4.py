

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car is going")

    def stop(self):
        print("Car stopped")

    def turn(self, direction):
        print("Car turned " + direction)

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return "Скорость превышена!"
        else:
            return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return "High speed!"
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


my_PoliceCar = PoliceCar(60, "red", "mazda")
my_PoliceCar.go()
my_PoliceCar.turn("left")
my_PoliceCar.stop()
print(my_PoliceCar.show_speed())
print(my_PoliceCar.is_police)

my_TownCar = TownCar(80, "red", "mazda")
my_TownCar.go()
my_TownCar.turn("right")
my_TownCar.stop()
print(my_TownCar.show_speed())
print(my_TownCar.is_police)

