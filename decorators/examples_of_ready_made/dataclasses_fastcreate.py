from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)

"""
Автоматически создает методы __init__, __repr__, __eq__ и др. для классов данных.
"""
