from abc import ABC, abstractmethod
from typing import override, TypeVar


class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        ...

class Dog(Animal):
    @override
    def speak(self) -> str:
        return "Гав!"

class Cat(Animal):
    @override
    def speak(self) -> str:
        return "Мяу!"


animals: list[Animal] = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())  # Полиморфный вызов метода
                           # Гав!
                           # Мяу!
                           # Гав!

T_Animal = TypeVar("T_Animal", bound=Animal)

class AnimalFactory[T_Animal](ABC):
    @abstractmethod
    def create(self) -> Animal:
        ...

class DogFactory(AnimalFactory):
    def create(self) -> Dog:
        return Dog()

animal_factory: AnimalFactory = DogFactory()

factory_result = animal_factory.create()  # Ковариантный вызов метода
