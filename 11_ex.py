from abc import ABC, abstractmethod
from typing import final, override


class General:
    pass


class Any(General):
    pass


class Animal(Any, ABC):   
    @abstractmethod
    def get_sound(self) -> None:
        ...


class Dog(Animal):
    @override
    def get_sound(self) -> None:
        print('Dog woof!!!')


class Cat(Animal):
    @override
    def get_sound(self) -> None:
        print('Cat meow!!!')


@final
class NoneClass(Cat, Dog):
    def __getattribute__(self, name):
        raise TypeError("Запрещен вызов методов из NoneClass.")


# Инициализируем глобальный экземпляр NoneClass.
Void = NoneClass()


# I. Полиморфное использование Void.

def is_void(obj: Any) -> bool:
    return obj is Void

def use_animal(obj: Animal) -> None:
    if is_void(obj):
        print("Нет животного.")
        return
    obj.get_sound()

animals: list[Animal] = []
animals.append(Cat())
animals.append(Dog())
animals.append(Void)

for animal in animals:
    use_animal(animal)

# Цикл выведет:
# Cat meow!!!
# Dog woof!!!
# Нет животного


# II. Проверка NoneClass, как пустого и закрытого.

# Будет ошибка TypeError.
Void.get_sound()

# Но такой вызов никак запретить нельзя.
Dog.get_sound(Void)

# И такой вызов тоже запретить нельзя.
object.__getattribute__(Void, "get_sound")()

# Будет ошибка тайп-чекера.
class NewClass(NoneClass):
    pass
