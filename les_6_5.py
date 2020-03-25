

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print(f"{self.title}: Рисуем тонкую линию")


class Pencil(Stationery):

    def draw(self):
        print(f"{self.title}: Рисуем линию, которую можно стереть")


class Handle(Stationery):

    def draw(self):
        print(f"{self.title}: Рисуем самую красивую линию в мире")


my_Pen = Pen("Зеленая ручка")
my_Pen.draw()

my_Pencil = Pencil("Синий карандаш")
my_Pencil.draw()

my_Handle = Handle("Разноцветная ручка")
my_Handle.draw()
