class House:
    def __init__(self, wall: str, door: str, window: str, floor: str, garden: bool, swimming_pool: bool):
        self.wall = wall
        self.door = door
        self.window = window
        self.floor = floor
        self.garden = garden
        self.swimming_pool = swimming_pool

    def display(self):
        print(f"Ściany: {self.wall}")
        print(f"Drzwii: {self.door}")
        print(f"Okna: {self.window}")
        print(f"Podłoga: {self.floor}")
        print(f"Ogród: {self.garden}")
        print(f"Basen: {self.swimming_pool}")
