__author__ = 'Binary Ninja'
class BoardSquare:
    value = 0
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