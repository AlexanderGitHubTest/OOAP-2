'''
Думаю, что "-- расширение класса-родителя (наследник задаёт более общий случай родителя);"
это не когда мы добавляем функциональности, а когда все "родители" входят в множество "наследников" (обратное неверно),
то есть, например, мы "от отвёртки наследуем инструменты". Обычно наследование идёт в обратном порядке
'''


class Vehicle:
    '''
    Класс - Автомобиль.
    '''
    def __init__(self, name: str, max_speed_km_h: int):
        self.name = name  # Название
        self.max_speed_km_h = max_speed_km_h  # Максимальная скорость
    def start_moving(self) -> None:
        ''' Начать движение '''
        print("Автомобиль поехал.")
    def stop_moving(self) -> None:
        ''' Прекратить движение '''
        print("Автомобиль остановился.")


class TransportVehicle(Vehicle):
    '''
    Класс - Транспортное средство.
    # РАСШИРЕНИЕ класса-родителя.
    От Автомобиля наследуем Транспортное средство.
    Транспортное средство - включает автомобили, но не ограничивается ими.
    '''
    def __init__(self, name: str, max_speed_km_h: int, max_movement_height_km: int):
        super().__init__(name, max_speed_km_h)
        self.max_movement_height_km = max_movement_height_km  # Максимальная высота движения, км
    def start_moving(self) -> None:
        ''' Начать движение '''
        print("Транспортное средство начало двигаться.")
    def stop_moving(self) -> None:
        ''' Прекратить движение '''
        print("Транспортное средство остановилось.")


class CargoVehicle(Vehicle):
    '''
    Класс - Грузовой автомобиль.
    # СПЕЦИАЛИЗАЦИЯ класса-родителя.
    От Автомобиля наследуем Грузовой автомобиль.
    Грузовой автомобиль является автомобилем, но есть другие, не грузовые автомобили.
    '''
    def __init__(self, name: str, max_speed_km_h: int, load_capacity_tons: int):
        super().__init__(name, max_speed_km_h)
        self.load_capacity_tons = load_capacity_tons  # Грузоподъёмность, тонн
