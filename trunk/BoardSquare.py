__author__ = 'Binary Ninja'


class BoardSquare:
    empty_value = -1

    def __init__(self, x, y, value):
        assert isinstance(value, int)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.value = value
        self.x = x
        self.y = y

    def get_coordinates(self):
        return dict(x=self.x, y=self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x:" + str(self.x) + " y:" + str(self.y) + " value:" + str(self.value)