# DIP

# łamiemy dip

from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Bonds:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")
person = Person("Tom")

# bonds = Bonds()
# bonds.add_parent_and_child(parent, child1)
# bonds.add_parent_and_child(parent, child2)
# bonds.add_parent_and_child(child1, person)


class Research:
    def __init__(self, bonds: Bonds):
        relations = bonds.relations
        for r in relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"John ma dziecko o imieniu {r[2].name}")

# Research(bonds)

# Nie łamiemy DIP'

import abc

class IBonds:
    @abc.abstractmethod
    def find_all_children(self, name):
        pass


class Bonds(IBonds):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children(self, name):
        for r in self.relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, bonds: IBonds):
        for child in bonds.find_all_children("John"):
            print(f"John ma dziecko o imieniu {child}")


bonds = Bonds()
bonds.add_parent_and_child(parent, child1)
bonds.add_parent_and_child(parent, child2)
bonds.add_parent_and_child(child1, person)

Research(bonds)
