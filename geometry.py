def draw(object):
    for pixel in range(object.length):
        if object.width > 0:
            print('* ' * object.width)
        else:
            print('* ' * object.length)


class Rectangle:
    def __init__(self, width=0, length=0):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def __add__(self, rectangle):
        if isinstance(rectangle, Rectangle):
            return Rectangle(self.width + rectangle.width, self.length + rectangle.length)

    def __iter__(self):
        yield Rectangle()


class Square(Rectangle):
    def __init__(self, length=0):
        self.length = length
        super(Square, self).__init__(length, length)

    def __iter__(self):
        yield Square()


class Cube(Square):
    def volume(self):
        return self.length ** 3

    def __iter__(self):
        yield Cube()
