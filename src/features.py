class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def intro(self):
        print(f"Hello, my name is {self.name} and I am a {self.species}.")

        dog = Pet("Buddy", "Dog")
        dog.color = "blue"

        dog.intro()


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def intro(self):
        print(f"This car is a {self.make} {self.model}.")

        my_car = Car("Toyota", "Corolla")
        my_car.year = 2020

        my_car.intro()


class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def intro(self):
        print(f"This hotel is {self.name} located in {self.location}.")

        my_hotel = Hotel("Grand Hotel", "Paris")
        my_hotel.stars = 5

        my_hotel.intro()
