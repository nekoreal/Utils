

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        from math import pi
        return pi * self._radius ** 2

c = Circle(3)
print(c.area)

"""
Позволяет обращаться к методу как к атрибуту.
Часто используется для вычисляемых свойств.
"""
