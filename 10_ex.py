'''
1. Классы A и B. Использование декоратора final.
Python код исполнит. Предупреждение при проверке напишет тайп-чекер типа mypy.

2. Классы C и D. Использование __init_subclass__. В таком варианте python по сути
запрещает использование данного имени потомкам (исключение будет вызвано при инициализации класса-потомка).

'''


from typing import final

class A:
    @final
    def __init__(self) -> None:
        pass

class B(A):
    def __init__(self) -> None:
        pass

class C:
    _prohibited_for_inheritance = "method_c_only"
    def __init_subclass__(cls, **kwargs):
        if cls._prohibited_for_inheritance in cls.__dict__:
            raise TypeError(f"Метод {cls._prohibited_for_inheritance} запрещено переопределять!")        
        super().__init_subclass__(**kwargs)
    def method_c_only(self) -> None:
        pass

class D(C):
    def method_c_only(self) -> None:
        pass
