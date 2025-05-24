from abc import ABC, abstractmethod

# Abstract Factory
class Factory(ABC):
    @abstractmethod
    def create_product(self, kind=None):
        pass

# Concrete Factories
class DogFactory(Factory):
    def create_product(self, kind=None):
        return Dog()

class CatFactory(Factory):
    def create_product(self, kind=None):
        return Cat()

# Abstract Product
class Animals(ABC):
    @abstractmethod
    def run(self):
        pass

# Concrete Products
class Dog(Animals):
    def run(self):
        print("I'm a Dog, I can run!!")

class Cat(Animals):
    def run(self):
        print("I'm a Cat, I can run!!")

# ---- Client Code ----
factory = DogFactory()
dog = factory.create_product()
dog.run()

factory = CatFactory()
cat = factory.create_product()
cat.run()
