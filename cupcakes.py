from abc import ABC, abstractmethod
import csv

def get_cupcakes(file):
    with open (file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dict(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def delete_cupcake(file, cupcake):
    lines = list()
    with open(file, "r", newline="\n") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lines.append(row)
        for name in lines:
            if name["name"] == cupcake:
                lines.remove(name)
    with open(file, "w", newline="\n") as cvsfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(cvsfile, fieldnames=fieldnames)
        writer.writeheader()
        for line in lines:
            writer.writerow(line)


def read_csv(file):
    with open (file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)


def write_csv(file, cupcakes):
    with open(file, "w", newline = "\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                 writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        if hasattr(cupcake, "filling"):
                 writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


class Cupcake(ABC):
    size = 'regular'
    def __init__ (self,name,price,flavor,frosting,filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        self.filling = filling

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price


class Mini(Cupcake):
    size = 'mini'
    def __init__(self, name, price, flavor, frosting, filling):
        super().__init__(name, price, flavor, frosting, filling=None)

    def calculate_price(self, quantity):
        return quantity * self.price


class Large(Cupcake):
    size = 'large'
    def __init__(self,name,price,flavor,frosting,filling):
        super().__init__(name,price,flavor,frosting,filling)

    def calculate_price(self, quantity):
        return quantity * self.price

class Regular(Cupcake):
    size = 'regular'
    def __init__(self,name,price,flavor,frosting,filling):
        super().__init__(name,price,flavor,frosting,filling)

    def calculate_price(self, quantity):
        return quantity * self.price

cupcake1 = Mini("Chocolate", 1.99, "Chocolate", "White", None)
cupcake1.add_sprinkles("Chocolate", "Oreo")

cupcake2 = Large("White Chocolate", 3.99, "White Chocolate", "Vanilla", "Vanilla")
cupcake2.add_sprinkles("White Chocolate", "Nuts")

cupcake3 = Regular("Strawberry", 2.99, "Strawberry", "Vanilla", "Strawberry Jam")

cupcake4 = Regular("Cookies and Cream", 2.99, "Cookies and Cream", "Chocolate", "Chocolate")
cupcake4.add_sprinkles("Cookie crumbles")

cupcake5 = Large("Black Cocoa", 3.99, "Dark Chocolate", "Chocolate", "Dark chocolate")
cupcake5.add_sprinkles("Cocoa")

cupcake6 = Mini("Vanilla", 1.99, "Vanilla", "Vanilla", None)
cupcake6.add_sprinkles("Pink hearts")

cupcake_list = [cupcake1, cupcake2, cupcake3, cupcake4, cupcake5, cupcake6]

# write_csv("order.csv", cupcake_list)
