#LSP

# łamie lsp

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Width {self.width}, heigth {self.height}"


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)


    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value


    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rectangle: Rectangle):
    w = rectangle.width
    rectangle.height = 10
    expected = 10*w
    print(f"Oczekiwane pole: {expected}, mamy {rectangle.area}")


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
