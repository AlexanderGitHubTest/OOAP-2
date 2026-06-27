from abc import ABC, abstractmethod
import statistics
from typing import cast, final, override


@final
class NoneClass:
    pass


Void = NoneClass()


type Numeric = int | float


class _MathUtilites:
    '''
    Класс Математические утилиты для демонстрации 
    льготного наследования (facility inheritance).
    Класс содержит функции для подсчёта:
    - суммы,
    - среднего арифметического,
    - среднеквадратического отклонения
    '''

    @staticmethod
    def _sum(array: list[Numeric]):
        '''
        Сумма.
        '''
        return sum(array)

    @staticmethod
    def _mean(array: list[Numeric]):
        '''
        Среднее арифметическое.
        '''
        return statistics.mean(array)

    @staticmethod
    def _stdev(array: list[Numeric]):
        '''
        Среднеквадратичное отклонение.
        '''
        return statistics.stdev(array)


class Array(_MathUtilites):
    '''
    Класс "Массив", реализованный.
    Наследование от класса _MathUtilites - это
    льготное наследование (facility inheritance)
    '''

    def __init__(self, capacity: int) -> None:
        '''
        Конструктор получает размер массива
        (постусловие - создан не заполненный массив заданного размера).
        '''
        self._array: list[Numeric|NoneClass] = [Void] * capacity
        self._capacity: int = capacity

    def capacity(self) -> int:
        '''
        Запрос возвращает размер массива
        (предусловий и постусловий нет).
        '''
        return self._capacity

    def stat_info(self) -> dict[str, Numeric]:
        '''
        Запрос возвращает статистические сведения
        о массиве (сумму, среднее арифметическое и среднеквадратичное отклонение)
        (предусловий и постусловий нет).
        '''
        filtered: list[Numeric] = [cast(Numeric, n) for n in self._array if n is not Void]
        return {
            "sum": self._sum(filtered),
            "mean": self._mean(filtered),
            "stdev": self._stdev(filtered)
            }
   
    def get_item(self, i: int) -> Numeric | NoneClass:
        '''
        Запрос возвращает элемент из ячейки с индексом i:
        1-я ячейка имеет индекс 0
        (предусловие - индекс в границах массива).
        '''
        if i < 0 or i >= self._capacity:
            raise IndexError("Переданный индекс за границами массива!")
        return self._array[i]

    def put_item(self, i: int, item: Numeric) -> None:
        '''
        Команда записывает элемент в ячейку с индексом i
        (предусловие - индекс в границах массива)
        (постусловие - элемент сохранен в ячейку с индексом i).
        '''
        if i < 0 or i >= self._capacity:
            raise IndexError("Переданный индекс за границами массива!")
        self._array[i] = item

    def remove_item(self, i: int) -> None:
        '''
        Команда удаляет элемент из ячейки с индексом i
        (предусловие - индекс в границах массива)
        (постусловие - ячейка с индексом i очищена).
        '''
        if i < 0 or i >= self._capacity:
            raise IndexError("Переданный индекс за границами массива!")
        self._array[i] = Void


class Stack(ABC):
    '''
    Класс "Стек", абстрактный.
    '''

    @abstractmethod
    def __init__(self, max_size: int) -> None:
        '''
        Конструктор получает максимальный размер стека
        (постусловие - создан пустой стек с заданным максимальным размером).
        '''
        ...

    @abstractmethod
    def size(self) -> int:
        '''
        Запрос возвращает текущий размер стека
        (предусловий нет).
        '''
        ...

    @abstractmethod
    def peek(self) -> Numeric:
        '''
        Запрос возвращает верхний элемент стека
        (предусловие - стек не пустой).
        '''
        ...

    @abstractmethod
    def push(self, item: Numeric) -> None:
        '''
        Команда укладывает значение в стек
        (предусловие - стек не полон)
        (постусловие - добавлено значение в стек)
        '''
        ...

    @abstractmethod
    def pop(self) -> None:
        '''
        Команда удаляет верхнее значение из стека
        (предусловие стек не пуст)
        (постусловие - удалено верхнее значение из стека)
        '''
        ...


@final
class StackException(Exception):
    pass


class StackArray(Stack, Array):
    '''
    Класс "Стек на основе массива".
    Класс реализует стек на основе массива. 
    Этот вид наследования - наследование реализации (implementation inheritance).
    '''

    @override
    def __init__(self, max_size: int) -> None:
        '''
        Конструктор получает максимальный размер стека
        (постусловие - создан пустой стек с заданным максимальным размером,
        текущий размер стека установлен в 0).
        '''
        Array.__init__(self, max_size)
        self._size = 0

    @override
    def size(self) -> int:
        '''
        Запрос возвращает текущий размер стека
        (предусловий нет).
        '''
        return self._size

    @override
    def peek(self) -> Numeric:
        '''
        Запрос возвращает верхний элемент стека
        (предусловие - стек не пустой).
        '''
        if self._size == 0:
            raise StackException("Стек пустой!")
        return cast(Numeric, self.get_item(self._size - 1))

    @override
    def push(self, item: Numeric) -> None:
        '''
        Команда укладывает значение в стек
        (предусловие - стек не полон)
        (постусловие - добавлено значение в стек и увеличен на 1 размер стека)
        '''
        if self._size == self.capacity():
            raise StackException("Стек полон!")
        self.put_item(self._size, item)
        self._size += 1

    @override
    def pop(self) -> None:
        '''
        Команда удаляет верхнее значение из стека
        (предусловие стек не пуст)
        (постусловие - удалено верхнее значение из стека и уменьшен на 1 размер стека)
        '''
        if self._size == 0:
            raise StackException("Стек пустой!")
        self.remove_item(self._size - 1)
        self._size -= 1
