from abc import ABC, abstractmethod
class Clothes(ABC):

    def __init__(self, var):
        self.var = var

    @property
    def consumption(self):
        return 0

    @abstractmethod
    def get_var(self):
        return 0


class Coat(Clothes):

    @property
    def consumption(self):
        return f'Для пошива пальто нужно: {self.var / 6.5 + 0.5 :.2f} ткани'

    def get_var(self):
        return  f"размер = {self.var}"


class Suit(Clothes):

    @property
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.var + 0.3 :.2f} ткани'

    def get_var(self):
        return f"рост = {self.var}"


coat = Coat(64)
suit = Suit(170)
print(coat.consumption)
print(suit.consumption)
print(coat.get_var())
print(suit.get_var())