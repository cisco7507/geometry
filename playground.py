from geometry import Rectangle, Square, Cube
from random import randint, choice


def return_shape():
    return choice([Rectangle(), Square(), Cube()])


num_shapes = 10

shapes = [return_shape() for shape in range(num_shapes)]
for shape in shapes:
    # print(shape)
    if shape.__class__ is Rectangle:
        shape.width = randint(7, 12)
        shape.length = randint(7, 12)
    elif shape.__class__ is Square:
        shape.length = randint(7, 12)
    elif shape.__class__ is Cube:
        randint(7, 12)
        shape.length = randint(7,12)
    else:
        print('Unknown class')
        exit(1)

for shape in shapes:
    print(shape)
    continue
    exit(0)
    if type(shape) is Rectangle:
        print(f' This is a rectangle,  Width {shape.width} Length: {shape.length}, area is: {shape.area()}')
        draw(shape)
        print('')
    elif type(shape) is Square:
        print(f'This is a square, length: {shape.length}')
        draw(shape)
        print('')
    else:
        print(f'This is a cube of side: {shape.length} and volume: {shape.volume()}')


