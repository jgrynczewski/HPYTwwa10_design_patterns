# OCP
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for prod in products:
            if prod.color == color:
                yield prod

    def filter_by_size(self, products, size):
        for prod in products:
            if prod.size == size:
                yield prod

    def filter_by_size_and_color(self, products, size, color):
        for prod in products:
            if prod.size == size and prod.color == color:
                yield prod


### KOD KLIENCKI

apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
print("Green products:")
for prod in pf.filter_by_color(products, Color.GREEN):
    print(f"\t{prod.name} is green")

print("\nLarge products:")
for prod in pf.filter_by_size(products, Size.LARGE):
    print(f"\t{prod.name} is large")
