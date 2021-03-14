from ibuilder import IHouseBuilder


class CheapHouseBuilder(IHouseBuilder):
    def build_wall(self):
        self._house.wall = 'drewniane'

    def install_door(self):
        self._house.door = 'standardowe'

    def install_window(self):
        self._house.window = 'pcv'

    def lay_floor(self):
        self._house.floor = 'parkiet'

    def plant_garden(self):
        self._house.garden = True

    def excavate_pool(self):
        self._house.swimming_pool = False
