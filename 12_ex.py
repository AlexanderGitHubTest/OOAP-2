'''
Создаются следующие объекты и методы:
Класс General и его потомок Any.
Класс General (базовый, абстрактный) содержит методы:
- копирование объекта (копирование содержимого одного объекта в другой существующий, включая DeepCopy - глубокое копирование всей структуры);
- клонирование (создание нового объекта и глубокое копирование в него исходного объекта);
- сравнение объектов (включая глубокий вариант);
- сериализация/десериализация (перевод в формат для удобного ввода-вывода, как правило, строковый и восстановление из него);
- печать (наглядное представление в текстовом формате);
- проверка типа (является ли тип текущего объекта указанным типом);
- получение реального типа объекта (непосредственного класса, экземпляром которого он был создан).
- попытка присвоить переменной ссылки на другой объект.
'''


import copy
import pickle
from typing import final, Final, Any as TypingAny


@final
class NoneClass:
    '''
    Конечный класс для всех "классов-листьев"
    Не имеет пользовательских методов и не разрешено наследование.
    '''
    __slots__ = ()

    def __init_subclass__(cls, **kwargs):
        raise TypeError("Наследование от NoneClass запрещено")


VOID: Final[NoneClass] = NoneClass()


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

    @final
    def copy_to(self: T, object_copy_to: T) -> None:
        '''
        Копирует данные из одного объекта в другой.
        Копирует данные "из себя" в объект, который передан методу, как параметр)
        Копирование глубокое (всей структуры).
        Задамся тем, что объекты одного типа.
        Задамся тем, что после копирования второй объект должен стать
        идентичным первому (то есть поля, которые есть во втором, но 
        нет в первом, будут удалены).
        Допущение 1 - буду использовать deepcopy, но 
        допустимость объектов для данной функции сам проверять не буду,
        оставлю вывод ошибок за deepcopy (deepcopy не всё умеет копировать).
        Допущение 2 - работает только с классами, у которых есть __dict__.
        '''
        self_names_set = set(self.__dict__)
        object_copy_to_names_set = set(object_copy_to.__dict__)
        # 1. Удалим объекты, которые есть только во втором классе
        for attr in object_copy_to_names_set - self_names_set:
            delattr(object_copy_to, attr)
        # 2. Добавим или изменим объекты, которые есть в первом классе
        for name, value in self.__dict__.items():
            setattr(object_copy_to, name, copy.deepcopy(value))

    @final
    def clone(self: T) -> T:
        '''
        Клонирует данные "из себя" в новый объект. Возвращает этот объект.
        Клонирование глубокое (всей структуры).
        Допущение 1 - буду использовать deepcopy, но 
        допустимость объектов для данной функции сам проверять не буду,
        оставлю вывод ошибок за deepcopy (deepcopy не всё умеет копировать).
        Допущение 2 - работает только с классами, у которых есть __dict__.
        '''
        return copy.deepcopy(self)

    @final
    def __eq__(self, obj: TypingAny) -> bool:
        '''
        Сравнивает "себя" с переданным методу объектом.

        '''
        return self.__dict__ == obj.__dict__

    @final
    def serialize(self) -> bytes:
        '''
        Сериализует себя.
        '''
        return pickle.dumps(self)

    @final
    @staticmethod
    def deserialize(object_serialization: bytes) -> TypingAny:
        '''
        Десериализует в объект.
        '''
        return pickle.loads(object_serialization)

    @final
    def __repr__(self) -> str:
        '''
        Выводит себя в текстовом формате.
        '''
        return f"Класс: {self.__class__.__name__}, id: {id(self)}."

    @final
    def is_current_specified_type(self, specified_type: str) -> bool:
        '''
        Проверка, является ли тип текущего объекта указанным типом
        (методу передаётся текстовое название типа).
        '''
        return self.__class__.__name__ == specified_type

    @final
    def get_object_type(self) -> str:
        '''
        Получить реальный тип объекта (непосредственного класса, 
        экземпляром которого он был создан).
        Метод возвращает текстовое название типа.
        '''
        return self.__class__.__name__

    @final
    def assignment_attempt(self, target: T | NoneClass, source: TypingAny) -> T | NoneClass:
        '''
        Если тип target и source одинаковый,
        либо тип target родительский по отношению к типу source,
        то возвращает source.
        Иначе возвращает значение VOID (экземпляр NoneClass).
        Выполнен как запрос, так как в python нельзя присвоить новое значение
        переданной переменной. Для чистоты функции не меняет состояния объекта.
        '''
        if isinstance(source, type(target)):
            return source
        return VOID


class Any(General):
    '''
    Наcледник General, от которого должны создаваться объекты.
    '''
    pass
