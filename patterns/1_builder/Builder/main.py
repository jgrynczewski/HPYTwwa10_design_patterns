from my_house_builder import MyHouseBuilder
from cheap_house_builder import CheapHouseBuilder

print("Dom:")
builder = MyHouseBuilder()
builder.build_house()
house = builder.get_house()

house.display()

print("\nTani dom:")
builder = CheapHouseBuilder()
builder.build_house()
house = builder.get_house()
house.display()
