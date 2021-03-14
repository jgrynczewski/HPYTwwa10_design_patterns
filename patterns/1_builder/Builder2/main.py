from my_house_builder import MyHouseBuilder
from cheap_house_builder import CheapHouseBuilder
from director import Director

print("Mój dom:")
my_house_builder = MyHouseBuilder()
d = Director(my_house_builder)
d.build_house()
my_house = d.get_house()
my_house.display()

print("\nTani dom:")
cheap_house_builder = CheapHouseBuilder()
d = Director(cheap_house_builder)
d.build_house()
my_house = d.get_house()
my_house.display()
