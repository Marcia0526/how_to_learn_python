class Shape:
    def __init__(self, r):
        self._r = r

    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('circle area is:', 3.14 * self._r * self._r)


class Square(Shape):
    def draw(self):
        print('Square area is:', self._r * self._r)


class Decorator(Shape):
    def __init__(self, obj: Shape):
        self._obj = obj

    def draw(self):
        self._obj.draw()


class ColorDecorator(Decorator):
    def draw(self):
        print('add color for the shape: ', self._obj.__class__.__name__)
        self._obj.draw()


class SizeDecorator(Decorator):
    def draw(self):
        print('modify size for the shape: ', self._obj.__class__.__name__)
        self._obj.draw()


circle = Circle(5)
color_decorator = ColorDecorator(circle)
size_decorator = SizeDecorator(color_decorator)
size_decorator.draw()

print()

square = Square(5)
color_decorator = ColorDecorator(square)
size_decorator = SizeDecorator(color_decorator)
size_decorator.draw()







