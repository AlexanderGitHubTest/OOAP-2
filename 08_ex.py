'''
При использовании generic типов в новом формате для python 3.12+ явно 
тип ковариантный или контравариантный
не указывается. Type-checker проверяет это самостоятельно.
'''

from typing import override
from abc import ABC, abstractmethod


class Animal(ABC):
    
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


class AnimalCage[T: Animal]:
    '''
    Класс "Клетка с животным".
    При использовании данного класса
    ковариантная типизация, так как
    - атрибут класса считается приватным (по соглашению) 
    и в него ничего не записывается;
    - методы класса только возвращают объекты с типом
    Animal или его наследниками, но не используют их как 
    параметры.
    '''
    def __init__(self, animal: T) -> None:
        self._animal = animal
    
    def get_animal(self) -> T:
        return self._animal


class AnimalHandle[T: Animal]:
    '''
    Класс "Обработчик животных".
    При использовании данного класса
    контравариантная типизация, так как
    - переданное методу значение не сохраняется в классе
    (то есть это чистая функция)
    - методы класса используют объекты с типом
    Animal или его наследниками как параметры.
    '''
    
    def get_animal_name(self, animal: T) -> str:
        '''
        Метод возвращает название переданного класса
        '''
        return animal.__class__.__name__


def print_animal_sound(animal_cage: AnimalCage[Animal]) -> None:
    '''
    Выводит звук, издаваемый Animal, которое помещено 
    внутри контейнера AnimalCage
    '''
    animal = animal_cage.get_animal()
    animal.get_sound()


def print_dog_name(handler: AnimalHandle[Dog], dog: Dog) -> None:
    '''
    "Обработчик собак" - печатает имя класса собаки
    '''   
    print(f'Имя класса: {handler.get_animal_name(dog)}.')


def main() -> None:

    # КОВАРИАНТНОСТЬ
    dog_cage : AnimalCage[Dog] = AnimalCage(Dog())
    '''
    Ковариантность: функция, ожидающая параметр типа
    "Клетка с животным, внутри которой животное",
    получает переменную типа
    "Клетка с животным, внутри которой собака",
    при этом type-checker ошибок не пишет.
    '''
    print_animal_sound(dog_cage)


    # КОНТРАВАРИАНТНОСТЬ
    animal_handler: AnimalHandle[Animal] = AnimalHandle()
    '''
    Контравариантность: функция, ожидающая параметр типа
    "Обработчик животных, параметризированный типом собака",
    получает переменную типа
    "Обработчик животных, параметризированный типом животное",
    при этом type-checker ошибок не пишет.
    '''
    print_dog_name(animal_handler, Dog())


if __name__ == '__main__':
    main()
