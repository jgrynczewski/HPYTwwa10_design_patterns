# Dziedziczeniem, relacja typu IS-A (Cow is an Animal)
# Comopozycja, relacja type HAS-A (Cow has a milk)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.milk = Milk()

    def speak(self):
        print("Muuuuu")

    def feed(self):
        self.milk.increase()

    def give_milk(self):
        if self.milk.check():
            print("Proszę")
            self.milk.decrease()
        else:
            print("Nie mam mleka")

    def check_milk(self):
        print(f"Mam {self.milk.check()} mleka.")


class Dog(Animal):
    def speak(self):
        print("Hau hau")


class Corn:
    pass


class Milk:
    def __init__(self):
        self.amount = 0

    def increase(self):
        self.amount += 1

    def decrease(self):
        self.amount -= 1

    def check(self):
        return self.amount


c = Cow("Mućka")
c.feed()
c.check_milk()
c.give_milk()
c.check_milk()
c.give_milk()
