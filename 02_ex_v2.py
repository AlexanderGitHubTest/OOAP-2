from abc import ABC, abstractmethod


class Phone(ABC):
    '''
    Абстрактный лласс - Телефон.
    '''
    def __init__(self, name: str) -> None:
        self.name = name  # Название
    @abstractmethod
    def make_call(self, phone_number: str) -> None:
        ''' Позвонить '''
        ...
    @abstractmethod
    def accept_call(self) -> None:
        ''' Принять звонок '''
        ...


class Smartphone(Phone):
    '''
    Класс - Смартфон.
    # РАСШИРЕНИЕ класса-родителя.
    Смарфон "умеет" звонить и принимать звонок (как родитель),
    но также может запустить браузер или сделать фотографию
    '''
    def make_call(self, phone_number: str) -> None:
        '''
        Позвонить - реализуем метод
        '''
        print(f"Набран номер {phone_number}.")
    def accept_call(self) -> None:
        '''
        Принять звонок - реализуем метод
        '''
        print("Звонок принят.")
    def launch_browser(self) -> None:
        ''' Запустить браузер '''
        print("Браузер запущен")
    def take_photo(self) -> None:
        ''' Сделать фотографию '''
        print("Фотография готова")


class WiredPhone(Phone):
    '''
    Класс - Проводной телефон.
    # СПЕЦИАЛИЗАЦИЯ класса-родителя.
    Проводной телефон - более конкретный вариант телефона
    '''
    def __init__(self, name: str, wire_length_meters: int) -> None:
        super().__init__(name: str)
        self.wire_length_meters = wire_length_meters  # Длина провода в метрах
    def make_call(self, phone_number: str) -> None:
        '''
        Позвонить - реализуем метод
        '''
        print(f"Набран номер {phone_number}.")

    def accept_call(self) -> None:
        '''
        Принять звонок - реализуем метод
        '''
        print("Звонок принят.")
