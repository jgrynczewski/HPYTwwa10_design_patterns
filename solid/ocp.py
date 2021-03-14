# OCP
from enum import Enum

# łamiemy OCP

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

# Nie łamiemy OCP
import abc

class ISpecification(abc.ABC):

    @abc.abstractmethod
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class IFilter(abc.ABC):

    @abc.abstractmethod
    def fitler(self, items, specification):
        pass


class ColorSpecification(ISpecification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class BetterFilter:
    def filter(self, items, specification: ISpecification):
        for item in items:
            if specification.is_satisfied(item):
                yield item


class SizeSpecification(ISpecification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# Combinator
class AndSpecification(ISpecification):
    def __init__(self, spec1: ISpecification, spec2: ISpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)


##############
# KOD KLIENCKI
##############

bf = BetterFilter()

green = ColorSpecification(Color.GREEN)
print("\nGreen products (new_way):")
for prod in bf.filter(products, green):
    print(f"\t{prod.name} is green")

large = SizeSpecification(Size.LARGE)
print("\nLarge products (new_way):")
for prod in bf.filter(products, large):
    print(f"\t{prod.name} is large")

# large_blue = AndSpecification(
#     SizeSpecification(Size.LARGE),
#     ColorSpecification(Color.BLUE)
# )

blue = ColorSpecification(Color.BLUE)
large_blue = large and blue

print("\nLarge and blue products (new_way):")
for prod in bf.filter(products, large_blue):
    print(f"\t{prod.name} is large and blue")

