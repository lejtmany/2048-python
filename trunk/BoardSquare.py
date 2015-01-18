__author__ = 'Miriam'

class BoardSquare:

    value = 0

    def __init__(self, value):
        """
        instantiates a board square
        :type value: int
        """
        assert isinstance(value, int)
        self.value = value


a = BoardSquare(9)
print(a.value)