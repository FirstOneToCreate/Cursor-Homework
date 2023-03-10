# . Сreate a class hierarchy of animals with at least 5 animals that have additional methods each, create an instance
# for each of the animal and call the unique method for it. Determine if each of the animal is an instance of the
# Animals class class Animals: """ Parent class, should have eat, sleep """
#
# class Animal1(Animal):
# """
# Some of the animal with 1-2 extra methods related to this animal

# class Animal:
#     def __init__(self, kind, habitat):
#         self.kind = kind
#         self.habitat = habitat
#
#     def eat(self):
#         print(f"{self.kind} is eating!")
#
#     def sleep(self):
#         print(f"Shhhhh, {self.kind} is sleeping.")
#
# class Mammal(Animal):
#
#     def __init__(self, kind, habitat, ):


class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def bark(self):
        print(f"The {self.age} years old dog called {self.name} and is a {self.species} is barking at burglars.")


class Cat(Animal):
    def meow(self):
        print(f"The {self.age} years old cat called {self.name} and is a {self.species} is meowing.")


class Eagle(Animal):
    def fly(self):
        print(f"The {self.age} years old eagle called {self.name} and is a {self.species} is flying high in the sky.")


class Goldfish(Animal):
    def swim(self):
        print(f"The {self.age} years old goldfish called {self.name} and is a {self.species} is swimming in the pond.")


class Monkey(Animal):
    def jump(self):
        print(f"The {self.age} years old monkey called {self.name} and is a {self.species} is jumping in the jungle.")


dog = Dog("Lord", 9, "mammal")
dog.bark()

cat = Cat("Sphinx", 3, "mammal")
cat.meow()

eagle = Eagle("Creed", 6, "bird")
eagle.fly()

goldfish = Goldfish("Goldie", 3, "fish")
goldfish.swim()

monkey = Monkey("Julio", 5, "mammal")
monkey.jump()
