class Person:
    def __init__(self, name, age, money, has_home):
        self.name = name
        self.age = age
        self.money = money
        self.has_home = has_home

    def provide_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nMoney: {self.money}\nHas Home: {self.has_home}")

    def make_money(self, amount):
        self.money += amount

    def buy_home(self, area, cost):
        if self.money >= cost:
            self.money -= cost
            self.has_home = True
            print(f"{self.name} bought a {area} sq. m. home for {cost}.")

        else:
            print(f"{self.name} does not have enough money to buy a home.")


class Home:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def apply_discount(self, discount):
        self.cost -= (self.cost * discount / 100)


class Realtor:
    _instance = None

    def __new__(cls, name, houses, discount):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name, houses, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide_info(self):
        for house in self.houses:
            print(f"Area: {house.area} sq. m.\nCost: {house.cost}\n")

    def give_discount(self, house):
        house.apply_discount(self.discount)
        print(f"{self.name} gave a {self.discount}% discount on a {house.area} sq. m. home worth {house.cost}.")

    def steal_money(self):
        import random
        chance = random.randint(1, 10)
        if chance == 1:
            print(f"{self.name} stole your money!")
            return True
        else:
            return False


# Creating objects
p1 = Person("Vova", 21, 10000, False)
h1 = Home(40, 50000)
r1 = Realtor("Mike", [h1], 10)

# Using objects
p1.provide_info()
p1.make_money(100000)
p1.buy_home(h1.area, h1.cost)
p1.provide_info()

r1.provide_info()
r1.give_discount(h1)
r1.steal_money()
