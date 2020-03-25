
class Road:
    _asf_weight = 25
    _height = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self):
        return self._length * self._width * self._asf_weight * self._height


my_road = Road(20, 5000)
print(my_road.massa())

