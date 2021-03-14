from ibuilder import IHouseBuilder


class MyHouseBuilder(IHouseBuilder):
    def build_house(self):
        self.new_house()
        self.build_wall()
        self.install_door()
        self.install_window()
        self.lay_floor()
        self.plant_garden()
        self.excavate_pool()

    def build_wall(self):
        self._house.wall = 'murowane'

    def install_door(self):
        self._house.door = 'antywłamaniowe'

    def install_window(self):
        self._house.window = 'kuloodporne'

    def lay_floor(self):
        self._house.floor = 'panele'

    def plant_garden(self):
        self._house.garden = True

    def excavate_pool(self):
        self._house.swimming_pool = True
