from __future__ import annotations

from abc import ABC, abstractmethod
from typing import final, Final, override, Protocol, Self


class SupportsAdd(Protocol):
    '''
    Протокол - ограничивает данные только типами,
    которые поддерживают операцию сложения
    '''
    def __add__(self, other: Self) -> Self:
        pass


@final
class NoneClass:
    '''
    Конечный класс для всех "классов-листьев"
    Не имеет пользовательских методов и не разрешено наследование.
    '''
    __slots__ = ()

    def __init_subclass__(cls, **kwargs):
        raise TypeError("Наследование от NoneClass запрещено")


Void: Final[NoneClass] = NoneClass()


class General[T]:
    '''
    Базовый класс, от него наследуется класс Any.
    Запрещено создавать экземпляры General.
    '''

    def __new__(cls, *args, **kwargs):
        if cls is General:
            raise TypeError(
                f"Запрещено создавать экземпляры класса General!"
            )
        return super().__new__(cls)

    '''
    ... наполнение класса General убрал для экономии места ...
    '''


class Any[T](General[T]):
    '''
    Наcледник General, от которого должны создаваться объекты.
    '''
    pass


class Operations[T](Any[T], ABC):
    '''
    Абстрактный класс, в котором находятся общие операции
    '''
    # перекрою стандартный "магический" метод сложения
    @abstractmethod
    def __add__(self: T, other: T) -> T | NoneClass:
        pass


class Vector[T: SupportsAdd](Operations["Vector[T]"]):
    """
    Линейный массив значений типа T, наследуемого от General, над которым допустима операция сложения, 
    реализуемая как сложение соответствующих значений типа T двух векторов одинаковой длины.
    """

    def __init__(self) -> None:
        self._array: list[T] = []

    def __len__(self) -> int:
        return len(self._array)

    def __getitem__(self, i: int) -> T:
        if i < 0 or i >= len(self._array):
            raise IndexError('Index is out of bounds')
        return self._array[i]

    def append(self, item: T) -> None:
        self._array.append(item)

    @override
    def __add__(self, other: Vector[T]) -> Vector[T] | NoneClass:
        if len(self._array) != len(other):
            return Void
        vector_result: Vector[T] = Vector()
        for left, right in zip(self._array, other._array):
            vector_result.append(left + right)
        return vector_result


def main():
    '''
    Сложение объектов типа Vector<Vector<Vector<T>>>массив массивов массивов
    Сложим
    Vector1 : [[[3, 6]], [[9, 11]]]
    и
    Vector2 : [[[5, 7]], [[1, 8]]]
    
    Получим результат : [[[8, 13]], [[10, 19]]]
    '''
    
    array1_internal1 = Vector()
    array1_internal2 = Vector()
    array1_middle1 = Vector()
    array1_middle2 = Vector()
    array1_external = Vector()
    array2_internal1 = Vector()
    array2_internal2 = Vector()
    array2_middle1 = Vector()
    array2_middle2 = Vector()
    array2_external = Vector()

    array1_internal1.append(3)
    array1_internal1.append(6)
    array1_middle1.append(array1_internal1)
    array1_internal2.append(9)
    array1_internal2.append(11)
    array1_middle2.append(array1_internal2)
    array1_external.append(array1_middle1)
    array1_external.append(array1_middle2)
    array2_internal1.append(5)
    array2_internal1.append(7)
    array2_middle1.append(array2_internal1)
    array2_internal2.append(1)
    array2_internal2.append(8)
    array2_middle2.append(array2_internal2)
    array2_external.append(array2_middle1)
    array2_external.append(array2_middle2)

    array_result = array1_external + array2_external
    print(len(array_result)) # 2
    print(array_result[0][0][0]) # 8
    print(array_result[0][0][1]) # 13
    print(array_result[1][0][0]) # 10
    print(array_result[1][0][1]) # 19


if __name__ == "__main__":
    main()
