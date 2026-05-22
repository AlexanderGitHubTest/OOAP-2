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


def main() -> None:
    movers: list[Mover] = [
        InternalCombustionEngine("Бензиновый двигатель", 150),
        Horse("Стрелка", 1),
    ]
    for mover in movers:
        mover.check_mover()
    # Проверить уровень масла
    # Осмотреть лошадь


if __name__ == "__main__":
    main()
