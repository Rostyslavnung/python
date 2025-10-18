class Vehicle:
    def __init__(self, make, model, year, price, speed):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__price = price
        self.__speed = speed

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def get_speed(self):
        return self.__speed

    def set_price(self, price):
        self.__price = price

    def set_speed(self, speed):
        self.__speed = speed

    def display_info(self):
        return (f"Марка: {self.__make}, Модель: {self.__model}, "
                f"Рік: {self.__year}, Ціна: {self.__price}$, "
                f"Швидкість: {self.__speed} км/год")


class Airplane(Vehicle):
    def __init__(self, make, model, year, price, speed, altitude, passengers):
        super().__init__(make, model, year, price, speed)
        self.__altitude = altitude
        self.__passengers = passengers

    def display_info(self):
        return (super().display_info() +
                f", Висота: {self.__altitude} м, Пасажирів: {self.__passengers}")


class Car(Vehicle):
    def __init__(self, make, model, year, price, speed, fuel_type):
        super().__init__(make, model, year, price, speed)
        self.__fuel_type = fuel_type

    def display_info(self):
        return (super().display_info() +
                f", Тип палива: {self.__fuel_type}")


class Ship(Vehicle):
    def __init__(self, make, model, year, price, speed, passengers, port):
        super().__init__(make, model, year, price, speed)
        self.__passengers = passengers
        self.__port = port

    def display_info(self):
        return (super().display_info() +
                f", Пасажирів: {self.__passengers}, Порт приписки: {self.__port}")


vehicles = [
    Airplane("Boeing", "747", 2015, 150_000_000, 900, 10000, 416),
    Car("Tesla", "Model S", 2022, 80_000, 250, "Електро"),
    Ship("Royal Caribbean", "Harmony", 2018, 1_000_000_000, 45, 6780, "Маямі")
]

for v in vehicles:
    print(v.display_info())

print("\nПошук транспорту після 2020 року:")
for v in vehicles:
    if v.get_year() >= 2020:
        print(v.display_info())
