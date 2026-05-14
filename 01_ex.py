from abc import ABC, abstractmethod


class Mover(ABC):
    '''
    Движитель - абстрактный класс.
    '''
    def __init__(self, name: str, power_horsepower: int):
        self.name = name # Название
        self.power_horsepower = power_horsepower # Мощность (л.с.)
    @abstractmethod
    def check_mover(self) -> bool:
        '''
        Проверить движитель
        '''
        ...

class InternalCombustionEngine(Mover):
    '''
    Двигатель внутреннего сгорания
    '''
    def check_mover(self) -> bool:
        print("Проверить уровень масла")
        return True

class Horse(Mover):
    '''
    Лошадь
    '''
    def check_mover(self) -> bool:
        print("Осмотреть лошадь")
        return True


class TransportVehicle(ABC):
    '''
    Транспортное средство - абстрактный класс
    '''
    def __init__(self, name: str, mover: Mover, max_speed_km_h: int):
        self.name = name # Название
        # КОМПОЗИЦИЯ:
        # "Транспортное средство содержит Движитель"
        self.mover = mover # Движитель это объект класса "Движитель"
        self.max_speed_km_h = max_speed_km_h # Максимальная скорость
    @abstractmethod
    def start_moving(self) -> None:
        ''' Начать движение '''
        pass
    @abstractmethod
    def stop_moving(self) -> None:
        ''' Прекратить движение '''
        pass

class Car(TransportVehicle):
    '''
    НАСЛЕДОВАНИЕ:
    Автомобиль - наследник класса Транспортное средство
    "Автомобиль - это транспортное средство"

    Добавлен атрибут "Пассажировместимость"
    '''
    def __init__(self, name: str, mover, max_speed_km_h: int, passenger_capacity: int):
        super().__init__(name, mover, max_speed_km_h)
        self.passenger_capacity = passenger_capacity # Пассажировместимость
    def start_moving(self) -> None:
        ''' Начать движение '''
        print("Автомобиль поехал")
    def stop_moving(self) -> None:
        ''' Прекратить движение '''
        print("Автомобиль остановился")

class HorseDrawnCarriage(TransportVehicle):
    '''
    НАСЛЕДОВАНИЕ:
    Гужевая повозка - наследник класса Транспортное средство
    "Гужевая повозка - это транспортное средство"

    Добавлен атрибут "Тип повозки"
    '''
    def __init__(self, name: str, mover, max_speed_km_h: int, carriage_type: int):
        super().__init__(name, mover, max_speed_km_h)
        self.carriage_type = carriage_type # Тип повозки
    def start_moving(self) -> None:
        ''' Начать движение '''
        print("Н-но!")
    def stop_moving(self) -> None:
        ''' Прекратить движение '''
        print("Тпру!")


def main() -> None:
    vehicle = Car(
        'Такси',
        InternalCombustionEngine('Бензиновый двигатель', 150),
        200,
        4)
    carriage = HorseDrawnCarriage(
        'Телега с лошадью',
        Horse('Стрелка', 1),
        30,
        'Телега')
    '''
    ПОЛИМОРФИЗМ: 
    при вызове одного и того же метода (start_moving()) разные действия в зависимости от класса экземпляра.
    '''
    vehicle.start_moving()
    # Автомобиль поехал
    carriage.start_moving()
    # Н-Но

if __name__ == "__main__":
    main()
