from ibuilder import IHouseBuilder


class Director:
    def __init__(self, builder: IHouseBuilder):
        self._builder = builder

    def build_house(self):
        self._builder.new_house()
        self._builder.build_wall()
        self._builder.install_door()
        self._builder.install_window()
        self._builder.lay_floor()
        self._builder.plant_garden()
        self._builder.excavate_pool()

    def get_house(self):
        return self._builder.get_house()
